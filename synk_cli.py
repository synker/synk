#!/usr/bin/python3

import os, time, argparse, getpass, hashlib


CONFFILE = "~/.config/synk.conf"


def get_args():
    parser = argparse.ArgumentParser()
    parser.addArgument("-s", "--setup", help="Run the script in setup mode.")

    return parser.parse_args()


def setup():
    projectdir = input("Enter directory for project: ").strip()
    usernm = input("Enter username for project directory")          # synker
    proto, git_serv = input("Enter url to git project").split(':')  # https://github.com/synker/synk.git
    passwd = getpass.getpass()                                      # tosynkornottosynk

    try:
        os.system("git --git-dir=%s --work-tree=%s remote remove origin" % (projectdir + ".git", projectdir))
        os.system("git remote add origin " + proto + "//%s:%s@%s" % (usernm, passwd, git_serv))

        with open(CONFFILE, "w") as cf:
            cf.write(projectdir + "\n" + usernm + "\n" + proto + "\n" + git_serv + "\n" + hashlib.sha512(passwd))
    except Exception:
        print("An error occured. Please reenter your information.")
        os.quit()
        quit()


def upload_changes():
    os.system("git add -f . && git commit -am 'autocommit' && git push origin master")


def get_changes():
    os.system("git pull origin master --no-edit")


def main():
    args = get_args()
    if args.setup:
        setup()
        os.quit()
        quit()
    if not os.path.isfile("~/.config/synk.conf"):
        print("Please run `./synk_cli.py -s` first.")
            os.quit()
            break
    while True:
        try:
            upload_changes()
            get_changes()
            time.sleep(0.1)
        except KeyboardInterrupt:
            os.quit()
            break
        except Exception:
            print("An error occurred.")
            os.quit()
            break


if __name__ == "__main__":
    main()

