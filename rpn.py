#!/usr/bin/env python3

import click
import operator
import readline
from termcolor import colored


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg, verbose):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            print(colored(arg1, "green") + colored(token, "red") + colored(arg2, "green"))
            result = function(arg1, arg2)
            stack.append(result)
        if verbose:
            print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

@click.command()
@click.option('-v', '--verbose', is_flag=True)
def main(verbose):
    while True:
        result = calculate(input("rpn calc> "), verbose)
        print(colored("Result: {}".format(result), "blue"))

if __name__ == '__main__':
    main()
