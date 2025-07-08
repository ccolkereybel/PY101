# Ask user for first number
# Ask user for second number
# Ask user for an operation to perform
#Perform operation on the two numbers
#Print result to the terminal

def prompt(message):
    print(f'==> {message}')

prompt('Welcome to Calculator')
prompt("What's the first number?")
number1 = input()
prompt("What's the second number?")
number2 = input()

print(f'{number1} {number2}')

print('What operation would you line to perform?\n 1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

if operation == '1':
    output = int(number1) + int(number2)
elif operation == '2':
    output = int(number1) - int(number2)
elif operation == '3':
    output = int(number1) * int(number2)
elif operation == '4':
    output = int(number1) / int(number2)

print(f'The result is: {output}')