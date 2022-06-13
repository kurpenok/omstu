#! /usr/bin/python3

import sys

from PySide2 import QtWidgets

from modules.ui.ui_main import Ui_main_window

from modules.configurations import set_text

from modules.decision import save_user_info
from modules.decision import save_answer


class MainWindow(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # set_text.setup(self)
        self.label_save_status.setText("")

        self.push_button_yes.setEnabled(False)
        self.push_button_rather_yes.setEnabled(False)
        self.push_button_ignorance.setEnabled(False)
        self.push_button_rather_no.setEnabled(False)
        self.push_button_no.setEnabled(False)

        self.push_button_save_user_info.clicked.connect(lambda: save_user_info.save(self))
        
        self.questions = [
            "Когда я закроюсь?",
            "Когда я получу стипу?",
            "Зачем нужен линал на практике?"
        ]
        self.q = 0

        self.answers = []
        self.answer = "На пересдачу"
        self.push_button_yes.clicked.connect(lambda: save_answer.save(self, 0, self.q + 1))
        self.push_button_rather_yes.clicked.connect(lambda: save_answer.save(self, 1, self.q + 1))
        self.push_button_ignorance.clicked.connect(lambda: save_answer.save(self, 2, self.q + 1))
        self.push_button_rather_no.clicked.connect(lambda: save_answer.save(self, 3, self.q + 1))
        self.push_button_no.clicked.connect(lambda: save_answer.save(self, 4, self.q + 1))

        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

