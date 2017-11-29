import sys

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
    print("Prefix Expression")
    for test in test_string:
        print(Infix2Prefix(test))
    print("Postfix Expression")
    for test in test_string:
        print(Infix2Postfix(test))

if __name__ == "__main__":
    test()
