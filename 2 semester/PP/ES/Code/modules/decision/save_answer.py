from modules.decision import clear_data


def save(self, number: int, q: int) -> None:
    self.answers.append(number)
    
    if q != len(self.questions):
        self.text_edit_question.setText(self.questions[q])
        self.q = q
    else:
        clear_data.clear(self)

