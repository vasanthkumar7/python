from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
filename=input("Enter name of the file to be saved as:")
filename=filename+".pdf"
pdf=canvas.Canvas(filename)

pdf.setTitle('resume')
name=input("Enter your name:")
name=name.capitalize()
pdf.setFont('Helvetica',20)
pdf.drawString(200,810,name)
pdf.setFont('Courier',10)
phno=input("Enter your phone number:")
email=input("Enter your Email id:")
acc=input("Enter your Linked in account:")
subhead=email+" | "+phno+" | "+acc
pdf.drawString(80,780,subhead)
pdf.line(0,770,830,770)

tem=10
#education
pdf.setFont('Courier',20)
pdf.drawString(10+tem,740,'EDUCATION:')

pdf.setFillColorRGB(0,0,0)
print("EDUCATION")
print("**********")
colname=input("Enter your college name: ")
colname =colname.upper()
pdf.setFont('Courier-Bold',15)
pdf.drawString(10+tem,720,colname)
pdf.setFont('Courier',10)
coursename=input("Enter the course name: ")
pdf.drawString(10+tem,705,coursename)
gp=input("Enter year of graduation and place(ex: year of Graduation 2022 | chennai,india):")
pdf.drawString(10+tem,695,gp)
cgpa=input("Enter CGPA:")
cgpa="cgpa:"+cgpa
pdf.drawString(10+tem,685,cgpa)
colname=input("Enter your college name: ")
colname =colname.upper()
pdf.setFont('Courier-Bold',15)
pdf.drawString(10+tem,665,colname)
pdf.setFont('Courier',10)
coursename=input("Enter the course name: ")
pdf.drawString(10+tem,650,coursename)
gp=input("Enter year of graduation and place(ex: year of Graduation 2022 | chennai,india):")
pdf.drawString(10+tem,640,gp)
cgpa=input("Enter CGPA:")
cgpa="cgpa:"+cgpa
pdf.drawString(10+tem,630,cgpa)

temp0=-55
pdf.setFont('Courier-Bold',15)
schlname=input("Enter your school name:")
pdf.drawString(10+tem,665+temp0,schlname)
pdf.setFont('Courier',10)
gp=input("Enter year of graduation and place(ex: year of Graduation 2022 | chennai,india):")
pdf.drawString(10+tem,650+temp0,gp)
cgpa=input("Enter CGPA:")
cgpa="cgpa:"+cgpa
pdf.drawString(10+tem,640+temp0,cgpa)

temp=-60

#projects
print(" ")
print(" ")
print("PROJECTS")
print("**********")

pdf.setFont('Courier',20)
pdf.drawString(10+tem,605+temp,'PROJECTS:')
pdf.setFont('Courier-Bold',15)
print("")
print("Project1")
proname=input("Enter your project name:")
proname=proname.upper()
pdf.drawString(10+tem,585+temp,proname)
pdf.setFont('Courier',10)
pp=input("Enter the time place when the project is built (ex:WINTER 2017 | chennai,india):")
pdf.drawString(10+tem,570+temp,pp)
som=input("whats the project objective or what tool is used build the project:")
som="  >"+som
pdf.drawString(10+tem,555+temp,som)
som=input("whats the concepts are implemented:")
som="  >"+som
pdf.drawString(10+tem,540+temp,som)
print("")
print("Project2")
pdf.setFont('Courier-Bold',15)
proname=input("Enter your project name:")
proname=proname.upper()
pdf.drawString(10+tem,520+temp,proname)
pdf.setFont('Courier',10)
pp=input("Enter the time place when the project is built (ex:WINTER 2017 | chennai,india):")
pdf.drawString(10+tem,505+temp,pp)
som=input("whats the project objective or what tool is used build the project:")
som="  >"+som
pdf.drawString(10+tem,490+temp,som)
som=input("whats the concepts are implemented:")
som="  >"+som
pdf.drawString(10+tem,480+temp,som)
print("")
print("Project3")
pdf.setFont('Courier-Bold',15)
proname=input("Enter your project name:")
proname=proname.upper()
pdf.drawString(10+tem,460+temp,proname)
pdf.setFont('Courier',10)
pp=input("Enter the time place when the project is built (ex:WINTER 2017 | chennai,india):")
pdf.drawString(10+tem,440+temp,pp)
som=input("whats the project objective or what tool is used build the project:")
som="  >"+som
pdf.drawString(10+tem,425+temp,som)
som=input("whats the concepts are implemented:")
som="  >"+som
pdf.drawString(10+tem,415+temp,som)

pdf.setFont('Courier-Bold',15)
print("")
print("Project4")
proname=input("Enter your project name:")
proname=proname.upper()
pdf.drawString(10+tem,395+temp,proname)
pdf.setFont('Courier',10)
pp=input("Enter the time place when the project is built (ex:WINTER 2017 | chennai,india):")
pdf.drawString(10+tem,375+temp,pp)
som=input("whats the project objective or what tool is used build the project:")
som="  >"+som
pdf.drawString(10+tem,360+temp,som)
som=input("whats the concepts are implemented:")
som="  >"+som
pdf.drawString(10+tem,345+temp,som)

pdf.setFont('Courier-Bold',15)
print("")
print("Project5")
proname=input("Enter your project name:")
pdf.drawString(10+tem,325+temp,proname)
pdf.setFont('Courier',10)
pp=input("Enter the time place when the project is built (ex:WINTER 2017 | chennai,india):")
pdf.drawString(10+tem,305+temp,pp)
som=input("whats the project objective or what tool is used build the project:")
som="  >"+som
pdf.drawString(10+tem,290+temp,som)
som=input("whats the concepts are implemented:")
som="  >"+som
pdf.drawString(10+tem,275+temp,som)

temp1=-75
#achivements
print("")
print("ACHIVEMENTS:")
print("*************")

pdf.setFont('Courier',20)
pdf.drawString(10+tem,255+temp1,'ACHIVEMENTS:')
pdf.setFont('Courier-Bold',15)
ach=input("In which field or competion you have achived:")
pdf.drawString(10+tem,235+temp1,ach)
ba=input("in that what is your achomplisment:")

pdf.setFont('Courier',10)
pdf.drawString(10+tem,220+temp1,ba)
print("")
ach=input("In which field or competion you have achived:")
pdf.setFont('Courier-Bold',15)
pdf.drawString(10+tem,200+temp1,ach)
pdf.setFont('Courier',10)
ba=input("in that what is your achomplisment:")
pdf.drawString(10+tem,180+temp1,ba)
pdf.setFont('Courier-Bold',15)
print("")
ach=input("In which field or competion you have achived:")
pdf.drawString(10+tem,160+temp1,ach)
pdf.setFont('Courier',10)
ba=input("in that what is your achomplisment:")
pdf.drawString(10+tem,140+temp1,ba)

#skills
print("")
print("SKILLS")
print("**********")
pdf.setFont('Courier',20)
pdf.drawString(360,740,'SKILLS:')
pdf.setFont('Courier-Bold',15)
pdf.drawString(360,720,'TECHNICAL SKILLS:')
tcsk=input("what are the technical skills you have:")
pdf.setFont('Courier',10)
pdf.drawString(360,700,tcsk)

pdf.setFont('Courier-Bold',15)
pdf.drawString(360,680,'SOFT SKILLS:')
tcsk=input("what are the soft skills you have:")
pdf.setFont('Courier',10)
pdf.drawString(360,665,tcsk)

temp2=20
#work experience
print("")
print("WORK EXPERIEBCE AND INTERNSHIPS")
print("*******************************")

pdf.setFont('Courier',20)
pdf.drawString(360,605+temp2,'WORK EXPERIENCE:')
pdf.setFont('Courier-Bold',15)
print("")
print("#company1")
cn=input("Enter the company name :")
cn=cn.upper()
pdf.drawString(360,585+temp2,cn)
wp=input("what period of time you worked there (ex:2017-2018):")
wl=input("where it is located (ex:chennai,india):")
workplace=wp+" | "+wl
pdf.setFont('Courier',10)
pdf.drawString(360,570+temp2,workplace)
som=input("whats your experience in that company:")
som="  >"+som
pdf.drawString(360,555+temp2,som)
som=input("whats your major takeaway from that company:")
som="  >"+som
pdf.drawString(360,540+temp2,som)

print(" ")
print("#company2")
pdf.setFont('Courier-Bold',15)
cn=input("Enter the company name :")
cn=cn.upper()
pdf.drawString(360,520+temp2,cn)
pdf.setFont('Courier',10)
wp=input("what period of time you worked there (ex:2017-2018):")
wl=input("where it is located (ex:chennai,india):")
workplace=wp+" | "+wl
pdf.drawString(360,505+temp2,workplace)
som=input("whats your experience in that company:")
som="  >"+som
pdf.drawString(360,490+temp2,som)
som=input("whats your major takeaway from that company:")
som="  >"+som
pdf.drawString(360,480+temp2,som)

print(" ")
print("#company3")
pdf.setFont('Courier-Bold',15)
cn=input("Enter the company name :")
cn=cn.upper()
pdf.drawString(360,460+temp2,cn)
pdf.setFont('Courier',10)
wp=input("what period of time you worked there (ex:2017-2018):")
wl=input("where it is located (ex:chennai,india):")
workplace=wp+" | "+wl
pdf.drawString(360,440+temp2,workplace)
som=input("whats your experience in that company:")
som="  >"+som
pdf.drawString(360,425+temp2,som)
som=input("whats your major takeaway from that company:")
som="  >"+som
pdf.drawString(360,415+temp2,som)

print("")
print("Links")
print("******")

#links
pdf.setFont('Courier',20)
pdf.drawString(360,370+temp2,'LINKS:')
pdf.setFont('Courier',10)
lin=input("Enter your linked account link:")
pdf.drawString(360,350+temp2,lin)
lin=input("Enter your facebook account link:")
pdf.drawString(360,335+temp2,lin)
lin=input("Enter your twitter account link:")
pdf.drawString(360,320+temp2,lin)
lin=input("Enter your hackerrank account link:")
pdf.drawString(360,305+temp2,lin)
lin=input("Enter your stackoverflow account link:")
pdf.drawString(360,290+temp2,lin)



pdf.save()
