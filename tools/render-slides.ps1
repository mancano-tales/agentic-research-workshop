param([string]$Source = 'aulas/agentes-ia-pesquisa.qmd')

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path $PSScriptRoot -Parent
Push-Location $repoRoot
try {
    if (-not (Test-Path -LiteralPath $Source)) { throw "Fonte inexistente: $Source" }
    $sourcePath = (Resolve-Path -LiteralPath $Source).Path
    if (-not $sourcePath.StartsWith($repoRoot, [StringComparison]::OrdinalIgnoreCase)) {
        throw 'A fonte deve estar dentro do repositório.'
    }
    $relativeSource = $sourcePath.Substring($repoRoot.Length).TrimStart('\', '/')

    # Versão na capa, como na dissertação: MAIOR.DIAS.BUILD
    #   MAIOR = suba à mão numa reescrita geral dos slides
    #   DIAS  = dias distintos com render arquivado em _renders/ (mais hoje)
    #   BUILD = total de PDFs arquivados mais este render
    $versaoMaior = 1
    $archiveDir = Join-Path $repoRoot '_renders'
    $archived = @(Get-ChildItem -Path $archiveDir -Filter *.pdf -ErrorAction SilentlyContinue)
    $now = Get-Date
    $days = @($archived | ForEach-Object { $_.Name.Substring(0, 10) }) + $now.ToString('yyyy-MM-dd') | Sort-Object -Unique
    $versao = '{0}.{1}.{2}' -f $versaoMaior, $days.Count, ($archived.Count + 1)
    $capa = '\date{{\textcolor{{red}}{{\fbox{{\begin{{tabular}}{{c}}Versão {0}\\Renderizada em {1} às {2}\end{{tabular}}}}}}}}' -f $versao, $now.ToString('dd/MM/yyyy'), $now.ToString('HH\hmm')
    # Lido por madrid-header.tex; apagado ao fim, para um render avulso sair sem versão.
    $versaoTex = Join-Path $repoRoot 'aulas/versao.tex'
    [IO.File]::WriteAllText($versaoTex, $capa)

    $renderStart = Get-Date
    & quarto render $relativeSource --to madrid-web-beamer
    if ($LASTEXITCODE -ne 0) { throw 'Falha na renderização: madrid-web-beamer' }
    $baseName = [IO.Path]::GetFileNameWithoutExtension($relativeSource)
    $outputRelative = Join-Path ([IO.Path]::GetDirectoryName($relativeSource)) $baseName
    $built = Join-Path $repoRoot (Join-Path '_site' "$outputRelative.pdf")
    if ((Get-Item -LiteralPath $built).LastWriteTime -lt $renderStart) {
        throw "O PDF em $built é de uma rodada anterior."
    }

    # Nome fixo em assets/: o link do site sempre serve a última versão.
    $target = Join-Path $repoRoot 'assets/agentes-ia-pesquisa.pdf'
    Copy-Item -LiteralPath $built -Destination $target -Force

    # Cópia datada em _renders/ (não versionada): é o arquivo para enviar.
    New-Item -ItemType Directory -Path $archiveDir -Force | Out-Null
    $datedName = '{0}_{1}_v{2}.pdf' -f $now.ToString('yyyy-MM-dd_HHmm'), $baseName, $versao
    Copy-Item -LiteralPath $built -Destination (Join-Path $archiveDir $datedName) -Force

    Write-Output "Versão: $versao"
    Write-Output "PDF datado: _renders/$datedName"
    Write-Output "PDF do site: assets/agentes-ia-pesquisa.pdf (versionar apos conferir)"
} finally {
    Remove-Item -LiteralPath (Join-Path $repoRoot 'aulas/versao.tex') -ErrorAction SilentlyContinue
    Pop-Location
}
