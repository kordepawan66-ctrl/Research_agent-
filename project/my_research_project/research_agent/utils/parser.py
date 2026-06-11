import pypdf
import re

def extract_pdf_text(file_path):
    """Extracts raw text from an academic paper PDF."""
    reader = pypdf.PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def generate_apa_citation(metadata):
    """Autonomously formats a basic APA reference."""
    authors = metadata.get('authors', 'Unknown Author')
    year = metadata.get('year', 'n.d.')
    title = metadata.get('title', 'Untitled Document')
    journal = metadata.get('journal', 'Unknown Journal')
    
    return f"{authors} ({year}). {title}. *{journal}*."