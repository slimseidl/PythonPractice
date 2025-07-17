in_string = str(input())

print(f'Original string is {in_string}')
print(f'Print only even characters below:')


for char in range(len(in_string)):
    if char % 2 == 0:
        print(in_string[char])