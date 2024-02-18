from PySide2 import QtWidgets

from modules.decision import save_to_docx
from modules.decision import save_to_xlsx


def clear(self) -> None:
    if self.answers in [[0, 4, 2], [1, 4, 2]]:
        self.answer = "Искусственный интеллект с ограничением по памяти"
    elif self.answers in [[4, 2, 2], [3, 2, 2], [3, 2, 1], [3, 1, 2], [3, 1, 1]]:
        self.answer = "Реагирующий ИИ"
    elif self.answers in [[0, 0, 4], [0, 1, 4], [1, 0, 4], [0, 0, 3], [0, 1, 3], [1, 0, 3]]:
        self.answer = "ИИ с теоретическими основами разума"
    elif self.answers in[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]:
        self.answer = "ИИ, обладающий самосознанием"
    else:
        self.answer = "Ваши цели за пределами моего понимания"

    self.line_edit_surname.setText("")
    self.line_edit_name.setText("")
    self.line_edit_patronymic.setText("")
    
    self.label_save_status.setText("")

    self.push_button_save_user_info.setEnabled(True)

    self.text_edit_question.setText("")
    self.noq = 0
    self.answers = []

    self.push_button_yes.setEnabled(False)
    self.push_button_rather_yes.setEnabled(False)
    self.push_button_ignorance.setEnabled(False)
    self.push_button_rather_no.setEnabled(False)
    self.push_button_no.setEnabled(False)

    self.line_edit_surname.setEnabled(True)
    self.line_edit_name.setEnabled(True)
    self.line_edit_patronymic.setEnabled(True)

    save_to_docx.save(self)
    save_to_xlsx.save(self)

    QtWidgets.QMessageBox.information(self, "Успешно", "Данные успешно сохранены")

