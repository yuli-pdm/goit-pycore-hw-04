def parse_input(user_input: str) -> tuple[str, list[str]]:
    user_input = user_input.strip()
    if not user_input:
        return "", []

    parts = user_input.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(name: str, phone: str, contacts: dict[str, str]) -> str:
    contacts[name] = phone
    return "Contact added."


def change_contact(name: str, phone: str, contacts: dict[str, str]) -> str:
    if name not in contacts:
        return "Error: Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(name: str, contacts: dict[str, str]) -> str:
    if name not in contacts:
        return "Error: Contact not found."
    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts saved."

    lines = []
    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")
    return "\n".join(lines)


def main() -> None:
    contacts: dict[str, str] = {}

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if len(args) != 2:
                print("Invalid command.")
            else:
                name, phone = args
                print(add_contact(name, phone, contacts))

        elif command == "change":
            if len(args) != 2:
                print("Invalid command.")
            else:
                name, phone = args
                print(change_contact(name, phone, contacts))

        elif command == "phone":
            if len(args) != 1:
                print("Invalid command.")
            else:
                name = args[0]
                print(show_phone(name, contacts))

        elif command == "all":
            if len(args) != 0:
                print("Invalid command.")
            else:
                print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
    