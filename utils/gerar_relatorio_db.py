from reportlab.pdfgen import canvas
from models.listagem_produtos import listagem_produtos
from models.listagem_usuarios import listagem_usuarios


def gerar_relatorio_db():

    c = canvas.Canvas("relatorio_db.pdf")
    y = 800

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Relatório de Produtos:")
    y -= 30

    c.setFont("Helvetica", 12)
    produtos = listagem_produtos()
    for produto in produtos:
        c.drawString(60, y, str(produto))
        y -= 20
        if y < 50:
            c.showPage()
            y = 800

    y -= 20
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Relatório de Usuários:")
    y -= 30

    c.setFont("Helvetica", 12)
    usuarios = listagem_usuarios()
    for usuario in usuarios:
        c.drawString(60, y, str(usuario))
        y -= 20
        if y < 50:
            c.showPage()
            y = 800

    c.save()

