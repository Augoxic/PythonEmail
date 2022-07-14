import pickle


def lookup(emails):
    name = input("Enter a name: ")
    print(emails.get(name, 'That specified name was not found'))


def addNew(emails):
    name = input("Enter a name: ")
    email = input("Enter an email: ")

    if name not in emails:
        emails[name] = email
        print("Name and address have been added")

    else:
        print("That entry doesnt exist")


def change(emails):
    name = input("Enter name: ")

    if name not in emails:
        print("That name doesnt exist")

    else:
        newAddress = input("Enter new adddress: ")
        emails[name] = newAddress
        print("Information updated")


def delete(emails):
    name = input("Enter name: ")
    if name in emails:
        del emails[name]
        print("Information deleted")
    else:
        print("That name was not found")


try:
    emailFile = open("emails.txt", "rb")  # read and write
    emails = pickle.load(emailFile)
    print("\nEmail Dictionary: ")
    for name, email in emails.items():
        print(f"{name}: {email}")
    emailFile.close()

except FileNotFoundError:
    emails = {}
choice = ""

while choice != "5":
    print("Menu\n------------------------------")
    print("1. Look up an email address")
    print("2. Add a new name and email")
    print("3. Change existing email address")
    print("4. Delete a name and email")
    print("5. Quit Program \n")

    choice = input("Enter your choice: ")
    if choice == "1":
        lookup(emails)

    elif choice == "2":
        addNew(emails)

    elif choice == "3":
        change(emails)

    elif choice == "4":
        delete(emails)

    else:
        file = open("emails.txt", 'wb')
        pickle.dump(emails, file)
        print("Information saved")
        file.close
