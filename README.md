# QR Code Generator

A Python script to generate QR codes that can be displayed in the terminal or saved as image files.

## Features

- 📱 Display QR codes directly in the terminal using Unicode blocks
- 💾 Save QR codes as PNG image files
- 📶 Generate WiFi QR codes for easy network sharing
- 🎯 Simple and interactive command-line interface

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/qr-code-generator.git
cd qr-code-generator
```

2. Install required dependencies:
```bash
pip install qrcode[pil]
```

## Usage

Run the script:
```bash
python qr_code_generator.py
```

The script will:
1. Prompt you to enter data to encode (URL, text, WiFi credentials, etc.)
2. Display the QR code in your terminal
3. Ask if you want to save it to a file

### WiFi QR Code Format

To create a WiFi QR code that allows automatic connection, use this format:
```
WIFI:T:WPA;S:YourNetworkName;P:YourPassword;;
```

Where:
- `T` = Security type (WPA, WEP, or nopass)
- `S` = Network SSID (name)
- `P` = Password

### Example

```bash
Enter the data to encode in QR code: WIFI:T:WPA;S:MyHomeWiFi;P:mypassword123;;

Displaying QR code in terminal:
█████████████████████████████████████
██ ▄▄▄▄▄ █ ... (QR code appears here)
...

Save to file? (y/n): y
Enter output filename (press Enter for 'qrcode.png'): wifi_qrcode.png
QR code generated successfully: wifi_qrcode.png
```

## Use Cases

- **WiFi Sharing**: Generate QR codes for guests to connect to your WiFi
- **URL Sharing**: Create QR codes for websites and links
- **Contact Information**: Encode vCards for easy contact sharing
- **Event Information**: Share event details and registration links

## Requirements

- Python 3.6+
- qrcode library with PIL support

## License

MIT License - Feel free to use and modify as needed.

## Contributing

Pull requests are welcome! Feel free to submit issues for bugs or feature requests.
