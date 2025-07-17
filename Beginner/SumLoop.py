prev_num = 0

for num in range(1, 11):
    x_sum = prev_num + num
    print(f'Current Number: {num}, "Previous Number: {prev_num}, Sum: {x_sum}')
    prev_num = num