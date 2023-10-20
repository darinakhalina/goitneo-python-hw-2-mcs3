# decorator
def input_error(func):
    def inner(args, contacts):
        try:
            return func(args, contacts)
        except KeyError:
            return "Give me defined contact please."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name please."
    return inner


# add decorator
@input_error
def hello_command(*args):
    return "How can I help you?"


# Example for ValueError
# Enter a command: add testname - without phone
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


# Example for KeyError
# Enter a command: change invalidcontact 12345678 - with incorrect contact
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


# Example for IndexError
# Enter a command: phone - without name
@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def show_all(args, contacts):
    all_contacts = []
    for name, phone in contacts.items():
        all_contacts.append(f"{name} - {phone}")
    return "\n".join(all_contacts)


# map command names to the corresponding functions
COMMANDS = {
    hello_command: ("hello",),
    add_contact: ("add",),
    change_contact: ("change",),
    show_phone: ("phone",),
    show_all: ("all",),
}


# command and arguments from user input
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    # initializing an empty dictionary for contacts
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        # check if the user entered "close" or "exit" to exit
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        command_action = None

        # identify the correct command
        for action, keys in COMMANDS.items():
            if command in keys:
                command_action = action
                break

        # invalid command
        if command_action is not None:
            print(command_action(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
