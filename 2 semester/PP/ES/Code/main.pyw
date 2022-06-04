#! /usr/bin/python3

import sys

from PySide2 import QtWidgets

from modules.ui.ui_main import Ui_main_window

from modules.configurations import set_locale
from modules.configurations import set_text


class MainWindow(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self) -> None:
        super().__init__()

        self.setupUi(self)

        set_locale.setup()

        set_text.setup(self)

        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

