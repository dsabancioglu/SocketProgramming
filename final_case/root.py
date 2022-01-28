#pylint: skip-file
from logging import root
from tkinter import *
from client import Client
from server import Server

class Root:
    def __init__(self):
        self.rootObject = root()

        self.root = Tk()
        self.root.title("Client Server Communication")
        self.root.geometry('900x500+500+250')
        



