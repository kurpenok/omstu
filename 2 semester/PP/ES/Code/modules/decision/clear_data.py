def clear(self) -> None:
    self.line_edit_surname.setText("")
    self.line_edit_name.setText("")
    self.line_edit_patronymic.setText("")
    
    self.label_save_status.setText("")

    self.push_button_save_user_info.setEnabled(True)

    self.text_edit_question.setText("")

    self.push_button_yes.setEnabled(False)
    self.push_button_rather_yes.setEnabled(False)
    self.push_button_ignorance.setEnabled(False)
    self.push_button_rather_no.setEnabled(False)
    self.push_button_no.setEnabled(False)

