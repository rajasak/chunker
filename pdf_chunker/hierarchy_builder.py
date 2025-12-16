import re

SECTION_RE = re.compile(r'^(\d+(?:\.\d+)*)(?:\.)?\s+')

def _depth(num: str) -> int:
    return num.count(".") + 1


def build_hierarchy(sections):
    stack = []
    output = []
    last_numbered = None

    for sec in sections:
        title = sec["title"]
        text = sec["text"]

        match = SECTION_RE.match(title)

        node = {
            "chunk_number": None,
            "title": title,
            "text": f"{title}\n{text}".strip(),
            "image_path": sec["image_path"],
            "children": []
        }

        if match:
            number = match.group(1)
            node["chunk_number"] = number

            while stack and _depth(stack[-1]["chunk_number"]) >= _depth(number):
                stack.pop()

            if stack:
                stack[-1]["children"].append(node)
            else:
                output.append(node)

            stack.append(node)
            last_numbered = node
        else:
            if last_numbered:
                last_numbered["children"].append(node)
            else:
                output.append(node)

    return output


def build_flat(sections):
    chunks = []

    for sec in sections:
        match = SECTION_RE.match(sec["title"])
        chunks.append({
            "chunk_number": match.group(1) if match else None,
            "title": sec["title"],
            "text": f"{sec['title']}\n{sec['text']}".strip(),
            "image_path": sec["image_path"]
        })

    return chunks
