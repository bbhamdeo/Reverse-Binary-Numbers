

from sys import argv

script, argument = argv

x = int(bin(int(argument))[:1:-1], 2)

print x

