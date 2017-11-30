import sys

priority = {'(': 1, '+': 2, '-':2, '*':3, '/':3, '%':3}
def infix_to_prefix(expression):
    global priority
    operand_stack = []
    symbol_stack = []
    index = 0
    while index < len(expression):
        if expression[index] == ' ':
            continue
        elif expression[index] == '(':
            symbol_stack.append(expression[index])
        elif expression[index] == ')':
            while len(symbol_stack) > 0 and symbol_stack[-1] != '(':
                get_prefix_subexpression(symbol_stack, operand_stack)
            if len(symbol_stack) > 0 and symbol_stack[-1] == '(':
                symbol_stack.pop()
        elif expression[index] in '+-*/%':
            while len(symbol_stack) > 0 and priority[expression[index]] <= priority[symbol_stack[-1]]:
                get_prefix_subexpression(symbol_stack, operand_stack)
            symbol_stack.append(expression[index])
        else: #expression[index] is an operand
            operand_stack.append(expression[index])

        index += 1

    while len(symbol_stack) > 0 and len(operand_stack) > 1:
        get_prefix_subexpression(symbol_stack, operand_stack)

    assert len(operand_stack) == 1
    return operand_stack[0]

def get_prefix_subexpression(symbol_stack, operand_stack):
    if len(symbol_stack) > 0 and len(operand_stack) > 1:
        second_oper = operand_stack.pop()
        first_oper = operand_stack.pop()
        symbol = symbol_stack.pop()
        operand_stack.append("{0}{1}{2}".format(symbol,first_oper,second_oper))
    else:
        raise NameError("Input stack does not have enough element!")

def infix_to_postfix(expression):
    global priority
    operand_stack = []
    symbol_stack = []
    index = 0
    while index < len(expression):
        cur_char = expression[index]
        index += 1
        if cur_char == ' ':
            continue
        elif cur_char == '(':
            symbol_stack.append(cur_char)
        elif cur_char == ')':
            while len(symbol_stack) > 0 and symbol_stack[-1] != '(':
                get_postfix_subexpression(symbol_stack, operand_stack)
            if len(symbol_stack) > 0 and symbol_stack[-1] == '(':
                symbol_stack.pop()
        elif cur_char in "+-*/%":
            while len(symbol_stack) > 0 and priority[cur_char] <= priority[symbol_stack[-1]]:
                get_postfix_subexpression(symbol_stack,operand_stack)
            symbol_stack.append(cur_char)
        else: #expression[index] is an operand
            operand_stack.append(cur_char)

    while len(symbol_stack) > 0 and len(operand_stack) > 1:
        get_postfix_subexpression(symbol_stack, operand_stack)

    assert len(operand_stack) == 1
    return operand_stack[0]

def get_postfix_subexpression(symbol_stack, operand_stack):
    if len(symbol_stack) > 0 and len(operand_stack) > 1:
        second_oper = operand_stack.pop()
        first_oper = operand_stack.pop()
        symbol = symbol_stack.pop()
        operand_stack.append("{0}{1}{2}".format(first_oper, second_oper, symbol))
    else:
        raise NameError("Input stack does not have enough element!")

#Fully Parenthesize
#argument: infix expression
def get_fully_parenthesized(expression):
    operator_list = []
    prefix_expression = infix_to_prefix(expression)
    input_queue = list(prefix_expression)
    return ''.join(parenthesize(input_queue, operator_list))

def parenthesize(input_queue, operator_list):
    res = []
    if len(input_queue) <= 0 or (not input_queue[0] in '+-*/%'):
        return res
    else:
        res.append('(')
        operator_list.append(input_queue.pop(0))
        #Left Operand
        if input_queue[0] in '+-*/%':
            res.append(''.join(parenthesize(input_queue, operator_list)))
        else:
            res.append(input_queue.pop(0))
        #Infix Operator
        res.append(operator_list.pop())
        #Right operand
        if input_queue[0] in '+-*/%':
            res.append(''.join(parenthesize(input_queue, operator_list)))
        else:
            res.append(input_queue.pop(0))
        res.append(')')
        return res



# Need expression to be fully parenthesized
def Infix2Prefix(expression):
    res = []
    left_index_stack = []

    for i in range(len(expression)):
        if expression[i] == '(': #left parenthesis, record index and use '(' to hold the place
            left_index_stack.append(len(res))
            res.append(expression[i])
        elif expression[i] in "+-*/%": #operator
            assert len(left_index_stack) > 0
            left_index = left_index_stack.pop()
            res[left_index] = expression[i]
        elif expression[i] == ')' or expression[i] == ' ':
            continue
        else:
            res.append(expression[i])

    return ''.join(res)

#Need expression to be fully parenthesized
def Infix2Postfix(expression):
    res = []
    symbol_stack = []

    for i in range(len(expression)):
        if expression[i] == '(' or expression[i] == ' ':
            continue
        elif expression[i] in "+-*/%":
            symbol_stack.append(expression[i])
        elif expression[i] == ')':
            assert len(symbol_stack) > 0
            right = symbol_stack.pop()
            res.append(right)
        else:
            res.append(expression[i])

    return ''.join(res)

def test():
    test_string = ["(A+(B*C))","((A+B)*(C+D))","((A*(B+C))+(D/E))"]
    print("Prefix Expression(Require infix expression to be fully parentheized)")
    for test in test_string:
        print(test,":",Infix2Prefix(test))
    print("Postfix Expression(Require infix expression to be fully parentheized)")
    for test in test_string:
        print(test,":",Infix2Postfix(test))
    test_string2 = ["A+B*C+D", "A+B*(C+D)", "(A+B)*(C-D)"]
    print("Prefix Expression")
    for test in test_string2:
        print(test,":", infix_to_prefix(test))
    print("Postfix Expression")
    for test in test_string2:
        print(test,":", infix_to_postfix(test))
    print("Fully Parenthesized")
    for test in test_string2:
        print(test,":", get_fully_parenthesized(test))

if __name__ == "__main__":
    test()
