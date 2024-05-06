class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_key):
        found_contacts = []
        for contact in self.contacts:
            if search_key.lower() in contact.name.lower() or search_key in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, old_name, new_contact):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                break

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

if __name__ == "__main__":
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_key = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_key)
            if found_contacts:
                print("Search results:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            found_contacts = contact_book.search_contact(name)
            if found_contacts:
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email address: ")
                new_address = input("Enter new address: ")
                updated_contact = Contact(new_name, new_phone, new_email, new_address)
                contact_book.update_contact(name, updated_contact)
                print("Contact updated successfully.")
            else:
                print("Contact not found.")

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
            print("Contact deleted successfully.")

        elif choice == "6":
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please select a valid option.")