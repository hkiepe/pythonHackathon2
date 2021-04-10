import json


def open_phonebook(filename):
    with open(filename, 'r') as file:
        data_json = json.load(file)
    return data_json


def update_phonebook(filename, phoneBook):
    with open(filename, "r+") as file:
        file.seek(0)
        file.truncate()
        json.dump(phoneBook, file)


def drop_adressline():
    print_adresslist()
    line_id = int(input("select the adress id you want to delete?")) - 1
    with open('phoneBook.json', 'r') as file:
        data_json = json.load(file)
        data_json["people"].pop(line_id)
    update_phonebook('phoneBook.json', data_json)


def print_menu():
    print("++++++++++++++ Menu ++++++++++++++")
    print("1 - Show Phonebook")
    print("2 - New Contact")
    print("3 - Delete Contact")
    print("4 - Quit")
    selected = input("What do you want to do?")
    return selected


def print_adresslist():
    data_json = open_phonebook('phoneBook.json')
    print("ID - Forename - Surname - Mail - Phone")
    for id in data_json['people']:
        print(str(id['id']) + ' - ' + id['forename'] + ' - ' + id['surname'] + ' - ' + id['mail'] + ' - ' + id['phone'])


def input_new_adress():
    data_json = open_phonebook('phoneBook.json')
    print("please add a new contact")
    if len(data_json['people']) == 0:
        new_id = 0
    else:
        new_id = len(data_json['people']) + 1
    forename = input("please add a forename")
    surname = input("please add a surname")
    mail = input("please add a mail")
    phone = input("please add a phone number")
    data_json["people"].append({"id": new_id, "forename": forename, "surname": surname, "mail": mail, "phone": phone})
    update_phonebook('phoneBook.json', data_json)
