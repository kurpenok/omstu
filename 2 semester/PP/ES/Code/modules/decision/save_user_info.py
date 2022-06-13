from PySide2 import QtWidgets


def save(self) -> None:
    self.surname = self.line_edit_surname.text()
    self.name = self.line_edit_name.text()
    self.patronymic = self.line_edit_patronymic.text()

    if self.surname and self.name and self.patronymic:
        self.label_save_status.setText("Успешно сохранено")

        self.line_edit_surname.setEnabled(False)
        self.line_edit_name.setEnabled(False)
        self.line_edit_patronymic.setEnabled(False)

        self.push_button_save_user_info.setEnabled(False)

        self.text_edit_question.setText(self.questions[0])

        self.push_button_yes.setEnabled(True)
        self.push_button_rather_yes.setEnabled(True)
        self.push_button_ignorance.setEnabled(True)
        self.push_button_rather_no.setEnabled(True)
        self.push_button_no.setEnabled(True)
    else:
        QtWidgets.QMessageBox.critical(self, "Ошибка", "Данные введены некорректно!")

