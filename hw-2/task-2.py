from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("The number must contain 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        phone = Phone(phone)
        if phone in self.phones:
            self.phones.remove(phone)

    def find_phone(self, phone_number):
        phone = None
        for p in self.phones:
            if p.value == phone_number:
                phone = p
                break
        return phone

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if phone:
            phone.value = new_phone

    def __str__(self):
        return (
            f"Contact name: {self.name.value}, phones: "
            f"{'; '.join(p.value for p in self.phones)}"
        )


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name] if name in self.data else None

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)


def main():
    try:
        # Створення нової адресної книги
        book = AddressBook()

        # Створення запису для John
        john_record = Record("John")
        john_record.add_phone("1234567890")
        john_record.add_phone("5555555555")

        # Додавання запису John до адресної книги
        book.add_record(john_record)

        # Створення та додавання нового запису для Jane
        jane_record = Record("Jane")
        jane_record.add_phone("9876543210")
        book.add_record(jane_record)

        # Виведення всіх записів у книзі
        for name, record in book.data.items():
            # Виведення: Contact name: John, phones: 1234567890; 5555555555
            # Виведення: Contact name: Jane, phones: 9876543210
            print(record)

        # Знаходження та редагування телефону для John
        john = book.find("John")
        john.edit_phone("1234567890", "1112223333")

        # Виведення: Contact name: John, phones: 1112223333; 5555555555
        print(john)

        # Пошук конкретного телефону у записі John
        found_phone = john.find_phone("5555555555")
        # Виведення: John: 5555555555
        print(f"{john.name}: {found_phone}")

        # Видалення запису Jane
        book.delete("Jane")

        # Виведення всіх записів у книзі
        # після видалення запису Jane та оновлення запису John
        for name, record in book.data.items():
            # Виведення: Contact name: John, phones: 1112223333; 5555555555
            print(record)

    except Exception as e:
        print(f'An error occurred: {str(e)}')


if __name__ == "__main__":
    main()
