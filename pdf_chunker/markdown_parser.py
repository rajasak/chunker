import re
from typing import List, Tuple

# Matches: 1, 1.1, 2.3.4 etc
SECTION_RE = re.compile(r'^\d+(?:\.\d+)*\.?\s+')

#mcp
def extract_sections_from_markdown(markdown: str) -> List[Tuple[str, str]]:
    """
    Extract (title, text) pairs from markdown using heading markers.
    """
    heading_re = re.compile(r'^(#{1,6})\s*(.+)')

    sections = []
    current_heading = None
    current_lines = []

    def commit():
        if current_heading is not None:
            sections.append(
                (current_heading, "\n".join(current_lines).strip())
            )

    for line in markdown.splitlines():
        m = heading_re.match(line)
        if m:
            commit()
            current_heading = m.group(2).strip()
            current_lines = []
        else:
            current_lines.append(line)

    commit()
    return sections


def merge_child_sections(
    sections: List[Tuple[str, str]]
) -> List[Tuple[str, str]]:
    """
    Merge unnumbered child headings into the nearest numbered parent section.
    """

    merged = []
    current_title = None
    current_text = []

    for title, text in sections:
        title = title.strip()
        text = text.strip()

        # REAL numbered section (1, 1.1, 2.3.4 ...)
        if SECTION_RE.match(title):
            # commit previous section
            if current_title is not None:
                merged.append(
                    (current_title, "\n".join(current_text).strip())
                )

            current_title = title
            current_text = [text] if text else []

        # CHILD heading → merge into parent
        else:
            if current_title is None:
                continue  # orphan → skip safely

            # keep child heading visible
            current_text.append(title)
            if text:
                current_text.append(text)

    # commit last section
    if current_title is not None:
        merged.append(
            (current_title, "\n".join(current_text).strip())
        )

    return merged

def markdown_to_sections(markdown: str) -> List[Tuple[str, str]]:
    """
    High-level API:
    Markdown → extracted sections → merged sections
    """
    raw_sections = extract_sections_from_markdown(markdown)
    return merge_child_sections(raw_sections)

def markdown_to_sections(markdown: str) -> List[Tuple[str, str]]:
    """
    High-level API:
    Markdown → extracted sections → merged sections
    """
    raw_sections = extract_sections_from_markdown(markdown)
    return merge_child_sections(raw_sections)

def markdown_to_sections(markdown: str) -> List[Tuple[str, str]]:
    """
    High-level API:
    Markdown → extracted sections → merged sections
    """
    raw_sections = extract_sections_from_markdown(markdown)
    return merge_child_sections(raw_sections)

