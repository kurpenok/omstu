import os

import pylightxl


def save(self) -> None:
    wb = os.getcwd()
    line = 1
    
    if os.path.exists(f"{wb}/Report.xlsx"):
        db = pylightxl.readxl("Report.xlsx")

        while True:
            output = db.ws(ws="Лист1").index(row=line, col=0)
            if not output:
                break
    else:
        db = pylightxl.Database()
        db.add_ws(ws="Лист1")

    db.ws(ws="Лист1").update_index(row=line, col=1, val=self.surname)
    db.ws(ws="Лист1").update_index(row=line, col=2, val=self.name)
    db.ws(ws="Лист1").update_index(row=line, col=3, val=self.patronymic)
    db.ws(ws="Лист1").update_index(row=line, col=4, val=self.answer)
    
    pylightxl.writexl(db=db, fn="Report.xlsx")

