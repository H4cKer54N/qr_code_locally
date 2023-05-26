import qrcode
from PIL import Image
from getpass import getpass

def parse_color(color_string):
    """Convierte un string 'r,g,b' en una tupla de RGB (r, g, b)."""
    return tuple(int(x) for x in color_string.split(','))

print("Bienvenido al generador de códigos QR")
print("Por favor selecciona el tipo de QR que deseas generar:")
print("1. Tarjeta personal")
print("2. Sitio Web")
print("3. Correo Electrónico")
print("4. SMS")
print("5. Texto")
print("6. WiFi")

qr_type = input()

if qr_type == '1':
    print("Has seleccionado vCard. Por favor ingresa los siguientes datos:")
    n = input("Nombre (opcional): ")
    fn = input("Nombre Completo (opcional): ")
    url = input("URL (opcional): ")
    email = input("Correo electrónico (opcional): ")
    tel = input("Número de teléfono (opcional): ")
    adr = input("Dirección (opcional): ")
    city = input("Ciudad (opcional): ")
    prov = input("Provincia (opcional): ")
    pais = input("Pais (opcional): ")
    cap = input("Codigo Postal (opcional): ")
    data = f'''BEGIN:VCARD
    VERSION:3.0
    N:{n}
    FN:{fn}
    URL:{url}
    EMAIL;TYPE=lavoro:{email}
    TEL;TYPE=lavoro:{tel}
    ADR;TYPE=lavoro:{adr}
    ADR;TYPE=lavoro:;;{adr};{city};{prov};{cap};{pais}
    END:VCARD'''

elif qr_type == '2':
    print("Has seleccionado Sitio Web. Por favor ingresa la URL:")
    data = input()

elif qr_type == '3':
    print("Has seleccionado Correo Electrónico. Por favor ingresa el correo electrónico:")
    data = input()

elif qr_type == '4':
    print("Has seleccionado SMS. Por favor ingresa el número de teléfono y el mensaje:")
    data = f'SMS:{input("Número de teléfono: ")}:{input("Mensaje: ")}'

elif qr_type == '5':
    print("Has seleccionado Texto. Por favor ingresa el texto:")
    data = input()

elif qr_type == '6':
    print("Has seleccionado WiFi. Por favor ingresa el SSID, el tipo de seguridad y la contraseña:")
    data = f'WIFI:T:{input("Tipo de seguridad (normalmente WPA/WPA2): ")};S:{input("SSID (Nombre de red): ")};P:{getpass("Contraseña: ")};;'

else:
    print("Opción no válida.")
    exit(1)

output_file = input("Por favor, ingresa la ruta donde deseas guardar el código QR generado (dejar en blanco si quieres que sea la misma carpeta donde se ejecuta este programa): ")
image_logo = input("Por favor, ingresa la ruta al archivo de la imagen del logo (deja en blanco si no deseas un logo): ")
background_color = parse_color(input("Color de fondo del QR, en formato 'r,g,b' (deja en blanco para blanco): ") or '255,255,255')
foreground_color = parse_color(input("Color del frente del QR, en formato 'r,g,b' (deja en blanco para negro): ") or '0,0,0')

QRcode = qrcode.QRCode(border=2)
QRcode.add_data(data)
QRcode.make()

if image_logo:
    logo = Image.open(image_logo)
    hsize = int((float(logo.size[1])*float(100/float(logo.size[0]))))
    logo = logo.resize((200, 200), Image.ANTIALIAS)
    new_image = Image.new("RGBA", logo.size, (35,45,71))
    new_image.paste(logo, (0, 0), logo)
    logo = new_image 

QRimg = QRcode.make_image(fill_color=foreground_color, back_color=background_color).convert('RGB')

if image_logo:
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

QRimg.save(output_file or 'image3.png')

print("¡Código QR generado exitosamente!")
