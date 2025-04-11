import ast
import textwrap

import astor


def extract_undocumented_functions(filepath):
    with open(filepath, "r") as f:
        source = f.read()
    tree = ast.parse(source)

    undocumented = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and ast.get_docstring(node) is None:
            source_segment = astor.to_source(node)
            undocumented.append({"node": node, "source": source_segment})
    return undocumented


def clean_docstring(raw: str) -> str:
    lines = raw.strip().splitlines()
    clean_lines = []

    for line in lines:
        if any(
            x in line.lower()
            for x in ["here is", "the following", "```", "triple quotes", "output:"]
        ):
            continue
        if line.strip().startswith('\\"""') or line.strip().endswith('\\"""'):
            continue
        if line.strip().startswith('"""') or line.strip().endswith('"""'):
            continue

        clean_lines.append(line.strip())

    cleaned = "\n".join(clean_lines)
    return textwrap.indent(cleaned, "    ")  # 4 espacios


def indent_docstring(docstring: str, indent_level: int = 1, spaces: int = 4) -> str:
    indentation = " " * (indent_level * spaces)
    return "\n".join(
        indentation + line if line.strip() != "" else ""
        for line in docstring.strip().splitlines()
    )


def insert_docstrings(filepath, documented_functions):
    with open(filepath, "r") as f:
        source = f.read()

    tree = ast.parse(source)

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            for func_obj, docstring in documented_functions:
                if node.name == func_obj["node"].name:
                    cleaned_docstring = clean_docstring(docstring)
                    # logger.debug(f"[Documenter] Inserting docstring for function: {node.name}")
                    # logger.debug(f"[Documenter] Docstring content:\n{cleaned_docstring}")
                    doc_node = ast.Expr(value=ast.Str(s=cleaned_docstring))
                    node.body.insert(0, doc_node)

    return astor.to_source(tree)


def save_to_output(original_path, content):
    import os

    from document_me.utils import safe_save

    filename = os.path.basename(original_path)

    # Ruta absoluta al directorio scripts/
    scripts_dir = os.path.abspath(os.path.join(os.path.dirname(original_path), ".."))

    # Ruta a documented_scripts/ en el mismo nivel que scripts/
    output_dir = os.path.join(scripts_dir, "documented_scripts")

    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, filename)

    safe_save(output_path, content)
