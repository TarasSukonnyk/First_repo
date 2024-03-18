def add_contact(contacts, name, phone_number):
    if name in contacts:
        return "Contact already exists."
    else:
        contacts[name] = phone_number
        return "Contact added."

def change_contact(contacts, name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone_number}" for name, phone_number in contacts.items()])
    else:
        return "No contacts found."

def parse_input(input_str):
    parts = input_str.lower().split()
    command = parts[0]
    if command == "hello":
        return "How can I help you?"
    elif command == "add" and len(parts) == 3:
        return add_contact(contacts, parts[1], parts[2])
    elif command == "change" and len(parts) == 3:
        return change_contact(contacts, parts[1], parts[2])
    elif command == "phone" and len(parts) == 2:
        return show_phone(contacts, parts[1])
    elif command == "all":
        return show_all(contacts)
    elif command in ["exit", "close"]:
        return "Good bye!"
    else:
        return "Invalid command. Please try again."

def main():
    contacts = {}
    print("Welcome to the Console Assistant Bot!")
    print("Commands:")
    print("hello - Greet the bot")
    print("add [name] [phone_number] - Add a new contact")
    print("change [name] [new_phone_number] - Change the phone number of a contact")
    print("phone [name] - Show the phone number of a contact")
    print("all - Show all contacts")
    print("exit/close - Exit the program")

    running = True
    while running:
        user_input = input("Enter command: ")
        response = parse_input(user_input)
        print(response)
        if response == "Good bye!":
            running = False

if __name__ == "__main__":
    main()
