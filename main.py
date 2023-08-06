ADDRESSBOOK = {}



COMMANDS_LIST = ["'How to add a contact?'  - To add a new contact enter one of this commands: 'add', 'додай', '+' you can add to dictionarry contact name and his phone number, for example: 'add Kristian 393277889776'.",
"'How to change phone number of contact?' - To change contact phone number enter: change 'name of contact' 'new phone number', for example: 'change Kristian 380995552731.",
"'How to check phone number of a contact?' - To show phone number which you are iterested in enter: phone 'name of contact', for example: 'phone Kristian'.",
"'How to check which contacts do I have already in my dictionary?' - to show all contacts that you saved already enter 'show all'.",
"'How to close program?' - enter one of this commands 'good bye', 'close', 'exit' or you can use Ctrl C'.",
"'How can I check list of commands again?' - enter 'help'. 🙂"]


def input_error(wrap):   #working in case of errors
    def inner(*args):
        nonlocal wrap
        try:
            return wrap(*args)
        except (IndexError, KeyError, ValueError, TypeError):
            return "Give me the correct command please"
    return inner


@input_error
def add_handler(data):  # handler function
    name = data[0].title()
    phone = data[1]
    i = 0                 # in case if contact is already exist we add him a number for example Kristain , Kristian 1 , Kristian 2
    while True:
        new_name = name if i == 0 else f"{name} ({i})"
        if new_name not in ADDRESSBOOK:
            ADDRESSBOOK[new_name] = phone
            return f"Contact {new_name} with phone {phone} was saved"
        i += 1


@input_error
def change_handler(data):    #changing phone number function
    name = data[0].title()
    new_phone = data[1]
    if name in ADDRESSBOOK:
        ADDRESSBOOK[name] = new_phone
        return f"Contact {name} with new phone number - {new_phone} was saved"
    else:
        return f'Sorry, but {name} was not found in the address book.'



@input_error
def phone_shower_handler(data): #showing phone number function
    name = data[0].title()
    if name in ADDRESSBOOK:
        phone_to_show = ADDRESSBOOK.get(name)
        return f"Here is number of {name} and his phone number is - {phone_to_show}"
    else:
        return f"Contact {name} was not found"



@input_error
def show_handler(*args):
    if ADDRESSBOOK:                  #show all contacts function
        return f"Here is your phone list {ADDRESSBOOK}"
    else:
        return "there is no contacts in you contacts list"


@input_error
def help_handler(*args):      #help function
    return "\n".join(COMMANDS_LIST)


@input_error
def exit_handler(*args):   #finishing process
    return "Good bye!"


@input_error
def hello_handler(*args):  #saying hey to user
    return "How can I help you? If you don`t know commands to operate with program enter 'help'"


@input_error
def command_parser(raw_str: str): #command parser
    elements = raw_str.split()
    for key, value in COMMANDS.items():
        for command in value:
            if ' '.join(elements).lower().startswith(command):
                return key, elements[len(command.split()):]
    return None, ()



COMMANDS = {
    add_handler: ["add", "додай", "+"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"],
    change_handler: ["change"],
    phone_shower_handler: ["phone"],
    show_handler: ["show all"],
    help_handler: ["help"],
}


@input_error
def main(): #question-answer loop
    while True:
        user_input = input(">>>")  #add timur 380996602558
        if not user_input:
            continue
        if user_input.isspace():
            print("You provided a space. Give me name and phone, please!")
            continue
        func, data = command_parser(user_input)
        if func is None:  # Проверяем, что команда найдена
            print("Command not found. Please enter a valid command, or enter 'help' to find out what commands the program operates on. ")
            continue
        result = func(data)
        print(result)
        if func == exit_handler:
            break



if __name__ == "__main__":
    main()