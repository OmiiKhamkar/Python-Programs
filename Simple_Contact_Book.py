# Contact Book

contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact Saved!")

    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            for name, phone in contacts.items():
                print(f"{name} : {phone}")

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print("Found:", contacts[search])
        else:
            print("Contact not found.")

    elif choice == "4":
        break

    else:
        print("Invalid Option!")
