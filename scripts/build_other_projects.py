"""Builds the "Otros proyectos" table as SVG images, in the same style as assets/stack.svg.

Each project is its own SVG row so the README can link every row to its repository.
To add a project: append it to PROJECTS, run `python scripts/build_other_projects.py`,
and add its <a><img></a> line to the README (the script prints it).
"""
from pathlib import Path
from xml.sax.saxutils import escape

PROJECTS = [
    {
        "file": "other-nexus.svg",
        "repo": "https://github.com/IrvinSegura/ISO-social",
        "name": "Nexus",
        "kind": "App Android",
        "description": "Red social con feed offline, historias con música, círculos privados "
                       "con código de invitación y mensajes directos entre miembros. "
                       "Multi-módulo con Clean Architecture y MVI.",
        "stack": ["Kotlin", "Jetpack Compose", "Hilt", "Room", "Firebase", "Supabase"],
    },
]

ACCENTS = ["#34D399", "#38BDF8", "#A78BFA", "#FBBF24", "#60A5FA"]

WIDTH = 1000
COL_NAME, COL_DESC, COL_STACK = 44, 250, 640
STACK_RIGHT = 976
DESC_CHARS_PER_LINE = 50
DESC_LINE_HEIGHT = 20
CHIP_HEIGHT, CHIP_GAP, CHIP_ROW = 26, 8, 34

ASSETS = Path(__file__).resolve().parent.parent / "assets"

HEAD = """<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title">
<title id="title">{title}</title>
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B1220"/><stop offset="1" stop-color="#0F1C30"/></linearGradient>
<radialGradient id="glow" cx="0.95" cy="0" r="0.8"><stop offset="0" stop-color="{accent}" stop-opacity=".12"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#FFFFFF" stroke-opacity=".035"/></pattern>
</defs>
<style>
.sans{{font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,'Helvetica Neue',Arial,sans-serif}}
.mono{{font-family:ui-monospace,SFMono-Regular,'Cascadia Mono',Consolas,Menlo,monospace}}
</style>
<rect x=".5" y=".5" width="{iw}" height="{ih}" rx="14" fill="url(#bg)"/>
<rect x=".5" y=".5" width="{iw}" height="{ih}" rx="14" fill="url(#grid)"/>
<rect x=".5" y=".5" width="{iw}" height="{ih}" rx="14" fill="url(#glow)" stroke="#1E2B3F"/>
"""


def svg_open(height, title, accent="#38BDF8"):
    return HEAD.format(w=WIDTH, h=height, iw=WIDTH - 1, ih=height - 1, title=escape(title), accent=accent)


def wrap(text, limit):
    lines, line = [], ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > limit:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    return lines + [line] if line else lines


def chip_width(label):
    return round(7.2 * len(label) + 22)


def layout_chips(labels):
    rows, x, row = [[]], COL_STACK, 0
    for label in labels:
        w = chip_width(label)
        if rows[row] and x + w > STACK_RIGHT:
            rows.append([])
            row, x = row + 1, COL_STACK
        rows[row].append((x, w, label))
        x += w + CHIP_GAP
    return rows


def build_header():
    height = 84
    out = [svg_open(height, "Otros proyectos: proyecto, qué hace y tecnologías")]
    out.append('<text x="40" y="38" class="mono" font-size="12" font-weight="600" fill="#38BDF8" '
               'letter-spacing="1.5">OTROS PROYECTOS · CLIC EN UNO PARA VER SU REPOSITORIO</text>')
    for x, label in ((COL_NAME, "PROYECTO"), (COL_DESC, "QUÉ HACE"), (COL_STACK, "TECNOLOGÍAS")):
        out.append(f'<text x="{x}" y="66" class="mono" font-size="10" font-weight="600" fill="#8B9AB0" '
                   f'letter-spacing="1.2">{label}</text>')
    out.append(f'<line x1="24" y1="76" x2="{WIDTH - 24}" y2="76" stroke="#26364F"/>')
    out.append("</svg>\n")
    return "\n".join(out)


def build_row(project, accent):
    desc = wrap(project["description"], DESC_CHARS_PER_LINE)
    chips = layout_chips(project["stack"])
    content = max(len(desc) * DESC_LINE_HEIGHT, len(chips) * CHIP_ROW - CHIP_GAP, 58)
    height = content + 48
    top = 24

    title = f'{project["name"]} ({project["kind"]}): {project["description"]} Tecnologías: {", ".join(project["stack"])}.'
    out = [svg_open(height, title, accent)]
    out.append(f'<rect x="24" y="{top - 6}" width="3" height="{height - 2 * (top - 6)}" rx="1.5" fill="{accent}"/>')
    out.append(f'<text x="{COL_NAME}" y="{top + 14}" class="mono" font-size="15" font-weight="700" fill="{accent}" '
               f'letter-spacing="1.2">{escape(project["name"].upper())}</text>')
    out.append(f'<text x="{COL_NAME}" y="{top + 34}" class="mono" font-size="11" font-weight="600" fill="#8B9AB0" '
               f'letter-spacing="1.1">{escape(project["kind"].upper())}</text>')
    out.append(f'<text x="{COL_NAME}" y="{height - 20}" class="mono" font-size="11" font-weight="600" fill="#E6EDF3" '
               f'fill-opacity=".7">Ver repositorio →</text>')
    for i, line in enumerate(desc):
        out.append(f'<text x="{COL_DESC}" y="{top + 14 + i * DESC_LINE_HEIGHT}" class="sans" font-size="14" '
                   f'fill="#E6EDF3">{escape(line)}</text>')
    for r, row in enumerate(chips):
        y = top + r * CHIP_ROW
        for x, w, label in row:
            out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{CHIP_HEIGHT}" rx="13" fill="{accent}" '
                       f'fill-opacity=".08" stroke="{accent}" stroke-opacity=".45"/>'
                       f'<text x="{x + w / 2}" y="{y + 17.32}" class="mono" font-size="12" font-weight="500" '
                       f'fill="#E6EDF3" text-anchor="middle">{escape(label)}</text>')
    out.append("</svg>\n")
    return "\n".join(out)


def main():
    (ASSETS / "other-projects-header.svg").write_text(build_header(), encoding="utf-8")
    lines = ['<img src="assets/other-projects-header.svg" width="100%" alt="Otros proyectos" />']
    for i, project in enumerate(PROJECTS):
        accent = ACCENTS[i % len(ACCENTS)]
        (ASSETS / project["file"]).write_text(build_row(project, accent), encoding="utf-8")
        alt = f'{project["name"]}: {project["kind"]}. {project["description"]}'
        lines.append(f'<a href="{project["repo"]}"><img src="assets/{project["file"]}" width="100%" alt="{escape(alt, {chr(34): "&quot;"})}" /></a>')
    print("\n".join(lines))


if __name__ == "__main__":
    main()
