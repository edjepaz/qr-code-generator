# QR Code Generator

A versatile command-line tool for generating various types of QR codes, available as a standalone Windows executable and Python script.

## Features

- 🖥️ **Interactive Menu**: User-friendly wizard for generating complex QR data.
- 📶 **Wi-Fi Config**: Create scannable Wi-Fi codes with SSID, password, and encryption.
- 📇 **vCard Contacts**: Generate contact cards for quick address book import.
- 📧 **Communication**: Pre-fill Email and SMS messages.
- 📍 **Geo Location**: Encode latitude and longitude for map locations.
- 📱 **Terminal View**: Display QR codes directly in your console using Unicode.
- 💾 **File Export**: Save QR codes as high-quality PNG images.

## Installation

### Option 1: Via Winget (Windows Package Manager)

Once approved, simply run:

```powershell
winget install qrcode-gen
```

### Option 2: Standalone Executable

Download the latest `qr-code-generator.exe` from the [Releases page](https://github.com/edjepaz/qr-code-generator/releases). No Python installation required.

### Option 3: Python Source

1. Clone the repository:
   ```bash
   git clone https://github.com/edjepaz/qr-code-generator.git
   cd qr-code-generator
   ```

2. Install dependencies:
   ```bash
   pip install qrcode[pil]
   ```

## Usage

Simply launch the application to see the interactive menu:

```bash
# If using Python script
python qr-code-generator.py

# If using executable
./qr-code-generator.exe
```

### Menu Options

1. **Text / URL**: Standard text or website link.
2. **Wi-Fi Network**: Enter SSID, Password, Encryption (WPA/WEP), and Hidden status.
3. **Contact (vCard)**: Enter Name, Phone, Email, and Organization.
4. **Email**: Enter Recipient, Subject, and Body.
5. **SMS**: Enter Phone Number and Message.
6. **Geo Location**: Enter Latitude and Longitude.

## Example

```text
Select QR Code Type:
1. Text / URL
2. Wi-Fi Network
3. Contact (vCard)
4. Email
5. SMS
6. Geo Location
Enter choice (1-6): 2

Enter SSID (Network Name): MyHomeWiFi
Enter Password: **********
Enter Encryption Type (WPA/WEP/nopass) [Default: WPA]: WPA
Is the network hidden? (true/false) [Default: false]: false

Displaying QR code in terminal:
█████████████████████████████████████
██ ▄▄▄▄▄ █ ... (QR code appears here)
...

Save to file? (y/n): y
```

## Requirements (Source only)

- Python 3.6+
- `qrcode` library with `pillow` support

## License

MIT License - See [LICENSE](LICENSE) for details.
