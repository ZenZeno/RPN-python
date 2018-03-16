calc_string = input("Please enter a RPN expression to evaluate, or q to quit: ")

while calc_string != 'q':
    calc_list = calc_string.split()

    calc_list.reverse()

    while len(calc_list) >= 2:
        x = float(calc_list.pop())

        next_token = calc_list.pop()
        
        # if the next token is not a digit or a unary operand, set operand = 'ERR'. Then, the next if statement
        # will cause an  error message to be printed
        if next_token.isdigit():
             y =float(next_token)
             operand = calc_list.pop()
        elif next_token == '!':
            operand = next_token 
        else:
            operand = 'ERR'

        if operand == '*':
            calc_list.append(x * y)
        elif operand == '+':
            calc_list.append(x + y)
        elif operand == '-':
            calc_list.append(x - y)
        elif operand == '/' and y != 0:
            calc_list.append(x / y)
        elif operand == '/' and y == 0:
            calc_list = ['Error: Division by 0']
        elif operand == '!':
            calc_list.append(-x)
        else:
            #operand was not a valid symbol, so the expression is poorly formatted
            calc_list = ['Error: Imroperly formatted expression']

    print(calc_list[0])
    calc_string = input("Please enter a RPN expression to evaluate, or q to quit: ")

