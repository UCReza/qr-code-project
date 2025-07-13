import qrcode

#URL to encode
url = "https://github.com/UCReza"

#QR Code instance 
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

#add the data to the QR code
qr.add_data(url)
qr.make(fit=True)

#creating image
img = qr.make_image(fill_color="black",
                    back_color="white")

#save the image
img.save("my_qr_code.png")

print("QR Code generated and saved as my_qr_code.png")