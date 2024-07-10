from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def create_pdf(filename, text):
    """
    Creates a PDF file with content in text argument

    Args:
        filename (str): The filename for the generated PDF.
        text (str): The content of the PDF.
    """
    # Create a PDF canvas
    pdf = canvas.Canvas(filename, pagesize=A4)

    # Set font and font size
    pdf.setFont("Helvetica", 18)

    # Draw the text at upper left corner with margins of (approximately) 50 points
    #   print(A4)
    w, h = A4
    pdf.drawCentredString(50, h - 50, text)
    # pdf.showPage()

    # Save the PDF
    pdf.save()
    print(f"PDF created successfully: {filename}")
