import argparse
from pathlib import Path

LATEX_HEADER = r"""
\documentclass{article}
\usepackage[a4paper,margin=1.5cm]{geometry}
\usepackage{listings}
\usepackage{xcolor}

\definecolor{keyword}{RGB}{0,0,180}
\definecolor{string}{RGB}{180,0,0}
\definecolor{comment}{RGB}{0,120,0}

\lstdefinestyle{python}{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{keyword}\bfseries,
    stringstyle=\color{string},
    commentstyle=\color{comment}\itshape,
    numbers=left,
    numberstyle=\tiny\color{gray},
    stepnumber=1,
    numbersep=8pt,
    showstringspaces=false,
    breaklines=true,
    frame=single
}

\begin{document}
\lstset{style=python}
"""

LATEX_FOOTER = r"""
\end{document}
"""


def escape_latex(text):
    replacements = {
        "\\": r"\textbackslash{}",
        "{": r"\{",
        "}": r"\}",
        "#": r"\#",
        "$": r"\$",
        "%": r"\%",
        "&": r"\&",
        "_": r"\_",
        "^": r"\^{}",
        "~": r"\~{}",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def convert_file(py_path, out_path):
    code = py_path.read_text(encoding="utf-8")
    code = escape_latex(code)

    tex = (
        LATEX_HEADER
        + f"\\section*{{{py_path.name}}}\n"
        + "\\begin{lstlisting}\n"
        + code
        + "\n\\end{lstlisting}\n"
        + LATEX_FOOTER
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(tex, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()

    for py_file in args.input_dir.rglob("*.py"):
        relative = py_file.relative_to(args.input_dir)
        tex_file = args.output_dir / relative.with_suffix(".tex")
        convert_file(py_file, tex_file)


if __name__ == "__main__":
    main()
