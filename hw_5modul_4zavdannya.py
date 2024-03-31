def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid command."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    name = args
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

@input_error
def show_all(args, contacts):
    if contacts:
        return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts available."

# Додайте обробник помилки для інших команд, які можуть виникнути

# Приклад використання
contacts = {}
while True:
    command = input("Enter a command: ").strip().split()
    if command:
        action = command[0]
        if action == "add":
            if len(command) != 3:
                print("Enter the argument for the command")
            else:
                result = add_contact(command[1:], contacts)
                print(result)
        elif action == "change":
            if len(command) != 3:
                print("Enter the argument for the command")
            else:
                result = change_contact(command[1:], contacts)
                print(result)
        elif action == "phone":
            if len(command) != 2:
                print("Enter the argument for the command")
            else:
                result = show_phone(command[1], contacts)
                print(result)
        elif action == "all":
            if len(command) != 1:
                print("Enter the argument for the command")
            else:
                result = show_all(command[1:], contacts)
                print(result)
        else:
            print("Enter a valid command.")
