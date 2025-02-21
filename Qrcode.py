
import qrcode

# Data to be encoded in the QR code
data = "https://www.adivasi.org"

# Creating an instance of QRCode
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is the smallest, 40 is the largest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # L: 7% error correction
    box_size=10,  # Size of each box in pixels
    border=4  # Border thickness in boxes
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")

# Show the QR code
img.show()