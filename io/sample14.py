import sys

print(type(sys.argv))
print(id(sys.argv))
print(sys.argv)

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')