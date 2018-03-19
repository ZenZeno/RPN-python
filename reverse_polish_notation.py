def binary_operator(x, y, operator):

    if operator == '*':
        return x * y
    elif operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '/' and y != 0:
        return x / y
    else:
        #operator was not a valid symbol, so the expression is poorly formatted
        return 'ERR'

def unary_operator(x, operator):

    if operator == '!':
        return -x
    else:
        return 'ERR'

calc_string = input("Please enter a RPN expression to evaluate, or q to quit: ")

while calc_string != 'q':
    calc_list = calc_string.split()

    calc_list.reverse()

    while len(calc_list) >= 2:
        x = float(calc_list.pop())

        next_token = calc_list.pop()
        
        # if the next token is not a digit or a unary operator, set operator = 'ERR'. Then, the next if statement
        # will cause an  error message to be printed
        if next_token.isdigit():
            y =float(next_token)
            try:
                operator = calc_list.pop()
                result = binary_operator(x, y, operator)
            except:
                result = 'ERR'
        else:
            operator = next_token
            result = unary_operator(x, operator)
            
        if result == 'ERR':
            print("Error: Improperly formatted expression")
        else:
            calc_list.append(result)
    try:
        print(calc_list[0])
    except:
        pass #Error message already printed, we just want to supress Index Out of Bounds error

    calc_string = input("Please enter a RPN expression to evaluate, or q to quit: ")

