#!/usr/bin/env python3

def isInt(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

def calculate(arg):
    stack = []
    for op in arg.split(" "):
            if isInt(op):
                stack.append(int(op))
            else:
                if op == '+' and len(stack) > 1:
                    result = stack[-1] + stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(result)
                elif op == '^' and len(stack) > 1:
                    result = stack[-1] ** stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(result)

    return stack[0]
                

def main():
    while True:
        print(calculate(input("rpn calc> ")))

if __name__ == '__main__':
    main()
