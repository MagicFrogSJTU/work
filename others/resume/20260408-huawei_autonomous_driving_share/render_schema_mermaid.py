import re
import urllib.request
from pathlib import Path


BASE_DIR = Path(__file__).parent
SCHEMA_FILE = BASE_DIR / "schema.md"
OUTPUT_DIR = BASE_DIR / "generated_mermaid"


def slugify(title: str) -> str:
    slug = re.sub(r"[^0-9a-zA-Z\u4e00-\u9fff]+", "_", title).strip("_")
    return slug or "diagram"


def parse_mermaid_blocks(text: str) -> list[tuple[int, str, str]]:
    results = []
    current_slide = 0
    pattern = re.compile(r"```mermaid\n(.*?)\n```", re.DOTALL)

    parts = re.split(r"(^## 第\d+页 .*?$)", text, flags=re.MULTILINE)
    for index in range(1, len(parts), 2):
        header = parts[index].strip()
        body = parts[index + 1]
        match = re.match(r"## 第(\d+)页\s+(.*)$", header)
        if not match:
            continue
        current_slide = int(match.group(1))
        title = match.group(2).strip()
        block_index = 1
        for diagram in pattern.findall(body):
            results.append(
                (current_slide, f"{slugify(title)}_{block_index}", diagram.strip())
            )
            block_index += 1
    return results


def render_png(code: str, output_path: Path) -> None:
    request = urllib.request.Request(
        "https://kroki.io/mermaid/png",
        data=code.encode("utf-8"),
        method="POST",
        headers={
            "Content-Type": "text/plain; charset=utf-8",
            "User-Agent": "copilot-mermaid-renderer/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        output_path.write_bytes(response.read())


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    text = SCHEMA_FILE.read_text(encoding="utf-8")
    diagrams = parse_mermaid_blocks(text)
    for slide_no, name, code in diagrams:
        mmd_path = OUTPUT_DIR / f"slide{slide_no:02d}_{name}.mmd"
        png_path = OUTPUT_DIR / f"slide{slide_no:02d}_{name}.png"
        mmd_path.write_text(code + "\n", encoding="utf-8")
        render_png(code, png_path)
        print(f"rendered {png_path.name}")


if __name__ == "__main__":
    main()
