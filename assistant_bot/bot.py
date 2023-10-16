def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."


def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise ValueError("Contact not found.")


def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        raise ValueError("Contact not found.")


def show_all(contacts):
    if not contacts:
        return "No contacts found."

    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Invalid command. Usage: add [name] [phone]")
            else:
                name, phone = args
                try:
                    print(add_contact(contacts, name, phone))
                except ValueError as e:
                    print(e)
        elif command == "change":
            if len(args) != 2:
                print("Invalid command. Usage: change [name] [phone]")
            else:
                name, phone = args
                try:
                    print(change_contact(contacts, name, phone))
                except ValueError as e:
                    print(e)
        elif command == "phone":
            if len(args) != 1:
                print("Invalid command. Usage: phone [name]")
            else:
                name = args[0]
                try:
                    print(show_phone(contacts, name))
                except ValueError as e:
                    print(e)
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
