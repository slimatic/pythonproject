#!/usr/bin/python3

a, b = 1, 2
if a < b:
    print('a ({}) is less than b ({})'.format(a, b))
else:
    print('a ({}) is not less than b ({})'.format(a, b))

print('foo')
print('foo' if a > b else 'bar')
print('foobar')

