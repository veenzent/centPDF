from fastapi.testclient import TestClient
from ..pdfapp import dependencies


def test_rotate_page():
    response = dependencies.rotate_page()
    pass

def test_rotate_pdf():
    response = dependencies.rotate_pdf()
    pass

def test_merge_pdf_files():
    response = dependencies.merge_pdf_files()
    pass

def test_split_pdf():
    dependencies.split_pdf()
    pass