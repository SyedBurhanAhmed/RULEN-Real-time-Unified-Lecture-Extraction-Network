from docx import Document
from docx.shared import Pt
import os
import re

DOCX_FOLDER = "output"
os.makedirs(DOCX_FOLDER, exist_ok=True)

def save_markdown_docx(markdown_text: str, filename: str) -> str:
    doc = Document()

    # Define simple styles
    style = doc.styles["Normal"]
    font = style.font
    font.name = "Calibri"
    font.size = Pt(11)

    lines = markdown_text.strip().splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            doc.add_paragraph()
            continue

        # **Bold Heading**
        if re.match(r"^\*\*(.+?)\*\*$", line):
            heading = re.findall(r"\*\*(.+?)\*\*", line)[0]
            doc.add_paragraph(heading, style="Heading 2")

        # Numbered list
        elif re.match(r"^\d+\.\s", line):
            doc.add_paragraph(line, style="List Number")

        # Bullet list
        elif re.match(r"^[-*+]\s", line):
            doc.add_paragraph(line[2:], style="List Bullet")

        else:
            doc.add_paragraph(line)

    # Save DOCX
    filename = filename if filename.endswith(".docx") else f"{filename}.docx"
    save_path = os.path.join(DOCX_FOLDER, filename)
    doc.save(save_path)
    return save_path
