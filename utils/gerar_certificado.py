from reportlab.pdfgen import canvas
from datetime import datetime
import os

def gerar_certificado(nome_participante, nome_palestra):
    nome_arquivo = f"certificado_{nome_participante.replace(' ', '_')}.pdf"
    data = datetime.now().strftime("%d/%m/%Y")
    c = canvas.Canvas(nome_arquivo)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 750, "Certificado de Participação")

    c.setFont("Helvetica", 14)
    texto = f"Certificamos que {nome_participante} participou da palestra \"{nome_palestra}\" em {data}."
    c.drawString(100, 700, texto)

    c.save()
    return nome_arquivo
