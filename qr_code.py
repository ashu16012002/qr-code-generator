import qrcode as qr
img = qr.make("https://chatgpt.com/")
img.save("chatgpt.png")