# Ask user for first number
# Ask user for second number
# Ask user for an operation to perform
#Perform operation on the two numbers
#Print result to the terminal

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    
    return False

prompt('Welcome to Calculator')
prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

print(f'{number1} {number2}')

print('What operation would you line to perform?\n 1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

print(f'The result is: {output}')