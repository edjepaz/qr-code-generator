import qrcode

def display_qr_terminal(data):
    """
    Display a QR code in the terminal using Unicode blocks.
    
    Args:
        data (str): The data to encode in the QR code
    """
    qr = qrcode.QRCode(border=2)
    qr.add_data(data)
    qr.make(fit=True)
    qr.print_ascii(invert=True)

def generate_qr_code(data, filename="qrcode.png"):
    """
    Generate a QR code from the provided data and save it as an image.
    
    Args:
        data (str): The data to encode in the QR code
        filename (str): The output filename (default: qrcode.png)
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code generated successfully: {filename}")

if __name__ == "__main__":
    # Example usage
    data = input("Enter the data to encode in QR code: ")
    
    print("\nDisplaying QR code in terminal:")
    display_qr_terminal(data)
    
    save = input("\nSave to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter output filename (press Enter for 'qrcode.png'): ").strip()
        if not filename:
            filename = "qrcode.png"
        generate_qr_code(data, filename)
