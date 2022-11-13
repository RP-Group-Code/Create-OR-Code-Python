import pyqrcode
import png

f = open("data.txt", "r")
for x in f:
	link=x.strip()
	link=link.replace("http://www.","")
	link=link.replace("/","")	
	qr_code = pyqrcode.create(link)
	qr_code.png(link+".png", scale=5)
	print("Creating qrcode: ",link)
print("Finish")