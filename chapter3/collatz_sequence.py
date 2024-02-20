import sys
# We want to take in a number.
# If it is even, then integer divide by 2.
# If it is odd, then multiply the number by 3 and add 1
# Continue until the number is equal to 1

try:
    num = int(input('Give me a number: '))
except ValueError as e:
    print(f'A number is required - {e}')
    sys.exit(1)
print(num)
while num != 1:
    if num % 2:
        num = (num * 3) + 1
        print(num)
    else:
        num //= 2
        print(num)
