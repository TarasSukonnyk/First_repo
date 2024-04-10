from collections import UserDict

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
    def __init__(self, phone):
        if len(phone) != 10:
            raise ValueError
        super().__init__(phone)


class Record:
    def __init__(self, name): 
        self.name = Name(name)
        self.phones = list()

    def add_phone(self, phone): 
        for p in self.phones: 
            if p.value == phone: 
                return
        self.phones.append(Phone(phone))

    def remove_phone(self, phone): #
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
    
    def edit_phone_alternative(self, old_phone, new_phone):
        '''This method checks if the phone exists'''
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone): 
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError
    
    def __str__(self):
        return f'Record(Name: {self.name} Phones: {self.phones})'
    
    def __repr__(self):
        return f'Record(Name: {self.name} Phones: {self.phones})'
    

class RecordAlternative:
    def __init__(self, name): 
        self.name = Name(name)
        self.phones = list()

    def add_phone(self, phone): 
        if self.find_phone(phone):
            return
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):  
        phone = self.find_phone(phone)
        if phone:
            self.phones.remove(phone)
            return
        raise ValueError
    
    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if phone:
            phone.value = new_phone
            return
        raise ValueError

    def find_phone(self, phone): 
        for p in self.phones:
            if p.value == phone:
                return p


class AddressBook(UserDict): 
    def add_record(self, record: Record): 
        name = record.name.value
        self.data.update({name: record}) 

    def add_record_alternative(self, record: Record): 
        name = record.name.value
        self.update({name: record}) 

    def find(self, name):
        return self.get(name) 
    
    def delete(self, name):
        del self[name]





john = Record('John')
john.add_phone('1234567890')

addressBook = AddressBook()
addressBook.add_record(john)

jane = Record('Jane')
jane.add_phone('1234567890')

addressBook.add_record(jane)

print(addressBook.find('John'))