import pickle
from collections import defaultdict, UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value): 
        self.value = value

    def __str__(self):
        return str(self.value) 
    
    def __repr__(self):
        return str(self.value) 
    

class Name(Field):
    def __init__(self, name=None):
        if name is None:
            raise ValueError
        super().__init__(name) 


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)  
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) == 10 and value.isdigit():
            self.__value = value
        else:
            raise ValueError('Invalid phone number')    


class Birthday(Field):
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            raise ValueError('Invalid date format. Should be ДД-ММ-РРРР')


class Record:
    def __init__(self, name): 
        self.name = Name(name)
        self.phones = list()

    def add_phone(self, phone): 
        for p in self.phones: 
            if p.value == phone: 
                return
        self.phones.append(Phone(phone))

    def remove_phone(self, phone): 
        for p in self.phones: 
            if p.value == phone: 
                self.phones.remove(p)
                return
        raise ValueError
    
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
        raise ValueError

    def find_phone(self, phone): 
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
    
    def __str__(self):
        return f'Record(Name: {self.name} Phones: {self.phones})'
    
    def __repr__(self):
        return f'Record(Name: {self.name} Phones: {self.phones})'
    

class AddressBook(UserDict): 
    def add_record(self, record: Record): 
        name = record.name.value
        self.data.update({name: record}) 

    def find(self, name):
        return self.data.get(name) 
    
    def delete(self, name):
        del self.data[name]

    def find_next_birthday(self, weekday):
        current_date = datetime.now().date()
        next_birthdays = []
        for record in self.data.values():
            if record.birthday.date.month < current_date.month or (record.birthday.date.month == current_date.month and record.birthday.date.day < current_date.day):
                next_birthday_year = current_date.year + 1
            else:
                next_birthday_year = current_date.year

            next_birthday = datetime(next_birthday_year, record.birthday.date.month, record.birthday.date.day).date()

            if next_birthday.weekday() == weekday:
                next_birthdays.append((record.name, next_birthday))

        return next_birthdays

    def get_upcoming_birthday(self, days=7):
        current_date = datetime.now().date()
        end_date = current_date + timedelta(days=days)
        upcoming_birthdays = []
        for record in self.data.values():
            birthday = record.birthday.date.replace(year=current_date.year)
            if current_date <= birthday <= end_date:
                upcoming_birthdays.append((record.name, birthday))

        return upcoming_birthdays
    
    def save_data(self, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load_data(cls, filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return cls()  # Return a new AddressBook if file not found

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError"
        except ValueError as e:
            return e
        except IndexError:
            return "IndexError"

    return wrapper


def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError"
        except ValueError as e:
            return e
        except IndexError:
            return "IndexError"

    return wrapper


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    try:
        record = book.find(name)
        if record:
            record.edit_phone(old_phone, new_phone)
            return f"Phone number updated for {name}."
        else:
            return "Contact not found."
    except KeyError:
        return "Contact not found."


@input_error
def show_phones(args, book: AddressBook):
    try:
        name = args[0]
        record = book.find(name)
        return [phone.value for phone in record.phones] if record else "Contact not found."
    except (KeyError, AttributeError):
        return "Contact not found."


@input_error
def show_all(book: AddressBook):
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args, book):
    name = args[0]
    birthday = args[1]
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday was added."
    else:
        raise KeyError


@input_error
def show_birthday(args, book):
    try:
        name = args[0]
        record = book.find(name)
        return str(record.birthday) if record and hasattr(record, 'birthday') else "Contact not found."
    except KeyError:
        return "Contact not found."


@input_error
def birthdays(args, book):
    try:
        upcoming_birthdays = book.get_upcoming_birthday()
        if not upcoming_birthdays:
            return "No upcoming birthdays."
        else:
            result = "Upcoming birthdays:\n"
            for record in upcoming_birthdays:
                result += f"{record.name}: {record.birthday.date.strftime('%d.%m.%Y')}\n"
            return result
    except (AttributeError, KeyError):
        return "No upcoming birthdays."


def parse_input(user_input):
    parts = user_input.strip().split(" ")
    if not parts:
        return None, []
    command = parts[0]
    args = parts[1:]
    if command not in ["hello", "add", "change", "phone", "all", "add-birthday", "show-birthday", "birthdays", "close", "exit"]:
        return "Invalid command.", []
    return command, args


def main():
    book = AddressBook.load_data()

    # Main program loop
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            book.save_data()
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phones(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
