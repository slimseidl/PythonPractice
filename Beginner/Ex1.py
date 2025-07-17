def mutliplier(num1, num2):
    product = num1 * num2

    if product < 1000:
        return product
    else:
        return num1 + num2

num1 = int(input())
num2 = int(input())

print(f'The result is: {mutliplier(num1, num2)}')