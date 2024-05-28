import csv


class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Phone:
    def __init__(self):
        self.contacts = []

    def load_contacts_from_csv(self, file):
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_phone_contact = PhoneContact(*row.values())
                self.contacts.append(new_phone_contact)

    def search_contacts(self, user_input):
        count = 0
        for contact in self.contacts:
            has_in_name = user_input.lower() in contact.name.lower()
            has_in_phone = user_input.lower() in contact.phone.lower()
            if has_in_name or has_in_phone:
                print(f'{contact.name} ({contact.phone})')
                count += 1
        if count == 0:
            print('Contact not found')


app = Phone()
app.load_contacts_from_csv('contacts.csv')
while True:
    app.search_contacts(input('Search contacts: '))
