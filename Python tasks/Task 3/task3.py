import itertools

right_numbers = 0

for i in range(372 ** 2, 809 ** 2 + 1):
    number_list = [int(j) for j in str(i)]

    condidion = 0


    for idx in range(1, len(number_list)):
        if number_list[idx - 1] <= number_list[idx]:
            condidion += 1

    if condidion == 5:

        repeated_digits = 0

        for key, group in itertools.groupby(number_list):
            if len(list(group)) > 1:
                repeated_digits += 1

        if repeated_digits > 1:
            right_numbers += 1

print(right_numbers)