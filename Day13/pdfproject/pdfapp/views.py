# pdfapp/views.py

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def generate_pdf(request):
    context = {
        'title': 'Test PDF',
        'message': 'Hello! This PDF was generated from Django.'
    }

    template = get_template('pdf_template.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="test.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors while generating PDF')
    return response
