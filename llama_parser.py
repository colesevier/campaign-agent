# llama_parser.py
import re

def parse_llama_response(text):
    sections = {}
    current_section = None
    buffer = []

    def flush():
        nonlocal buffer, current_section
        if current_section:
            content = "\n".join(buffer).strip()
            sections[current_section] = content
        buffer.clear()

    for line in text.splitlines():
        stripped = line.strip()

        # Match markdown headers like ## Section Name
        header_match = re.match(r"^##\s+(.*)", stripped)
        if header_match:
            flush()
            current_section = header_match.group(1).strip()
        elif current_section:
            buffer.append(stripped)

    flush()

    if not sections:
        return {"Raw Output": text.strip()}

    return sections
