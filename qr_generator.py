import qrcode
from PIL import Image

def generate_qr(upi_id, name):
    upi_url = f"upi://pay?pa={upi_id}&pn={name}&cu=INR"

    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(upi_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    file_path = "upi_qr.png"
    img.save(file_path)

    return file_path