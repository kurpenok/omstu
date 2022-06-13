def save(self) -> None:
    self.surname = self.line_edit_surname.text()
    self.name = self.line_edit_name.text()
    self.patronymic = self.line_edit_patronymic.text()

    self.label_save_status.setText("Успешно сохранено")

    self.line_edit_surname.setEnabled(False)
    self.line_edit_name.setEnabled(False)
    self.line_edit_patronymic.setEnabled(False)

    self.text_edit_question.setText(self.questions[0])

    self.push_button_yes.setEnabled(True)
    self.push_button_rather_yes.setEnabled(True)
    self.push_button_ignorance.setEnabled(True)
    self.push_button_rather_no.setEnabled(True)
    self.push_button_no.setEnabled(True)

