#!/usr/bin/python3
#Filename:rasing.py
class ShortIputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self):
        self.length=length
        self.atleast=atleast
try:
    text=input('Enter something -->')
    if len(text)<3:
        raise ShortInputException(len(text),3)
    except EOFError:
        print('Why did you do an EOF on me?')
    except ShortInputException as ex:
        print('ShortInputException:Thid input was {0} long,excepted at least {1}'.format(ex.lenth,ex.atleast))
    else:
        print('No exception was raised.')
