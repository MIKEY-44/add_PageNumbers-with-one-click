# PDF Page Numbering Script

This Python script adds page numbers to an existing PDF file using the `pypdf` and `reportlab` libraries. It places page numbers at the bottom-right corner of each page with a customizable font, size, and position.

---

## Features

- Adds page numbers starting from any number you choose (default is 1)
- Customizable font size and positioning offsets
- Uses Times New Roman font (macOS default path, configurable)
- Works with any PDF size or page count

---

## Requirements

- Python 3.x
- `pypdf` library
- `reportlab` library

You can install the required packages using pip:

```bash
pip install pypdf reportlab

Usage

## Place your input PDF file in the same directory as the script or provide the full path.
Update the input_pdf and output_pdf filenames as needed.
Run the script.
python add_page_numbers.py


Customization options
start_number: The starting page number (default: 1)
font_size: Size of the page number font (default: 10)
x_offset: Horizontal offset from the right edge (default: 40)
y_offset: Vertical offset from the bottom edge (default: 40; increase to move page numbers higher)



~example:

add_page_numbers(
    input_pdf="for_code.pdf",
    output_pdf="for_code_numbered.pdf",
    start_number=1,
    font_size=10,
    x_offset=40,
    y_offset=40
)

