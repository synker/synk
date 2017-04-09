#!/usr/bin/python3

import socket, os, time, multiprocessing

proto = "https"
git_server = "github.com/synker/synk.git"
usernm = "synker"
passwd = "tosynkornottosynk"


def setup():
    os.system("git remote remove origin")
    os.system("git remote add origin " + proto + "://%s:%s@%s" % (usernm, passwd, git_server))


def upload_changes():
    os.system("git add -f . && git commit -am 'autocommit' && git push origin master")


def get_changes():
    os.system("git pull origin master")


setup()

while True:
    upload_changes()
    get_changes()
    time.sleep(0.1)


