#на библиотеке pySocket, настройки в консоли, сервак
import socket
#import string

#сеттинг#
inipath = "setting.ini"
with open(inipath, "r+") as settingfile:
    text = ""

    text = settingfile.readlines()[0]
    maxdatavolume = text.split(" = ")[1]
    text = settingfile.readlines()[1]
    localhostip = text.split(" = ")[1]
    text = settingfile.readlines()[2]
    localhostport = text.split(" = ")[1]
    text = settingfile.readlines()[3]
    msgencode = text.split(" = ")[1]
    text = settingfile.readlines()[4]
    defmsg = text.split(" = ")[1]
    text = settingfile.readlines()[5]
    LOGfile_patch = text.split(" = ")[1]

if maxdatavolume == "def" or "default" or "":
    maxdatavolume = 2048
if localhostip == "def" or "default" or "'def'" or "'default'" or "":
    localhostip = "127.0.0.1"
if localhostport == "def" or "default" or "":
    localhostport = 2000
if LOGfile_patch == "def" or "default" or "'def'" or "'default'" or "":
    LOGfile_patch = "connectLog.txt"
#def WriteLOG(LOGcontent):
#    LOGfile = open(LOGfile_patch, 'r+')
#    LOGfile.write(LOGcontent)
#    LOGfile.close()

def StartServer():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((localhostip, localhostport))
        server.listen(4)
        print("Server started")
        while True:
            user, adres = server.accept()
            data = user.recv(maxdatavolume).decode(msgencode)
            print(data)
            user.send(load_page_from_get_request(data))
            user.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print("оффнулся")


def load_page_from_get_request(request_data):
    HDRS_200 = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'

    if not request_data:
        print("Empty request data")
        return HDRS_404.encode('utf-8') + b"<h1>404 Error: Page not found</h1>"

    request_parts = request_data.split(" ")
    if len(request_parts) < 2:
        print(f"Invalid request data: {request_data}")
        return HDRS_404.encode('utf-8') + b"<h1>404 Error: Page not found</h1>"

    path = request_parts[1]
    if path == '/':
        path = '/home.html'

    response = ""

    try:
        with open("htmlview" + path, "rb") as file:
            response = file.read()
        return HDRS_200.encode('utf-8') + response
    except FileNotFoundError:
        print(f"File not found: htmlview{path}")
        return HDRS_404.encode('utf-8') + b"<h1>404 Error: Page not found</h1>"


if __name__ == "__main__":
    StartServer()