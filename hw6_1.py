import re

from collections import UserDict
from dataclasses import dataclass


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Phone(Field):
    def __validation(self, value):
        if len(re.search(r"[^0-9]+", r"", value)) == 10:
            return value
        raise ValueError ('The number of digits in the number does not correspond to 10.')
    
    def __init__(self, value):
        self.value = self.__validation(value)

    def __str__(self):
        return str(self.value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone: str):
        self.phones.remove(Phone(phone))
    
    def edit_phone(self, phone: str, new_phone: str):
        self.__edit_phone(Phone(phone), Phone(new_phone))
    
    def __edit_phone(self, phone: Phone, new_phone: Phone):
        self.phones[self.__find_phone(Phone(phone))] = new_phone
   
    def find_phone(self, phone: str):
        return self.phones[self.__find_phone(Phone(phone))]
    
    def __find_phone(self, phone: Phone):
        try:
            return self.phones.index(phone)
        except:
            return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


@dataclass
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data.update(record)

    def find(self, name: str):
        for record in self.data.keys():
            if record == name:
                return self.data[name]
    
    def delete(self, name: str):
        self.data.popitem(Name(name))