from io import BytesIO
import docx


def create_docx_in_memory(text):
    doc = docx.Document()
    doc.add_paragraph(text)
    
    file_stream = BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)  # Go to the beginning of the file stream
    return file_stream