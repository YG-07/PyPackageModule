#-*- coding:utf-8 -*-
num=100
num1=111
num2=222

def run():
    print('run')

class Person:
    @staticmethod
    def eat():
        print('a person eating')


__all__ = ['num', 'run', 'Person']