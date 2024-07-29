import csv
import os
from datetime import datetime

current_directory = os.getcwd() + "/bot/inc/data.csv"

if not os.path.exists(current_directory):
    with open(current_directory, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\r")
        writer.writerow(["id", "name", "job", "user_id", "username", "status", "timestamp"])

def get_next_id():
    with open(current_directory, "r", encoding="utf8") as openfile:
        file = csv.DictReader(openfile, delimiter=",")
        ids = [int(row["id"]) for row in file]
        return max(ids) + 1 if ids else 1

def record(name, job, user_id, username):
    if not user_exists(user_id):
        with open(current_directory, "a+", encoding="utf8", newline='') as outfile:
            file = csv.writer(outfile, delimiter=",", lineterminator="\r")
            status = "Обработка"
            timestamp = datetime.now().isoformat()
            new_id = get_next_id()
            file.writerow([new_id, name, job, user_id, username, status, timestamp])
        return print("Done!")
    else:
        with open(current_directory, "r", encoding="utf8") as infile:
            data = list(csv.DictReader(infile, delimiter=","))
        
        with open(current_directory, "w", encoding="utf8", newline='') as outfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=",", lineterminator="\r")
            writer.writeheader()
            for row in data:
                if row["user_id"] == str(user_id):
                    row["name"] = name
                    row["job"] = job
                    row["username"] = username
                    row["status"] = "Обработка"
                    row["timestamp"] = datetime.now().isoformat()
                writer.writerow(row)
        return print("User data updated!")

def get_unit_record(id):
    with open(current_directory, "r", encoding="utf8") as openfile:
        file = csv.DictReader(openfile, delimiter=",")
        for row in file:
            if row["id"] == str(id):
                request = f'Заявка № {row["id"]}\nФИО: {row["name"]}\nДолжность: {row["job"]}\nUser ID: {row["user_id"]}\nСтатус заявки: {row["status"]}'
                return row["user_id"], request
    return 'Вы указали несуществующую запись', 'Проверьте № заявки'

def get_list_record():
    data = []
    with open(current_directory, "r", encoding="utf8") as openfile:
        file = csv.DictReader(openfile, delimiter=",")
        for row in file:
            data.append(f'_________________________\nЗаявка № {row["id"]}\nФИО: {row["name"]}\nДолжность: {row["job"]}\nСтатус заявки: {row["status"]}')
    return data

def user_exists(user_id):
    with open(current_directory, "r", encoding="utf8") as openfile:
        file = csv.DictReader(openfile, delimiter=",")
        for row in file:
            if row["user_id"] == str(user_id):
                return True
    return False

def get_user_status(user_id):
    with open(current_directory, "r", encoding="utf8") as openfile:
        file = csv.DictReader(openfile, delimiter=",")
        for row in file:
            if row["user_id"] == str(user_id):
                return row["status"]
    return None

def get_last_request_time(user_id):
    with open(current_directory, "r", encoding="utf8") as openfile:
        file = csv.DictReader(openfile, delimiter=",")
        for row in file:
            if row["user_id"] == str(user_id):
                return datetime.fromisoformat(row["timestamp"])
    return None

def getpagerequests():
    records = []
    for i in range(0, len(get_list_record()), 10):
        records.append(get_list_record()[i:i+10])
    return records[::-1]

def getnotification(user_id):
    with open(current_directory, "r", encoding="utf8") as openfile:
        file = csv.DictReader(openfile, delimiter=",")
        data = []
        for row in file:
            if row["user_id"] == str(user_id) and row["status"] == "Обработка":
                data.append(f'Заявка № {row["id"]}\nФИО: {row["name"]}\nДолжность: {row["job"]}')
        return data[-1] if data else "Нет данных по заявке"

def setrefusal(user_id):
    with open(current_directory, "r", encoding="utf-8") as openfile:
        file = csv.DictReader(openfile, delimiter=",")
        data = [row for row in file]

    with open(current_directory, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        writer.writeheader()
        for d in data:
            if d["user_id"] == str(user_id) and d["status"] == "Обработка":
                d["status"] = "Отклонено"
            writer.writerow(d)
    return print('ref')

def setapprove(user_id):
    with open(current_directory, "r", encoding="utf-8") as openfile:
        file = csv.DictReader(openfile, delimiter=",")
        data = [row for row in file]

    with open(current_directory, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        writer.writeheader()
        for d in data:
            if d["user_id"] == str(user_id) and d["status"] == "Обработка":
                d["status"] = "Одобрено"
            writer.writerow(d)
    return print('app')
