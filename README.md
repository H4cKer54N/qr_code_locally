# QR Code Generator
### This QR Code Generator is a Python script that allows you to create various types of QR codes. The QR code types supported are: vCard, Website URL, Email, SMS, Text, and WiFi.

## Features

Create various types of QR codes
Customize the foreground and background color of the QR codes
Add a logo to the center of the QR codes
Interactive console dialog for easier QR code creation


## Dependencies
This script depends on the following Python packages:

qrcode
PIL (Pillow)
You can install these packages with pip:

~~~
pip install qrcode pillow
~~~

## Usage
Run the script in your terminal and follow the interactive prompts:
~~~
python qr_generator.py
~~~

You'll first be asked to select the type of QR code you wish to generate. Depending on the type you select, you'll be asked to enter the necessary data. For instance, if you select 'vCard', you'll be asked to enter the name, full name, URL, email, phone number, and address. If you select 'Website URL', you'll only need to enter the URL, and so on.

Once you've entered the data for the QR code, you'll be asked to specify the output file path, logo image path, and the foreground and background colors.

## Contributions
We welcome contributions to this project! If you find a bug or have a feature suggestion, please create a new branch with the name of the bug or feature. For example, if you found a bug related to the color rendering, you could create a new branch called bug/color-rendering. If you have a feature suggestion, such as adding support for more QR code types, you could create a new branch called feature/more-qr-types. Once you've made your changes, please submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
If you have any questions, feel free to reach out to snbq89@gmail.com thanks.

