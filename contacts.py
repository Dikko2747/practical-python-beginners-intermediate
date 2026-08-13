import json


class ContactBook:
    def __init__(self, path="contacts.json"):
        self.path = path
        try:
            with open(path, encoding="utf-8") as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            self.contacts = []

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.contacts, f, indent=2)

    def add(self, name, phone):
        self.contacts.append({"name": name, "phone": phone})
        self.save()

    def search(self, term):
        return [
            contact
            for contact in self.contacts
            if term.lower() in contact["name"].lower()
        ]


def main():
    book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add")
        print("2. Search")
        print("3. List")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            book.add(name, phone)
            print("Contact saved.")

        elif choice == "2":
            term = input("Search name: ").strip()
            print(book.search(term))

        elif choice == "3":
            for contact in book.contacts:
                print(f"{contact['name']}: {contact['phone']}")

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
