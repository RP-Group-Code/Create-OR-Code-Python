import pyqrcode
import png
link = "https://covid19.go.id/id/"
qr_code = pyqrcode.create(link)
qr_code.png("covid19.png", scale=5)