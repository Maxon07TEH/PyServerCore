#на библиотеке pySocket, настройки в консоли, сервак
import socket

#сеттинг#
maxdatavolume = input('pacSize?- ')
localhostip = ("'" + input('ip?- ') + "'")
localhostport = input('port?- ')
msgencode = "utf-8"
defmsg = "сервер работает, комп горяч"
LOGfile_patch: str = ("'" + input("logPatch?-") + "'")

if maxdatavolume == "def" or "default":
    maxdatavolume = 1024
if localhostip == "def" or "default":
    localhostip = "127.0.0.1"
if localhostport == "def" or "default":
    localhostport = 2000
if LOGfile_patch == "def" or "default":
    LOGfile_patch = "connectLog.txt"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((localhostip, localhostport))

server.listen(32)

def WriteConLOG():
    LOGfile = open(LOGfile_patch, 'r+')
    LOGfile.write(data)
    LOGfile.close()

while True:
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    user, adres = server.accept()
    data = user.recv(maxdatavolume)
    WriteConLOG()
    print(data)
    user.send(HDRS.encode(msgencode) + defmsg.encode(msgencode))

    user.send(input().encode(msgencode))
