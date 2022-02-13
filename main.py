import qrcode

qrinput = input("Enter text or url you want to make qr code of: ")

img = qrcode.make(qrinput)
img.save("NewQR.jpg")
