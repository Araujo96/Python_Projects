import qrcode
import datetime


def qrcode_link(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    now = datetime.datetime.now()
    img.save("link_qrcode_{}.png".format(now.strftime("%Y-%m-%d_%H-%M-%S")))


def qrcode_music(music_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(music_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="rgb(153, 204, 50)", back_color="white")
    now = datetime.datetime.now()
    img.save("music_qrcode_{}.png".format(now.strftime("%Y-%m-%d_%H-%M-%S")))
    img.show()

choose = ""
while choose not in ["l", "a"]:
    choose = input("Deseja transformar um Link ou Áudio? Digite: l - Link, a - Áudio ").lower()

if choose == 'l':
    link = input('digite o Link para transformar em QRCODE: ')
    qrcode_link(link)
    print('qrcode Gerado com Sucesso!')
else:
    music_url = input("Digite o link da música do Spotify: ")
    qrcode_music(music_url)
    print('qrcode Gerado com Sucesso!')
