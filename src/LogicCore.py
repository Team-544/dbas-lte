from time import sleep

import pyodbc

from src.DB import DatabaseManipulate


class LogicCore:
    def __init__(self, ui):
        self.ui = ui
        try:
            self.db = DatabaseManipulate()
        except pyodbc.InterfaceError:
            self.ui.showStatus("Failed to connect to database system.")


    def signIn(self, username, password):
        try:
            self.db.signIn(username, password)
            return True
        except pyodbc.InterfaceError :
            self.ui.showStatus("Wrong user name or password.")
            return False

    def logOut(self):
        self.db.user_cnxn.close()
        self.db.user_cnxn = None

    def register(self, username, password):
        try:
            self.db.register(username, password)
            self.ui.showStatus("Your account is available now, please sign in.")
        except pyodbc.ProgrammingError:
            self.ui.showStatus("Your username is illegal, please try another one.")
