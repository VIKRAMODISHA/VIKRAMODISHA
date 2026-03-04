import PyPDF2

def extract_text(filepath):
    """Extract text from PDF file at the given filepath."""
    text = ""
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text() + '\n'
    return text.strip()