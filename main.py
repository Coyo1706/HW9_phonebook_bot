help_text = '''Basic commands of the bot:
- add --The command adds the subscriber's phone number to the phonebook. If the subscriber is present in the phone book,
  the number will be added to the list of subscriber numbers. The command, name and phone number must be entered
  separated by a space (Spaces in name or phone number are not allowed).
  Example of command: add Bob +380441111111

- change --Changing an existing phone number. Command, name and both old and new phone number
  should be entered with a space (Spaces in the name or phone number are not allowed).
  Example of command: change Bob +380441111111 +30502222222

- phone --Show subscriber's phone number/numbers.
  Example of command: phone Bob

- show all --Shows the names and phone numbers of all callers in the phone book.
  Example of command: show all

- good bye, close, exit, stop, brake --Any of these commands finishes the work of the bot.'''

phonebook = {}


# Exception handling decorator
def input_error(func):
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except KeyError:
            return print("Please enter correct the subscriber name")

        except ValueError:
            return print("Please enter correct the subscriber name")

        except IndexError:
            return print(
                "Please enter the correct subscriber name and phone number, separated by a space.")
        except TypeError:
            return print('TypeError')

    return wrapper


print(
    'Welcome! Please enter: "hello" or "help"(To learn the basic bot commands)'
)


# User interaction function
def main():
    chat = True

    while chat:
        user_input = str(input('Enter your command: '))
        call_bot, data = bot_commands(user_input)
        if call_bot:
            if call_bot == close_bot:
                print('Good bye!')
                chat = False
            if data:
                call_bot(*data)
            else:
                call_bot()


# Function adds the subscriber's phone number to the phonebook.
@input_error
def subs_add(*args):
    print(args)
    name = args[0]
    phone_numb = args[1]
    if name not in phonebook:
        phonebook[name] = []
        phonebook[name].append(phone_numb)

    elif name in phonebook:
        phonebook[name].append(phone_numb)

    return phonebook, print(
        'New subscriber successfully added to the phonebook.')


# Function changing an existing phone number
@input_error
def change_subs_phone(*args):
    name = args[0]
    phone_numb = args[1]
    new_phone_numb = args[2]

    if name in phonebook:
        phonebook[name].remove(phone_numb)
        phonebook[name].append(new_phone_numb)

    return phonebook, print(f'The phone number {name} has been successfully changed')


# Function show subscriber's phone number/numbers
def phone_numbers(name):
    if name in phonebook:
        print(f'Name: {name} Phone: {phonebook.get(name)}')


# Function shows the names and phone numbers of all callers in the phone book
@input_error
def show_all_phonebook(*args, **kwargs):
    for k, v in phonebook.items():
        print(k, ":", ", ".join(v))


# Function to close the bot
def close_bot(*args):

    return 'close_bot'


# Help function
def help_txt(*args, **kwargs):
    print(help_text)


# Hello function
def hello(*args, **kwargs):
    print('How can I help you?')


user_commands = {
    'hello': hello,
    'add': subs_add,
    'change': change_subs_phone,
    'phone': phone_numbers,
    'show': show_all_phonebook,
    'help': help_txt
}

user_exit_commands = ['good bye', 'close', 'exit', 'stop', 'brake']


# Function for parsing user commands
@input_error
def bot_commands(user_input):
    input_items = user_input.split()
    command = input_items[0].lower()
    data = input_items[1:]

    if command in user_exit_commands:
        return close_bot, data

    elif command in user_commands.keys():
        return user_commands.get(command), data

    else:
        print('Your command is not validated, check if it is entered correctly (enter "help" for help).')
        return None, None


if __name__ == '__main__':
    main()
