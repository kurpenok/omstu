from modules.decision import clear_data


def save(self, number: int, noq: int) -> None:
    self.answers.append(number)
    
    if noq != len(self.questions):
        self.text_edit_question.setText(self.questions[noq])
        self.noq = noq
    else:
        clear_data.clear(self)

