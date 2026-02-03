import ast
import os

root = os.path.join(os.path.dirname(__file__), "..", "src")
root = os.path.normpath(root)

summary = {
    "files": 0,
    "files_missing_module_doc": 0,
    "classes": 0,
    "classes_missing": 0,
    "functions": 0,
    "functions_missing": 0,
}

print("Scanning", root)
print()

for dirpath, dirs, files in os.walk(root):
    for fn in files:
        if not fn.endswith(".py"):
            continue
        path = os.path.join(dirpath, fn)
        summary["files"] += 1
        rel = os.path.relpath(path, start=os.path.normpath(os.path.join(root, "..")))
        with open(path, "r", encoding="utf-8") as f:
            try:
                src = f.read()
                node = ast.parse(src)
            except Exception as e:
                print(rel, "-> parse error:", e)
                continue
        mod_doc = ast.get_docstring(node)
        missing_mod = not bool(mod_doc)
        if missing_mod:
            summary["files_missing_module_doc"] += 1
        classes_missing = []
        funcs_missing = []
        for n in node.body:
            if isinstance(n, ast.ClassDef):
                summary["classes"] += 1
                if not ast.get_docstring(n):
                    classes_missing.append(n.name)
                    summary["classes_missing"] += 1
                # check methods
                for m in n.body:
                    if isinstance(m, ast.FunctionDef):
                        summary["functions"] += 1
                        if not ast.get_docstring(m):
                            funcs_missing.append(f"{n.name}.{m.name}")
                            summary["functions_missing"] += 1
            elif isinstance(n, ast.FunctionDef):
                summary["functions"] += 1
                if not ast.get_docstring(n):
                    funcs_missing.append(n.name)
                    summary["functions_missing"] += 1

        if missing_mod or classes_missing or funcs_missing:
            print(f"{rel}:")
            if missing_mod:
                print("  - module docstring: MISSING")
            if classes_missing:
                print("  - classes missing docstrings:", ", ".join(classes_missing))
            if funcs_missing:
                print(
                    "  - functions/methods missing docstrings:",
                    ", ".join(funcs_missing),
                )
            print()

print("Summary:")
for k, v in summary.items():
    print(f"  {k}: {v}")
