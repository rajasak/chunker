import json
from pathlib import Path

from .converter import convert_pdf_to_doc
from .image_extractor import extract_images
from .markdown_parser import markdown_to_sections
from .image_linker import attach_images
from .hierarchy_builder import build_hierarchy, build_flat


def convert_pdf(
    pdf_path: str,
    output_dir: str,
    hierarchical: bool = True,
    flat: bool = True
):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    doc = convert_pdf_to_doc(pdf_path)

    images = extract_images(doc, output_dir / "images")
    sections = markdown_to_sections(doc.export_to_markdown())
    enriched = attach_images(sections, images)

    if hierarchical:
        with open(output_dir / "chunks_hierarchical.json", "w", encoding="utf-8") as f:
            json.dump(build_hierarchy(enriched), f, indent=2, ensure_ascii=False)

    if flat:
        with open(output_dir / "chunks_flat.json", "w", encoding="utf-8") as f:
            json.dump(build_flat(enriched), f, indent=2, ensure_ascii=False)
