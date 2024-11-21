from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

math_dict ={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    continue_with_result = 'y'
    first_num = float(input("What's the first number?:  "))
    while continue_with_result == 'y':
        for key in math_dict:
            print(key)
        operation = input("Pick an operation:  ")
        second_num = float(input("What's the second number?:  "))
        chosen_operation = math_dict[operation]
        result = chosen_operation(first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {result}")
        continue_with_result = input(f"Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation: ").lower()
        if continue_with_result == 'y':
            first_num = result
        else:
            print("\n" * 15)
            calculator()


calculator()

