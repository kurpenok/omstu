import csv


def reader(path: str, encoding="utf-8") -> list:
    data = []

    with open(path, encoding=encoding) as file:
        buffer = csv.reader(file)
        for row in buffer:
            data.append(row)

    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = data[i][j].strip()

    return data


def generate_emails(names: list) -> list:
    emails = []

    for name in names:
        email = f"{name[0]}.{name[1]}@company.io"
        letter = 1
        
        while email in email:
            email = f"{name[0]}.{name[1][:letter]}@company.io"
            letter += 1

        emails.append(email)

    return emails


def writer(data: list, path: str, encoding="utf-8") -> None:
    old_data = []

    with open(path, "r", encoding=encoding) as file:
        buffer = csv.reader(file)
        for row in buffer:
            old_data.append(row)

    for i in range(len(old_data)):
        for j in range(len(old_data[i])):
            old_data[i][j] = old_data[i][j].strip()

    if len(data) != len(old_data) - 1:
        return
    
    new_data = []
    for i in range(len(old_data)):
        new_data.append(old_data[i])
        new_data[i][0] = data[i]

    with open(path, "w", encoding=encoding) as file:
        buffer = csv.writer(file)
        buffer.writerows(new_data)      


if __name__ == "__main__":
    data = reader("task_file.txt")
    
    names = []
    for i in range(len(data)):
        names.append([data[1], data[2]])

    emails = generate_emails(names)

    writer(emails, "task_file.txt")

