$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path $PSScriptRoot -Parent
$decks = @(
    @{ Source = 'sessions/01-introduction-ecosystem/llm-agents-for-research-session-1-slides.qmd' },
    @{ Source = 'sessions/02-practical-skills/llm-agents-for-research-session-2-slides.qmd' }
)
Push-Location $repoRoot
try {
    # Versão na capa, como na dissertação: MAIOR.DIAS.BUILD, comum aos dois PDFs
    #   MAIOR = suba à mão numa reescrita geral dos slides
    #   DIAS  = dias distintos com render arquivado em _renders/ (mais hoje)
    #   BUILD = versões distintas arquivadas mais esta (cada render gera nome novo)
    $versaoMaior = 1
    $archiveDir = Join-Path $repoRoot '_renders'
    $archived = @(Get-ChildItem -Path $archiveDir -Filter *.pdf -ErrorAction SilentlyContinue)
    $now = Get-Date
    $days = @($archived | ForEach-Object { $_.Name.Substring(0, 10) }) + $now.ToString('yyyy-MM-dd') | Sort-Object -Unique
    $builds = @($archived | ForEach-Object { if ($_.Name -match '_v(\d+\.\d+\.\d+)\.pdf$') { $Matches[1] } } | Sort-Object -Unique)
    $versao = '{0}.{1}.{2}' -f $versaoMaior, $days.Count, ($builds.Count + 1)
    $capa = '\date{{\textcolor{{red}}{{\fbox{{\begin{{tabular}}{{c}}Versão {0}\\Renderizada em {1} às {2}\end{{tabular}}}}}}}}' -f $versao, $now.ToString('dd\/MM\/yyyy'), $now.ToString('HH\hmm')
    # Lido por madrid-header.tex; apagado ao fim, para um render avulso sair sem versão.
    [IO.File]::WriteAllText((Join-Path $repoRoot 'sessions/versao.tex'), $capa)

    New-Item -ItemType Directory -Path $archiveDir -Force | Out-Null
    foreach ($deck in $decks) {
        $renderStart = Get-Date
        & quarto render $deck.Source --to madrid-web-beamer
        if ($LASTEXITCODE -ne 0) { throw "Falha na renderização: $($deck.Source)" }
        $built = Join-Path $repoRoot (Join-Path '_site' ([IO.Path]::ChangeExtension($deck.Source, '.pdf')))
        if ((Get-Item -LiteralPath $built).LastWriteTime -lt $renderStart) {
            throw "O PDF em $built é de uma rodada anterior."
        }
        $datedName = '{0}_{1}_v{2}.pdf' -f $now.ToString('yyyy-MM-dd_HHmm'), [IO.Path]::GetFileNameWithoutExtension($deck.Source), $versao
        Copy-Item -LiteralPath $built -Destination (Join-Path $archiveDir $datedName) -Force
        Write-Output "PDF: _renders/$datedName"
    }
    Write-Output "Versão: $versao"
} finally {
    Remove-Item -LiteralPath (Join-Path $repoRoot 'sessions/versao.tex') -ErrorAction SilentlyContinue
    Pop-Location
}
