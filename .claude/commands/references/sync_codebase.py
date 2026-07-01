#!/usr/bin/env python3
"""
knowledge-bridge: sync_codebase.py
Scans a VSCode project and generates a manifest for Obsidian module notes.

Usage: python sync_codebase.py <project_path> [output_manifest.json]

Note: This script does the file-system work. Claude Code reads the generated
manifest.json and writes the actual note content using its code understanding.
"""

import sys
import os
import json
from datetime import date
from pathlib import Path

SKIP_DIRS = {
    "node_modules", ".git", "__pycache__", ".next", "dist", "build",
    ".venv", "venv", ".env", "coverage", ".nyc_output", ".pytest_cache",
    "target", ".cargo", "vendor"
}
SKIP_EXTENSIONS = {
    ".pyc", ".pyo", ".class", ".o", ".so", ".dll", ".exe",
    ".jpg", ".png", ".gif", ".svg", ".ico", ".woff", ".ttf",
    ".lock", ".sum", ".min.js", ".min.css"
}
CODE_EXTENSIONS = {
    ".py", ".ts", ".tsx", ".js", ".jsx", ".go", ".rs", ".java",
    ".cpp", ".c", ".h", ".rb", ".php", ".swift", ".kt", ".scala",
    ".cs", ".ex", ".exs", ".clj"
}

def scan_project(project_path: str) -> dict:
    root = Path(project_path)
    manifest = {
        "project_path": str(root.resolve()),
        "project_name": root.name,
        "scanned_at": date.today().isoformat(),
        "structure": {},
        "entry_points": [],
        "config_files": [],
        "code_files": [],
        "todos": [],
        "stats": {}
    }

    markers = {
        "package.json": "nodejs",
        "pyproject.toml": "python",
        "setup.py": "python",
        "Cargo.toml": "rust",
        "go.mod": "go",
        "pom.xml": "java",
        "build.gradle": "java",
        "Gemfile": "ruby",
    }
    detected_type = "unknown"
    for marker, lang in markers.items():
        if (root / marker).exists():
            detected_type = lang
            manifest["config_files"].append(str(root / marker))
            break
    manifest["project_type"] = detected_type

    code_count = 0
    for path in root.rglob("*"):
        if any(skip in path.parts for skip in SKIP_DIRS):
            continue
        if not path.is_file():
            continue
        if path.suffix in SKIP_EXTENSIONS:
            continue

        rel = path.relative_to(root)
        str_rel = str(rel)

        if path.suffix in CODE_EXTENSIONS:
            code_count += 1
            entry = {"path": str_rel, "extension": path.suffix, "size": path.stat().st_size}

            if path.name in ("main.py", "index.ts", "index.js", "main.go",
                             "app.py", "server.py", "app.ts", "__main__.py"):
                manifest["entry_points"].append(str_rel)

            try:
                with open(path, "r", errors="ignore") as f:
                    for i, line in enumerate(f):
                        if i > 100:
                            break
                        if "TODO" in line or "FIXME" in line or "HACK" in line:
                            manifest["todos"].append({
                                "file": str_rel,
                                "line": i + 1,
                                "text": line.strip()[:120]
                            })
            except Exception:
                pass

            manifest["code_files"].append(entry)

    manifest["stats"] = {
        "total_code_files": code_count,
        "entry_points": len(manifest["entry_points"]),
        "todos": len(manifest["todos"])
    }

    def build_tree(path, depth=0, max_depth=2):
        if depth > max_depth:
            return {}
        result = {}
        try:
            for item in sorted(path.iterdir()):
                if item.name.startswith("."):
                    continue
                if item.name in SKIP_DIRS:
                    continue
                if item.is_dir():
                    result[item.name + "/"] = build_tree(item, depth + 1, max_depth)
                else:
                    result[item.name] = item.suffix
        except PermissionError:
            pass
        return result

    manifest["structure"] = build_tree(root)
    return manifest


def save_manifest(manifest: dict, output_path: str):
    with open(output_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Manifest saved: {output_path}")
    print(f"   Files: {manifest['stats']['total_code_files']} code files")
    print(f"   Entry points: {manifest['entry_points']}")
    print(f"   TODOs found: {manifest['stats']['todos']}")
    print(f"\nClaude Code will now read this manifest and generate Obsidian notes.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sync_codebase.py <project_path> [output_manifest.json]")
        sys.exit(1)

    project_path = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else "/tmp/kb-manifest.json"

    print(f"Scanning: {project_path}")
    manifest = scan_project(project_path)
    save_manifest(manifest, output)
