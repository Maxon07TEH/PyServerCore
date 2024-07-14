#на библиотеке pySocket, настройки в консоли, сервак
import socket
#import string

#сеттинг#
maxdatavolume = input('pacSize?- ')
localhostip = ("'" + input('ip?- ') + "'")
localhostport = input('port?- ')
msgencode = 'utf-8'
defmsg = "сервер работает, комп горяч"
LOGfile_patch: str = ("'" + input("logPatch?- ") + "'")

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
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    response = ''
    try:
        with open('htmlview'+path, 'rb') as file:
            response = file.read()
            return HDRS.encode(msgencode) + response
    except FileNotFoundError:
<<<<<<< Updated upstream
        return (HDRS_404 + 'no page').encode(msgencode)
=======
        print(f"File not found: htmlview{path}")
        return HDRS_404.encode('utf-8') + b"<h1>404 Error: Page not found, idi v sraku</h1>"
>>>>>>> Stashed changes

if __name__ == "__main__":
    StartServer()