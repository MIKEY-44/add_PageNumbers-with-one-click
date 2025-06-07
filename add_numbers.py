from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
import os

def add_page_numbers(input_pdf, output_pdf, start_number=1, font_size=10, x_offset=40, y_offset=40):
    # Register Times New Roman (macOS path)
    font_path = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"
    if not os.path.exists(font_path):
        raise FileNotFoundError("Times New Roman font not found. Please check the font path.")
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for i, page in enumerate(reader.pages):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=(width, height))
        page_number = f"{i + start_number}"

        can.setFont("TimesNewRoman", font_size)
        can.drawRightString(width - x_offset, y_offset, page_number)  # y_offset increased to move text up
        can.save()

        packet.seek(0)
        overlay = PdfReader(packet)
        page.merge_page(overlay.pages[0])
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

# === Run the function ===
add_page_numbers(
    input_pdf="neednumber.pdf",
    output_pdf="for_code_numbered.pdf",
    start_number=1,
    font_size=10,
    x_offset=40,
    y_offset=40  # Increased y_offset to move the page number up
)
