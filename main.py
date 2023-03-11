import qrcode
with open("site.csv") as file:
    for i in file:
        data = i.strip("\n")
        new_data = data.split(",")
        img = qrcode.make(f"{new_data[1]}")
        img.save(f"{new_data[0]}.jpg")
print("all QR code create completed")
