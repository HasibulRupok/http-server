from socket import *


def generateResponse(request):
    fileName = request.split()[1]
    # print(fileName)

    if fileName == '/':
        fileName = '/index.html'

    try:
        fileUrl = 'files' + fileName
        fileOpen = open(fileUrl)
        content = fileOpen.read()
        fileOpen.close()
        generatedResponse = 'HTTP/1.0 200 OK\n\n' + content
    except:
        generatedResponse = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    return generatedResponse


host = '127.0.0.1'
port = 8080

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((host, port))
serverSocket.listen(1)

while True:
    clientSocket, clientAddress = serverSocket.accept()
    webRequest = clientSocket.recv(2000).decode()
    # print(webRequest)

    htmlResponse = generateResponse(webRequest)
    htmlResponse = htmlResponse.encode()
    clientSocket.sendall(htmlResponse)
    clientSocket.close()
