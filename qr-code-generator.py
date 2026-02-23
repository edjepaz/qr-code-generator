import qrcode
import sys

def get_wifi_data():
    ssid = input("Enter SSID (Network Name): ")
    password = input("Enter Password: ")
    auth_type = input("Enter Encryption Type (WPA/WEP/nopass) [Default: WPA]: ").upper() or "WPA"
    hidden = input("Is the network hidden? (true/false) [Default: false]: ").lower() or "false"
    return f"WIFI:T:{auth_type};S:{ssid};P:{password};H:{hidden};;"

def get_contact_data():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    org = input("Enter Organization: ")
    return f"BEGIN:VCARD\nVERSION:3.0\nN:{name}\nTEL:{phone}\nEMAIL:{email}\nORG:{org}\nEND:VCARD"

def get_email_data():
    email = input("Enter Recipient Email: ")
    subject = input("Enter Subject: ")
    body = input("Enter Body: ")
    return f"mailto:{email}?subject={subject}&body={body}"

def get_sms_data():
    phone = input("Enter Phone Number: ")
    message = input("Enter Message: ")
    return f"smsto:{phone}:{message}"

def get_geo_data():
    latitude = input("Enter Latitude: ")
    longitude = input("Enter Longitude: ")
    return f"geo:{latitude},{longitude}"

def display_menu():
    print("\nSelect QR Code Type:")
    print("1. Text / URL")
    print("2. Wi-Fi Network")
    print("3. Contact (vCard)")
    print("4. Email")
    print("5. SMS")
    print("6. Geo Location")
    
    choice = input("Enter choice (1-6): ").strip()
    return choice

def display_qr_terminal(data):
    """
    Display a QR code in the terminal using Unicode blocks.

    Args:
        data (str): The data to encode in the QR code
    """
    qr = qrcode.QRCode(border=2)
    qr.add_data(data)
    try:
        qr.make(fit=True)
        qr.print_ascii(invert=True)
    except Exception as e:
        print(f"Error displaying QR code in terminal: {e}")

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
    choice = display_menu()
    
    data = ""
    if choice == '1':
        data = input("Enter text or URL: ")
    elif choice == '2':
        data = get_wifi_data()
    elif choice == '3':
        data = get_contact_data()
    elif choice == '4':
        data = get_email_data()
    elif choice == '5':
        data = get_sms_data()
    elif choice == '6':
        data = get_geo_data()
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

    print("\nDisplaying QR code in terminal:")
    display_qr_terminal(data)

    save = input("\nSave to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter output filename (press Enter for 'qrcode.png'): ").strip()
        if not filename:
            filename = "qrcode.png"
        generate_qr_code(data, filename)