def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found"
        except IndexError:
            return "Not found"
        except Exception() as e:
            return e

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    for key in contacts.keys():
        if(key == name):
            contacts[name] = phone
            return "Phone changed."
    raise(KeyError)

@input_error
def user_phone(args,contacts):
    name = args[0]
    
    for key,values in contacts.items():
        if(key == name):
            return values
    raise(KeyError)

@input_error
def delete_contact(args, contacts):
    name = args[0]
    for key in contacts.keys():
        if(key == name):
            contacts.pop(key)
            return "Contact deleted."
    raise(KeyError)

@input_error
def all_contacts(contacts):
    list_contacts = []
    for key,values in contacts.items():
        list_contacts.append({key: values})
    if not list_contacts:
        raise(IndexError)   
    return list_contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":   
            print(change_contact(args, contacts))
        elif command == "phone":
            print(user_phone(args,contacts))
        elif command == "all":
            print(all_contacts(contacts))
        elif command == "delete": 
            print(delete_contact(args, contacts))       
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()