import qrcode as qr

while True:
    webpage = input("Enter the address you want to turn into a QR Code: ")
    if "https" in webpage:
        break
    elif "http" in webpage:
        prompt = input("This might not be a safe website. Are you sure you want to proceed? (yes/no): ")
        prompt = prompt.lower()
        if prompt == "yes":
            break
        elif prompt == "no":
            continue
    else:
        print("This is not a valid webpage, please try again.")
        continue

while True:
    Qr_color = input("What color do you want the QR Code to be? ")
    Qr_color = Qr_color.lower()
    break

while True:
    background = input("What background color do you want the QR Code to have? ")
    background = background.lower()
    break

while True:
    folder = input("Specify the folder you want to save the QR Code in (do not add backslash to the end): ")
    folder = folder.lower()
    break

while True:
    name = input("Name your file! ")
    name = name.lower()
    break

qr_code = qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr_code.add_data(webpage)
qr_code.make(fit=True)
img = qr_code.make_image(fill_color=Qr_color, back_color=background)
img.save(f"{folder}\\{name}.png")

print("QR Code has been saved to your folder!")



