import random
numbers = []
for i in range(0,100):
    numbers.append(round(random.random() * 10000))

print('before ' + str(numbers))

def bubble_sort(input_list):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for (idx, num) in enumerate(input_list):
            if idx < len(input_list) - 1:
                if input_list[idx] > input_list[idx + 1]:
                    input_list[idx], input_list[idx + 1] = input_list[idx + 1], input_list[idx]
                    is_sorted = False

bubble_sort(numbers)

print('after ' + str(numbers))