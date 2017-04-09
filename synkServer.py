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


def sha256sum(target):
    sha256 = hashlib.sha256()
    with open(target, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def writeFile(target, content, last):
    cont = content.split('\n')
    cont.pop(0)
    if last:
        cont.pop(-1)
    with open(target, 'w') as t:
        for line in cont:
            t.write(line + '\n')
    t.close()


def recvData(conn):
    received = ""
    while True:
        data = conn.recv(4096)
        received += data.decode('utf-8')
        if len(data) < 4096:
            break
    return received


def syncServer():
    global sock0
    sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock0.bind((LHOST, LPORT))
    sock0.listen(10)

    while True:
        conn, (rip, rport) = sock0.accept()


while True:
    try:
        syncServer()
    except Exception as er:
        with open(LOG, 'a+') as log:
            log.write(str(er))
        log.close()
