def hello_message(name):
    if isinstance(name, str):
        return 'Hi ' + name
    else:
        return "I am not a string"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(hello_message('Kaleo'))
