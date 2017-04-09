#!/usr/bin/python3
"""
.____ ___  _ _      _  __
/ ___\\  \/// \  /|/ |/ /
|    \ \  / | |\ |||   /
\___ | / /  | | \|||   \
\____//_/   \_/  \|\_|\_\

"""
import avalon_framework as avalon
import os
import socket
import hashlib

os.listdir('/')  # Delete Later
RHOST = 'narexium.com'
RPORT = 4090
VERSION = '0.1 beta'
PROJECTDIR = '/home/k4yt3x/Projects/Python/Entr0'


def sendFile(conn, filename, orgfname, last):
    with open(filename, 'r') as target:
        sendBuffer = orgfname + '\n'
        try:
            for line in target:
                sendBuffer += line
        except UnicodeDecodeError:
            print(orgfname)
        if last:
            sendBuffer += '\nLAST'
        conn.send(sendBuffer.encode('utf-8'))


def syncDir():
    sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    avalon.info('Trying to connect to ' + RHOST + 'on port ' + str(RPORT))
    sock0.connect((RHOST, RPORT))
    directory = os.listdir(PROJECTDIR)
    for files in directory:
        print(files)
        filename = files
        size = len(filename)
        size = bin(size)[2:].zfill(16)  # encode filename size as 16 bit binary
        sock0.send(size.encode('utf-8'))
        sock0.send(filename.encode('utf-8'))

        filename = os.path.join(PROJECTDIR, filename)
        filesize = os.path.getsize(filename)
        filesize = bin(filesize)[2:].zfill(32)  # encode filesize as 32 bit binary
        sock0.send(filesize.encode('utf-8'))

        file_to_send = open(filename, 'rb')

        sendBuffer = file_to_send.read()
        sock0.sendall(sendBuffer)
        file_to_send.close()
        print('File Sent')

    sock0.close()


def printIcon():
    print(' ____ ___  _ _      _  __')
    print('/ ___\\\\  \\/// \\  /|/ |/ /')
    print('|    \\ \\  / | |\\ |||   /')
    print('\\___ | / /  | | \\|||   \\')
    print('\\____//_/   \\_/  \\|\\_|\\_\\')
    print('\nWelcome Using Synk ' + VERSION)


def synk():
    printIcon()
    input('Press Enter When Ready...')
    syncDir()


def sha256sum(target):
    sha256 = hashlib.sha256()
    with open(target, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


synk()
