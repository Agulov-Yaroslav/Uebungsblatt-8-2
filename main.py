#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Übungsblatt 08-2"""


# Aufgabe 6


def power(exponent):
    """
    Decorator, welcher dafür sorgt, dass die Elemente des ersten Arguments einer Funktion
    zuerst mit angegebenen Parameter exponent potenziert werden.
    Ist eine negative Zahl in sequence enthalten, so soll eine Fehlermeldung ausgegeben werden

    :param exponent:
    :return:
    """

    def potenzieren(func):
        def func_wrapper(sequence):

            if any(x < 0 for x in sequence):
                print("No negative numbers allowed")
                return None

            sequence = [x ** exponent for x in sequence]
            return func(sequence)

        return func_wrapper

    return potenzieren


def print_sum(sequence):
    """Print and return the sum of the sequence"""
    result = 0
    for number in sequence:
        result += number
    print("The sum of {} is {}".format(sequence, result))
    return result

def print_prod(sequence):
    """Print and return the product of the sequence"""
    result = 1
    for number in sequence:
        result *= number
    print("The product of {} is {}".format(sequence, result))
    return result


# Testaufrufe

if __name__ == "__main__":
    print_sum([1, 2, 3])
    print_prod([1, 2, 3])
    print_sum([1, -2, 3])
    print_prod([-1, 2, 3])
