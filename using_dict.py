#!/usr/bin/python3
#Filename:using_dict.py
#'ab'是‘a’ddress'b'ook的缩写
ab={ 'Swaroop':'swaroop@swaroopch.com',
     'Larry'  : 'larry@wall.org',
    'Matsumoto' : 'matz@ruby-lang.org',
    'Spammer'   : 'spammer@hotmail.com'}
print("Swaroop's address is",ab['Swaroop'])
del ab['Spammer']
print('\nThere are {0} contacts in the address-book\n'.format(len(ab)))
for name,address in ab.items():
    print('Contact {0} at {1} '.format(name,address))
ab['Guido']='guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is",ab['Guido'])


