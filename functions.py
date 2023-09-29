from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime

def make_quotation_pdf(items_dataframe):

    debt = 0
    for index,row in items_dataframe.iterrows():
        debt += row['item_total_price'] 

    today_date = datetime.date.today()
    formated_date = today_date.strftime("%d/%m/%Y")
    w, h = letter
    pdf_canvas = canvas.Canvas("quotation.pdf", pagesize=letter)
    change_color(pdf_canvas, 63, 74, 37)
    pdf_canvas.rect(20, h-30, w-40, 10, fill=True)
    change_color(pdf_canvas, 220, 220, 220) 
    pdf_canvas.rect(20, h-180, w-40, 150, fill=True)
    change_color(pdf_canvas, 0, 0, 0) 
    pdf_canvas.setFont("Helvetica-Bold", 14)
    pdf_canvas.drawString(240,h-70,"Lorem Lácteos S.A. de C.V")
    pdf_canvas.setFont("Helvetica", 12)
    pdf_canvas.drawString(240,h-90,"55 12 12 34 34")
    pdf_canvas.drawString(240,h-105,"ventas@loremlacteos.com")
    pdf_canvas.drawImage("img/logo.png", 35, h-145, width=173, height=105)
    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(w-130, h-50, "ID COTIZACIÓN")
    pdf_canvas.setFont("Helvetica", 8)
    pdf_canvas.drawString(w-170, h-65, "03d4bfa2-07b4-4892-bcb0-7bd54f40567f")
    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(w-130, h-85, "FECHA")
    pdf_canvas.setFont("Helvetica", 10)
    pdf_canvas.drawString(w-130, h-100, formated_date)
    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(w-130, h-135, "SALDO DEUDOR")
    pdf_canvas.setFont("Helvetica", 10)
    pdf_canvas.drawString(w-130, h-150, "MXN $" + str(debt))
    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(40, h-210, "CLIENTE")
    pdf_canvas.setFont("Helvetica", 12)
    pdf_canvas.drawString(40, h-230, "Público en general")
    change_color(pdf_canvas, 80, 80, 80) 
    pdf_canvas.setFont("Helvetica", 11)
    pdf_canvas.drawString(40, h-255, "Sandra Hérnandez")
    pdf_canvas.drawImage("img/phone.jpg", 35, h-280, width=13, height=13)
    pdf_canvas.drawImage("img/cellphone.png", 35, h-295, width=9, height=11)
    pdf_canvas.drawString(50, h-280, "5548484848")
    pdf_canvas.drawString(50, h-295, "55112233444")
    pdf_canvas.drawString(40, h-310, "cliente@mail.com")

    print(w,h)
    change_color(pdf_canvas, 45, 45, 45)
    pdf_canvas.rect(20, h-350, w-40, 20, fill=True)
    change_color(pdf_canvas, 250, 250, 250) 
    pdf_canvas.setFont("Helvetica-Bold", 11)
    pdf_canvas.drawString(40, h-345, "ARTÍCULO")
    pdf_canvas.setFont("Helvetica-Bold", 9)
    pdf_canvas.drawString(380, h-345, "PRECIO UNITARIO")
    pdf_canvas.setFont("Helvetica-Bold", 10)
    pdf_canvas.drawString(480, h-345, "CANTIDAD")
    pdf_canvas.drawString(550, h-345, "TOTAL")

    sheet_h_space = h - 370
    for index, row in items_dataframe.iterrows():
        if sheet_h_space < 50:
            pdf_canvas.showPage()
            sheet_h_space = h - 50

        if index%2==0:
            change_color(pdf_canvas, 250, 250, 250) 
        else:
            change_color(pdf_canvas, 190, 190, 190)
        pdf_canvas.rect(20, sheet_h_space, w-40, 20, fill=True)

        change_color(pdf_canvas, 45, 45, 45)
        pdf_canvas.setFont("Helvetica-Bold", 11)
        pdf_canvas.drawString(40, sheet_h_space + 5, str(row['item_name']))
        pdf_canvas.setFont("Helvetica-Bold", 9)
        pdf_canvas.drawString(380, sheet_h_space + 5, "${:.2f}".format(row['item_unit_price']))
        pdf_canvas.setFont("Helvetica-Bold", 10)
        pdf_canvas.drawString(480, sheet_h_space + 5, str(int(row['item_quantity'])))
        pdf_canvas.drawString(550, sheet_h_space + 5, "${:.2f}".format(row['item_total_price']))
        sheet_h_space -= 20     

    
    if sheet_h_space < 50:
        pdf_canvas.showPage()
        sheet_h_space = h - 50
    change_color(pdf_canvas, 190, 190, 190)
    pdf_canvas.rect(270, sheet_h_space - 10, w-290, 30, fill=True)
    change_color(pdf_canvas, 45, 45, 45)
    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(300, sheet_h_space + 5, "Total:")
    pdf_canvas.drawString(530, sheet_h_space + 5, "${:.2f}".format(debt))
    pdf_canvas.save()

def change_color(canvas, cr, cb, cg):
    r = cr/255
    g = cb/255
    b = cg/255
    canvas.setFillColorRGB(r,g,b)
    return canvas
