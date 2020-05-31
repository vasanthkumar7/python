from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdf=canvas.Canvas('fonts.pdf')
pdf.setTitle('fonts')
count=0
for font in pdf.getAvailableFonts():
    print(font)
    pdf.setFont(font,20)
    pdf.drawString(200,200+count,font)
    count=count+20
pdf.save()
