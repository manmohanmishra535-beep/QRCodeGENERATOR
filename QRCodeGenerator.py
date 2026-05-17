import qrcode

# Data to encode
data = "https://www.youtube.com/watch?v=6_NrgoEkjnE"

# Generate QR code
img = qrcode.make(data)

# Save image
img.save("qrcode.png")

# Show image
img.show()