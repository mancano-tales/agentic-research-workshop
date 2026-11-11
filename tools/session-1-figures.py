"""Gera os esquemas visuais da Sessão 1.

Uso, na raiz do repositório: python3 tools/session-1-figures.py
Saída: PNG de 300 dpi em sessions/01-introduction-ecosystem/images/.
Coordenadas: 1 unidade = 0,1 polegada, com origem no canto inferior esquerdo.
Todas as figuras têm 80 unidades de largura e entram no slide com width=100%.
"""
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Rectangle

OUT = Path(__file__).resolve().parents[1] / "sessions/01-introduction-ecosystem/images"

plt.rcParams["font.family"] = "Arial"

# Azul do tema Madrid; âmbar e vermelho sempre com rótulo, nunca como única pista.
BLUE = "#3333B2"
DARK = "#1C1C66"
RAMP = ["#E9E9F8", "#C9CBF0", "#9A9DE0", "#6668C9", "#3333B2"]
GRAY = "#5F6472"
LIGHT = "#F1F2F6"
LINE = "#D5D8E3"
AMBER = "#B87400"
AMBER_T = "#F8E3BC"
RED = "#C62828"
RED_T = "#F9DADA"
GREEN_T = "#D8F0DD"
INK = "#20222B"
WHITE = "#FFFFFF"

# Escala do texto: as figuras são reduzidas à largura do slide.
# FS vale para os diagramas densos; BIG, para os esquemas de cartões com pouco texto.
FS = 1.25
BIG = 1.42
_scale = FS

# Totais da execução em lab/demo-literature/backup/ (ver dados/ naquela pasta).
FUNNEL = [
    ("241", "encontrados"),
    ("236", "com resumo"),
    ("60", "na lista curta"),
    ("12", "fichados"),
]


def canvas(height, ymin=0, scale=FS):
    global _scale
    _scale = scale
    fig, ax = plt.subplots(figsize=(8, height / 10))
    ax.set_xlim(0, 80)
    ax.set_ylim(ymin, ymin + height)
    ax.axis("off")
    fig.subplots_adjust(0, 0, 1, 1)
    return fig, ax


def rounded(x, y, w, h, r, **kw):
    return FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", **kw)


def card(ax, x, y, w, h, fc=WHITE, ec=LINE, r=1.2, lw=0.9, shadow=True, z=2):
    if shadow:
        ax.add_patch(rounded(x + 0.3, y - 0.45, w, h, r, fc=DARK, ec="none", alpha=0.13, zorder=z - 1))
    ax.add_patch(rounded(x, y, w, h, r, fc=fc, ec=ec, lw=lw, zorder=z))


def text(ax, x, y, s, fs=10, color=INK, weight="normal", ha="center", va="center", **kw):
    kw.setdefault("zorder", 6)
    kw.setdefault("linespacing", 1.2)
    ax.text(x, y, s, fontsize=fs * _scale, color=color, fontweight=weight, ha=ha, va=va, **kw)


def node(ax, x, y, w, h, s, fc=BLUE, color=WHITE, fs=10.5, weight="bold", r=1.0, shadow=True):
    card(ax, x, y, w, h, fc=fc, ec="none", r=r, shadow=shadow)
    text(ax, x + w / 2, y + h / 2, s, fs, color, weight)


def arrow(ax, a, b, color=GRAY, lw=1.8, rad=0.0, ls="-", ms=13):
    ax.add_patch(
        FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=ms, color=color, lw=lw, linestyle=ls, connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0, zorder=4)
    )


def badge(ax, x, y, s, fc=BLUE, color=WHITE, r=1.35):
    ax.add_patch(Circle((x, y), r, fc=fc, ec="none", zorder=5))
    text(ax, x, y - 0.05, s, 9, color, "bold")


def save(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=300, facecolor=WHITE)
    plt.close(fig)


def measure(ax, s, fs, weight="normal"):
    """Largura do texto, em unidades do desenho."""
    probe = ax.text(0, 0, s, fontsize=fs * _scale, fontweight=weight)
    box = probe.get_window_extent(ax.figure.canvas.get_renderer())
    probe.remove()
    (x0, _), (x1, _) = ax.transData.inverted().transform([(box.x0, box.y0), (box.x1, box.y1)])
    return x1 - x0


def pills(ax, x, y, width, options, fs=8.8, h=2.7, pad=1.2, gap=0.8, row=3.3):
    """Opções em pílulas, com quebra de linha quando passam da largura."""
    cx, cy = x, y
    for s in options:
        w = measure(ax, s, fs) + 2 * pad
        if cx > x and cx + w > x + width:
            cx, cy = x, cy - row
        ax.add_patch(rounded(cx, cy - h / 2, w, h, h / 2, fc=RAMP[0], ec=RAMP[2], lw=0.8, zorder=3))
        text(ax, cx + w / 2, cy, s, fs)
        cx += w + gap


def survey():
    fig, ax = canvas(34.5, scale=BIG)
    h = 15.5
    cards = [
        (2, 18, 37, "Com que frequência você usa\nchatbots de IA na pesquisa?", ["nunca", "já testei", "toda semana", "quase todo dia"]),
        (41, 18, 37, "Já usou um agente que roda\ncomandos ou edita arquivos?", ["não sei o que é", "nunca usei", "já testei", "uso regularmente"]),
        (2, 1.5, 27, "Já usou IA para\nclassificar dados\nde uma análise?", ["sim", "não", "pretendo"]),
        (31, 1.5, 47, "O que mais preocupa você no\nuso de agentes na pesquisa?", ["erros difíceis de perceber", "sigilo dos dados", "perder habilidades", "custo", "regras e ética"]),
    ]
    for i, (x, y, w, question, options) in enumerate(cards):
        card(ax, x, y, w, h)
        badge(ax, x + 3, y + h - 3.2, str(i + 1), r=1.55)
        text(ax, x + 5.6, y + h - 2, question, 9.6, INK, "bold", ha="left", va="top")
        lines = question.count("\n") + 1
        pills(ax, x + 2, y + h - 2 - lines * 2.3 - 2.6, w - 4, options)
    save(fig, "survey")


def stats():
    fig, ax = canvas(16, scale=BIG)
    text(ax, 1, 14.3, "1.260 cientistas sociais quantitativos, fev.-mar. de 2026", 9, GRAY, ha="left")
    tiles = [
        ("81%", "usaram\nchatbots na\npesquisa"),
        ("20%", "usam\nagentes"),
        ("25%", "dos cientistas\npolíticos usam\nagentes"),
    ]
    for i, (number, caption) in enumerate(tiles):
        x = 1 + i * 26.35
        card(ax, x, 1, 25.3, 11)
        text(ax, x + 1.8, 6.4, number, 20, BLUE, "bold", ha="left")
        text(ax, x + 11, 6.5, caption, 9, ha="left")
    save(fig, "stats")


def loop():
    fig, ax = canvas(34)
    text(ax, 16, 31.6, "Chat", 13.5, DARK, "bold")
    node(ax, 3, 23.3, 11, 5, "Você", AMBER)
    node(ax, 18, 23.3, 11, 5, "Modelo", BLUE)
    for y, (a, b), s in [
        (19.6, (8.5, 23.5), "pedido"),
        (15.6, (23.5, 8.5), "resposta"),
        (11.6, (8.5, 23.5), "próximo pedido"),
    ]:
        arrow(ax, (a, y), (b, y))
        text(ax, 16, y + 1.4, s, 9, GRAY)
    card(ax, 2, 1.8, 28, 6.6, fc=LIGHT, ec="none", shadow=False)
    text(ax, 16, 5.1, "Poucas ferramentas: busca na web\ne arquivos que você envia", 9.2)

    ax.plot([33, 33], [2, 32.5], color=LINE, lw=1.5)

    cx, cy, a, b = 56, 15.5, 15, 10.5
    text(ax, cx, 31.6, "Agente", 13.5, DARK, "bold")
    ax.add_patch(Ellipse((cx, cy), 2 * a, 2 * b, fc="none", ec=RAMP[2], lw=2.4, zorder=1))
    for deg in (45, -45, -135, 135):
        t = math.radians(deg)
        px, py = cx + a * math.cos(t), cy + b * math.sin(t)
        dx, dy = a * math.sin(t), -b * math.cos(t)
        norm = math.hypot(dx, dy)
        dx, dy = dx / norm, dy / norm
        arrow(ax, (px - 0.9 * dx, py - 0.9 * dy), (px + 0.9 * dx, py + 0.9 * dy), BLUE, lw=2.4, ms=17)
    w, h = 12.5, 4.8
    for s, (x, y) in {
        "Decidir": (cx, cy + b),
        "Executar": (cx + a, cy),
        "Observar": (cx, cy - b),
        "Reavaliar": (cx - a, cy),
    }.items():
        node(ax, x - w / 2, y - h / 2, w, h, s, BLUE)
    text(ax, cx, cy, "ferramentas:\nterminal, seus\narquivos, web", 9.3, GRAY)
    node(ax, 66.5, 27.3, 12.5, 5.6, "Volta a você\npara validar", AMBER, fs=8.8)
    arrow(ax, (62.25, 27.2), (66.5, 29.4), AMBER, ls="--", lw=1.5)
    save(fig, "loop")


def anatomy():
    fig, ax = canvas(30)
    card(ax, 2, 6.5, 55, 22.5, fc=RAMP[0], ec=RAMP[2], r=1.6, lw=1.2)
    text(ax, 4.5, 26.2, "Harness: o programa em volta do modelo", 12, DARK, "bold", ha="left")
    text(ax, 4.5, 23.3, "define as ferramentas, monta o contexto, impõe limites", 9.3, GRAY, ha="left")
    node(ax, 5, 11.5, 13, 8.5, "Modelo\n(o LLM)", BLUE, fs=11.5)
    node(ax, 23.5, 12.75, 12.5, 6, "Permitido?", AMBER, fs=10)
    card(ax, 41, 11.5, 13.5, 8.5, fc=DARK, ec="none")
    text(ax, 47.75, 17.6, "Ferramentas", 10.3, WHITE, "bold")
    text(ax, 47.75, 14.2, "terminal,\narquivos, web", 8.8, WHITE)
    card(ax, 62, 11.5, 16, 8.5)
    text(ax, 70, 17.6, "Seu computador", 10, INK, "bold")
    text(ax, 70, 14.2, "arquivos, dados,\ninternet", 8.8)
    arrow(ax, (18, 15.75), (23.5, 15.75))
    text(ax, 20.75, 17.2, "pede", 8.8, GRAY)
    arrow(ax, (36, 15.75), (41, 15.75))
    text(ax, 38.5, 17.2, "sim", 8.8, GRAY)
    arrow(ax, (54.5, 15.75), (62, 15.75))
    ax.plot([70, 70, 11.5], [11.5, 8.6, 8.6], color=GRAY, lw=1.8, zorder=4, solid_capstyle="round", solid_joinstyle="round")
    arrow(ax, (11.5, 8.6), (11.5, 11.5))
    text(ax, 40.5, 9.9, "resultado", 8.8, GRAY)
    text(ax, 40, 2.8, "Janela de contexto: tudo o que o modelo vê agora.\nEla tem limite, e o que precisa durar fica em arquivos.", 9.3, GRAY)
    save(fig, "anatomy")


def window(ax, x, y, w, h, bg):
    card(ax, x, y, w, h, fc=bg, ec=GRAY, r=0.9, lw=0.8)
    for i, c in enumerate(["#E5534B", "#E8A317", "#46A758"]):
        ax.add_patch(Circle((x + 1.3 + i * 1.3, y + h - 1.2), 0.42, color=c, zorder=5))


def windows():
    fig, ax = canvas(34, 2.5)
    y, h, w = 11.5, 21.5, 24.5
    xs = [1.5, 27.75, 54]

    x = xs[0]
    window(ax, x, y, w, h, "#1E2230")
    lines = ["$ claude", "> conte as grafias", "  da coluna partido", "", "  PT: 3 grafias", "  MDB: 2 grafias", "> _"]
    for i, s in enumerate(lines):
        text(ax, x + 1.3, y + h - 4 - i * 2.3, s, 7.8, "#E8EAF0", ha="left", family="DejaVu Sans Mono")

    x = xs[1]
    window(ax, x, y, w, h, WHITE)
    ax.add_patch(Rectangle((x + 0.3, y + 0.4), 4.6, h - 3, color=LIGHT, zorder=3))
    for i in range(5):
        ax.add_patch(Rectangle((x + 1, y + h - 5 - i * 2), 3.2, 0.7, color=RAMP[1], zorder=4))
    for i, (bg, s) in enumerate([(RED_T, "- P.T."), (GREEN_T, "+ PT"), (RED_T, "- M.D.B."), (GREEN_T, "+ MDB")]):
        ax.add_patch(Rectangle((x + 5.4, y + h - 6 - i * 2.4), 10.6, 2, color=bg, zorder=3))
        text(ax, x + 6, y + h - 5 - i * 2.4, s, 7.6, ha="left", family="DejaVu Sans Mono")
    node(ax, x + 5.2, y + 1.3, 5.4, 2.3, "Aceitar", BLUE, fs=6.9, r=0.4, shadow=False)
    node(ax, x + 10.9, y + 1.3, 5.4, 2.3, "Rejeitar", GRAY, fs=6.9, r=0.4, shadow=False)
    ax.add_patch(rounded(x + 16.8, y + 0.8, 7, h - 3.6, 0.5, fc=RAMP[0], ec="none", zorder=3))
    text(ax, x + 20.3, y + h / 2 - 1, "painel\ndo\nagente", 8.2)

    x = xs[2]
    window(ax, x, y, w, h, WHITE)
    ax.add_patch(Rectangle((x + 0.3, y + 0.4), 6.2, h - 3, color=LIGHT, zorder=3))
    text(ax, x + 3.4, y + h - 4.3, "sessões", 7.6, GRAY)
    for i in range(4):
        ax.add_patch(Rectangle((x + 1, y + h - 7 - i * 2.3), 4.8, 0.8, color=RAMP[1], zorder=4))
    for i, wid in enumerate([13, 10, 14]):
        ax.add_patch(Rectangle((x + 7.6, y + h - 5.2 - i * 2.4), wid, 1, color=LIGHT, zorder=3))
    ax.add_patch(rounded(x + 7.6, y + 1.3, 15.6, 7.2, 0.5, fc=RAMP[0], ec="none", zorder=3))
    text(ax, x + 15.4, y + 4.9, "Alterações\n+12  -4\ncomentar por linha", 8.2)

    captions = [
        ("Terminal", "Você lê o que mudou no texto.\nDifícil sem programar."),
        ("Editor: VS Code, Positron", "Lado a lado: aceita ou rejeita\ncada trecho."),
        ("App desktop", "Painel de alterações.\nA porta mais fácil."),
    ]
    for x, (title, caption) in zip(xs, captions):
        text(ax, x + w / 2, 35, title, 11, DARK, "bold")
        text(ax, x + w / 2, 6.6, caption, 9)
    save(fig, "windows")


def timeline():
    fig, ax = canvas(27, scale=BIG)
    ax.plot([5, 75], [21.5, 21.5], color=RAMP[2], lw=2.4, zorder=1, solid_capstyle="round")
    arrow(ax, (75, 21.5), (77.5, 21.5), RAMP[2], lw=2.4, ms=16)
    items = [
        (14, "2025", "19% mais tempo", "Desenvolvedores com IA,\nem experimento do METR.\nAcreditavam ter sido\n20% mais rápidos."),
        (40, "2026", "+0,5 working paper", "a mais em seis meses,\nentre cientistas sociais\ncom agentes. O METR já\navalia que o ganho hoje\né maior."),
        (66, "Hoje", "Parece muito real", "A evidência ainda é\nfraca. O ganho aparece\nem ambição e qualidade:\nem código, o agente\ncostuma errar menos."),
    ]
    for x, year, headline, body in items:
        ax.plot([x, x], [18, 21.5], color=RAMP[2], lw=1.8, zorder=1)
        ax.add_patch(Circle((x, 21.5), 1.25, fc=BLUE, ec=WHITE, lw=2, zorder=5))
        text(ax, x, 24.9, year, 12.5, DARK, "bold")
        card(ax, x - 12.8, 1.5, 25.6, 16.5)
        text(ax, x - 11.1, 15.3, headline, 10.5, BLUE, "bold", ha="left")
        text(ax, x - 11.1, 13.1, body, 9, ha="left", va="top")
    save(fig, "timeline")


def plans():
    fig, ax = canvas(31, scale=BIG)
    products = [
        (2, "Claude (Anthropic)", "Claude Code incluído a partir do Pro", [
            ("Free", "sem o Claude Code", "US$ 0", False),
            ("Pro", "cerca de R$ 110", "US$ 20", True),
            ("Max", "", "US$ 100", False),
            ("Ultra", "", "US$ 200", False),
        ]),
        (41, "ChatGPT (OpenAI)", "Codex incluído em todos os planos", [
            ("Free", "", "US$ 0", False),
            ("Go", "", "US$ 8", False),
            ("Plus", "cerca de R$ 110", "US$ 20", True),
            ("Pro", "", "a partir de US$ 100", False),
        ]),
    ]
    for x, title, subtitle, rows in products:
        card(ax, x, 1.5, 37, 28)
        text(ax, x + 2.2, 26.4, title, 12, DARK, "bold", ha="left")
        text(ax, x + 34.8, 26.3, "por mês", 8.8, GRAY, ha="right")
        text(ax, x + 2.2, 23.2, subtitle, 8.8, GRAY, ha="left")
        for i, (name, note, price, highlight) in enumerate(rows):
            y = 18.4 - i * 4.4
            if highlight:
                ax.add_patch(rounded(x + 1.1, y - 1.9, 34.8, 3.8, 0.9, fc=RAMP[0], ec="none", zorder=3))
            elif i > 0 and not rows[i - 1][3]:
                ax.plot([x + 2.2, x + 34.8], [y + 2.2, y + 2.2], color=LINE, lw=0.8, zorder=3)
            text(ax, x + 2.2, y, name, 10.5, INK, "bold", ha="left")
            if note:
                text(ax, x + 9.2, y, note, 8.4, GRAY, ha="left")
            text(ax, x + 34.8, y, price, 10.5, BLUE if highlight else INK, "bold" if highlight else "normal", ha="right")
    save(fig, "plans")


def cost():
    fig, ax = canvas(31)
    base = 5.5
    ax.plot([6, 76], [base, base], color=GRAY, lw=1, zorder=5)
    card(ax, 11, base, 24, 21, fc=BLUE, ec="none", r=0.6, shadow=False)
    text(ax, 23, base + 14, "Produzir", 12, WHITE, "bold")
    text(ax, 23, base + 7.5, "verificar e entender\nvinham juntos", 10, WHITE)
    text(ax, 23, 2.6, "Antes", 12.5, DARK, "bold")
    card(ax, 45, base, 12, 5, fc=BLUE, ec="none", r=0.6, shadow=False)
    text(ax, 51, base + 8.2, "Produzir\nficou barato", 10, INK, "bold")
    card(ax, 61, base, 12, 19, fc=AMBER, ec="none", r=0.6, shadow=False)
    text(ax, 67, base + 12, "Verificar", 11, WHITE, "bold")
    text(ax, 67, base + 6.5, "continua\ncaro", 10, WHITE)
    text(ax, 59, 2.6, "Com agentes", 12.5, DARK, "bold")
    text(ax, 3.2, base + 10, "custo em tempo", 9, GRAY, rotation=90)
    text(ax, 76, 29, "Esquema, sem escala numérica", 8.8, GRAY, ha="right")
    save(fig, "cost")


def matrix():
    fig, ax = canvas(36)
    x0, y0, cw, ch = 11, 6.5, 34, 14.5
    cells = [
        (x0, y0 + ch, RAMP[1], INK, "Melhor uso", "Coletor conferido com fonte que\no agente não usou; o mesmo\nestimador em vários pacotes"),
        (x0 + cw, y0 + ch, RED, WHITE, "Perigo", "Decidir se a variável mede a\nposição; escolher controles e\nestratégia de identificação"),
        (x0, y0, RAMP[0], INK, "Delegue", "Padronizar partidos e datas"),
        (x0 + cw, y0, AMBER_T, INK, "Armadilha", "Codificar 2.000 discursos; fichar\nliteratura (o erro não aparece)"),
    ]
    for x, y, fc, color, name, body in cells:
        card(ax, x + 0.3, y + 0.3, cw - 0.6, ch - 0.6, fc=fc, ec="none", r=0.9, shadow=False)
        text(ax, x + 2, y + ch - 2.7, name, 14.5, color, "bold", ha="left")
        text(ax, x + 2, y + ch - 5.1, body, 10, color, ha="left", va="top")
    text(ax, x0 + cw / 2, y0 - 2, "Fácil", 10.5)
    text(ax, x0 + cw * 1.5, y0 - 2, "Difícil", 10.5)
    text(ax, x0 + cw, y0 - 5.2, "Dificuldade de verificar", 11.5, DARK, "bold")
    text(ax, x0 - 2.4, y0 + ch / 2, "Fácil", 10.5, rotation=90)
    text(ax, x0 - 2.4, y0 + ch * 1.5, "Difícil", 10.5, rotation=90)
    text(ax, x0 - 6.3, y0 + ch, "Dificuldade de fazer", 11.5, DARK, "bold", rotation=90)
    save(fig, "matrix")


def delegate():
    fig, ax = canvas(33, scale=BIG)

    def panel(x, w, color, title, mark, items):
        card(ax, x, 1.5, w, 30)
        ax.add_patch(rounded(x, 26.2, w, 5.3, 1.2, fc=color, ec="none", zorder=3))
        ax.add_patch(Rectangle((x, 26.2), w, 2.6, color=color, zorder=3))
        cx, cy = x + 3.6, 28.85
        ax.add_patch(Circle((cx, cy), 1.6, fc=WHITE, ec="none", zorder=5))
        if mark == "x":
            for d in (-1, 1):
                ax.plot([cx - 0.7, cx + 0.7], [cy - 0.7 * d, cy + 0.7 * d], color=color, lw=2.4, zorder=6, solid_capstyle="round")
        else:
            ax.plot([cx - 0.8, cx - 0.25, cx + 0.8], [cy, cy - 0.65, cy + 0.7], color=color, lw=2.4, zorder=6, solid_capstyle="round", solid_joinstyle="round")
        text(ax, x + 6.6, 28.8, title, 12, WHITE, "bold", ha="left")
        for i, (head, sub) in enumerate(items):
            y = 21.6 - i * 7.6
            ax.add_patch(Circle((x + 2.8, y + 1.1), 0.55, fc=color, ec="none", zorder=5))
            text(ax, x + 4.8, y + 1.1, head, 9.8, INK, "bold", ha="left")
            if sub:
                text(ax, x + 4.8, y - 0.4, sub, 9, GRAY, ha="left", va="top")

    panel(2, 42.5, RED, "Não delegue", "x", [
        ("A escrita", "do texto que você assina"),
        ("O que você precisa entender", "para responder pela autoria"),
        ("O que você ainda deveria aprender", "quem se substitui não aprende\ne não avança"),
    ])
    panel(46.5, 31.5, BLUE, "Pode delegar", "check", [
        ("O que você domina", "e já está consolidado"),
        ("O que você sabe conferir", ""),
    ])
    save(fig, "delegate")


def path():
    fig, ax = canvas(20.5)
    steps = [
        ("Pergunta", "Fundeb e\ndesigualdade", True),
        ("Busca", "API do\nOpenAlex", False),
        ("Seleção", "12 trabalhos", False),
        ("Fichas", "uma por\ntrabalho", False),
        ("Síntese", "uma página\ne .bib", False),
        ("Conferência", "DOI, resumo,\no que ficou fora", True),
    ]
    w, gap, x = 11.6, 1.6, 1.2
    text(ax, 40, 18.7, "Pedido em linguagem natural, em uma pasta vazia", 9.5, GRAY)
    for i, (name, sub, you) in enumerate(steps):
        node(ax, x, 9.5, w, 6.8, name, AMBER if you else BLUE, fs=9.6)
        text(ax, x + w / 2, 6, sub, 8.6)
        if i < len(steps) - 1:
            arrow(ax, (x + w + 0.15, 12.9), (x + w + gap - 0.1, 12.9), GRAY, ms=9, lw=1.4)
        x += w + gap
    ax.add_patch(rounded(28, 0.7, 2.2, 2.2, 0.4, fc=AMBER, ec="none"))
    text(ax, 31, 1.8, "você", 9.3, ha="left")
    ax.add_patch(rounded(42, 0.7, 2.2, 2.2, 0.4, fc=BLUE, ec="none"))
    text(ax, 45, 1.8, "agente", 9.3, ha="left")
    save(fig, "demo-path")


def check():
    fig, ax = canvas(28, scale=BIG)
    steps = [
        (2, 15, RAMP[0], INK, GRAY, "Fácil", "O DOI existe e leva\nao trabalho certo?", "Delegue"),
        (28, 19.5, AMBER_T, INK, GRAY, "Difícil", "A ficha diz o que o\nresumo diz? O agente\nacrescentou algo?", "Armadilha"),
        (54, 24, RED, WHITE, WHITE, "Mais difícil", "O que a busca\ndeixou de fora?", "Perigo"),
    ]
    for x, h, fc, color, muted, title, question, quadrant in steps:
        card(ax, x, 2, 24, h, fc=fc, ec="none")
        text(ax, x + 2, 2 + h - 2.9, title, 12, color, "bold", ha="left")
        text(ax, x + 2, 2 + h - 5.4, question, 9.6, color, ha="left", va="top")
        text(ax, x + 2, 4.2, f"na matriz: {quadrant}", 8.6, muted, ha="left")
    save(fig, "check")


def funnel():
    fig, ax = canvas(26, scale=BIG)
    w, gap, x, mid = 15.5, 4.2, 1.5, 16
    for i, (count, caption) in enumerate(FUNNEL):
        h = 16 - 2 * i
        color = WHITE if i >= 2 else INK
        card(ax, x, mid - h / 2, w, h, fc=RAMP[1 + i], ec="none", r=0.9)
        text(ax, x + w / 2, mid + 1.6, count, 17, color, "bold")
        text(ax, x + w / 2, mid - 2.6, caption, 9.6, color)
        if i < len(FUNNEL) - 1:
            arrow(ax, (x + w + 0.5, mid), (x + w + gap - 0.3, mid), GRAY, ms=11)
        x += w + gap
    text(ax, 40, 3.2, "Caixas sem escala. Cada passo é uma decisão de quem pesquisa,\nmesmo quando o agente a toma.", 8.8, GRAY)
    save(fig, "funnel")


def modes():
    fig, ax = canvas(31)
    rows = [
        ("Plan", "Leituras;\nsó propõe", "Você aprova\no plano", "Comece aqui em\ntarefa nova\nou grande", RAMP[0], INK),
        ("Manual", "Leituras", "Você, a\ncada ação", "Aprovar tudo\ncansa e vira\nreflexo", RAMP[1], INK),
        ("Accept edits", "Leituras e\nedições", "Você, nos\ncomandos", "Edita direto:\nleia o diff", RAMP[2], INK),
        ("Auto", "Quase tudo,\ncom checagem", "Um\nclassificador", "Menos pedidos,\nsem garantia\nde segurança", RAMP[4], WHITE),
        ("Bypass", "Tudo", "Ninguém", "Só em ambiente\nisolado", RED, WHITE),
    ]
    x0, w = 13, 13.2
    text(ax, 11.5, 21.5, "Roda sem\nperguntar", 9, GRAY, ha="right")
    text(ax, 11.5, 15.3, "Quem\ndecide", 9, GRAY, ha="right")
    text(ax, 11.5, 8.3, "Na\nprática", 9, GRAY, ha="right")
    ax.plot([x0, x0 + 5 * w], [18.4, 18.4], color=LINE, lw=1)
    ax.plot([x0, x0 + 5 * w], [12, 12], color=LINE, lw=1)
    for i, (name, runs, who, tip, fc, color) in enumerate(rows):
        x = x0 + i * w
        node(ax, x + 0.25, 25, w - 0.5, 4.6, name, fc, color, fs=9.8, r=0.7)
        text(ax, x + w / 2, 21.5, runs, 9.5)
        text(ax, x + w / 2, 15.3, who, 9.6, weight="bold")
        text(ax, x + w / 2, 8.3, tip, 8.9)
    arrow(ax, (x0 + 1, 3.2), (x0 + 5 * w - 1, 3.2), GRAY, lw=1.8)
    text(ax, x0 + 2.5 * w, 1.4, "mais autonomia para o agente", 9, GRAY)
    save(fig, "modes")


def case():
    fig, ax = canvas(29.5, scale=BIG)
    text(ax, 2, 27.8, "Relato de Manoel Galdino", 9, GRAY, ha="left")
    steps = [
        (2, RAMP[0], INK, BLUE, WHITE, "Modo automático", "o agente age sem pedir\naprovação a cada passo"),
        (28.5, WHITE, INK, BLUE, WHITE, "O agente decide", "enviar um e-mail"),
        (55, RED, WHITE, WHITE, RED, "E-mail enviado", "sem autorização"),
    ]
    for i, (x, fc, color, badge_fc, badge_color, title, body) in enumerate(steps):
        card(ax, x, 14.5, 23, 10.5, fc=fc, ec=LINE if fc == WHITE else "none")
        badge(ax, x + 3.1, 21.9, str(i + 1), badge_fc, badge_color, r=1.55)
        text(ax, x + 5.5, 21.9, title, 10.2, color, "bold", ha="left")
        text(ax, x + 2.2, 19.3, body, 9, color, ha="left", va="top")
        if i < len(steps) - 1:
            arrow(ax, (x + 23.4, 19.75), (x + 26.2, 19.75), GRAY, ms=12)
    card(ax, 2, 1.5, 76, 9.5, fc=AMBER_T, ec="none")
    node(ax, 3.8, 4.35, 10, 3.8, "Regra", AMBER, fs=9.5, r=0.9, shadow=False)
    text(ax, 16, 6.25, "O que não pode acontecer sem você pede uma regra no harness:\nenviar e-mail sempre exige aprovação.", 9.5, ha="left")
    save(fig, "case")


def prose_rule():
    fig, ax = canvas(34.5, 0.5)
    text(ax, 2, 33, "Prosa orienta", 13, DARK, "bold", ha="left")
    card(ax, 2, 22, 24, 8, fc=RAMP[0], ec="none")
    text(ax, 14, 26, "\"Por favor, não altere\nos dados brutos\"", 10)
    arrow(ax, (26, 26), (31, 26))
    node(ax, 31, 22, 15, 8, "O modelo\ndecide", BLUE, fs=11)
    arrow(ax, (46, 27.5), (54, 30))
    arrow(ax, (46, 24.5), (54, 22))
    card(ax, 54, 27, 24, 6, fc=RAMP[0], ec="none")
    text(ax, 66, 30, "quase sempre respeita", 10)
    card(ax, 54, 19, 24, 6, fc=RED_T, ec="none")
    text(ax, 66, 22, "às vezes, não", 10.3, weight="bold")

    ax.plot([2, 78], [16.6, 16.6], color=LINE, lw=1.5)

    text(ax, 2, 14, "Regra garante", 13, DARK, "bold", ha="left")
    card(ax, 2, 3.5, 24, 8, fc=RAMP[0], ec="none")
    text(ax, 14, 7.5, "Script que bloqueia escrita\nem dados/brutos/", 9.5)
    arrow(ax, (26, 7.5), (31, 7.5))
    node(ax, 31, 3.5, 15, 8, "O código\ndecide", AMBER, fs=11)
    arrow(ax, (46, 7.5), (54, 7.5))
    card(ax, 54, 4.5, 24, 6, fc=RAMP[1], ec="none")
    text(ax, 66, 7.5, "bloqueia sempre", 10.3, weight="bold")
    arrow(ax, (38.5, 3.5), (53.6, 1.7), RED, ls="--", lw=1.4, rad=0.08)
    text(ax, 78.5, 1.7, "só o que previu: um script escapa", 8.8, RED, ha="right")
    save(fig, "prose-rule")


FIGURES = (survey, stats, loop, anatomy, windows, timeline, plans, cost, matrix, delegate, path, check, funnel, modes, case, prose_rule)

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for make in FIGURES:
        make()
