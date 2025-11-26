from django.template.loader import get_template
from django.conf import settings
import os

from xhtml2pdf import pisa

def render_pdf(template_path, context, output_filename):
    safe_filename = output_filename.replace(" ", "_")
    template = get_template(template_path)
    html = template.render(context)

    pdf_folder = os.path.join(settings.MEDIA_ROOT, "pdfs")
    os.makedirs(pdf_folder, exist_ok=True)

    pdf_path = os.path.join(pdf_folder, safe_filename)

    with open(pdf_path, "wb") as pdf_file:
        pisa.CreatePDF(html, dest=pdf_file)

    return pdf_path
