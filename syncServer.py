#!/usr/bin/python3
"""
.____ ___  _ _      _  __
/ ___\\  \/// \  /|/ |/ /
|    \ \  / | |\ |||   /
\___ | / /  | | \|||   \
\____//_/   \_/  \|\_|\_\

"""
import avalon_framework as avalon
import socket
import os
import multiprocessing
import hashlib

LHOST = "0.0.0.0"
LPORT = 4090
PROJECTDIR = '/var/projects'
LOG = '/var/log/sync.log'

ssss

def recvData(conn):
    received = ""
    while True:
        data = conn.recv(4096)
        received += data.decode('utf-8')
        if len(data) < 4096:
            break
    return received


def projectFolderOK():
    if not os.path.isdir() and not os.path.isfile(PROJECTDIR):
        os.system('mkdir ' + PROJECTDIR)
        return True
    elif os.path.isfile(PROJECTDIR):
        avalon.error('The Project Directory is a file!')
        avalon.error('Please check your file system!')
        return False
    else:
        return True


def syncClient(sockclient):
    while True:
        size = sockclient.recv(16).decode('utf-8')  # Note that you limit your filename length to 255 bytes.
        if not size:
            break
        size = int(size, 2)
        filename = sockclient.recv(size).decode('utf-8')
        filesize = sockclient.recv(32).decode('utf-8')
        filesize = int(filesize, 2)
        file_to_write = open(filename, 'wb')
        chunksize = 4096
        while filesize > 0:
            if filesize < chunksize:
                chunksize = filesize
            data = sockclient.recv(chunksize)
            file_to_write.write(data)
            filesize -= chunksize

        file_to_write.close()
        print('File received successfully')
    sock0.close()


def syncServer():
    global sock0
    sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock0.bind((LHOST, LPORT))
    sock0.listen(10)

    while True:
        conn, (rip, rport) = sock0.accept()
        multiprocessing.Process(target=syncClient, args=(conn,)).start()


while True:
    try:
        syncServer()
    except Exception as er:
        with open(LOG, 'a+') as log:
            log.write(str(er))
        log.close()
