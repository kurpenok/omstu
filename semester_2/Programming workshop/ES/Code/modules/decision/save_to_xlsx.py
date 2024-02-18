import os

import pylightxl


def save(self) -> None:
    wb = os.getcwd()
    line = 1

    if not os.path.exists(f"{wb}/reports/"):
        os.mkdir(f"{wb}/reports/")
    
    if os.path.exists(f"{wb}/reports/Report.xlsx"):
        db = pylightxl.readxl("reports/Report.xlsx")

        while True:
            output = db.ws(ws="Лист1").index(row=line, col=1)
            if not output:
                break
            line += 1
    else:
        db = pylightxl.Database()
        db.add_ws(ws="Лист1")

    db.ws(ws="Лист1").update_index(row=line, col=1, val=self.surname)
    db.ws(ws="Лист1").update_index(row=line, col=2, val=self.name)
    db.ws(ws="Лист1").update_index(row=line, col=3, val=self.patronymic)
    db.ws(ws="Лист1").update_index(row=line, col=4, val=self.answer)
    
    pylightxl.writexl(db=db, fn="reports/Report.xlsx")

