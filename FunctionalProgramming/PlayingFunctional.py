from functools import reduce

print('--- Iterator example ---')


class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        # makes the object to an iterator
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1

        return self.current - 1


# print the iterated values
for c in Counter(3, 8):
    print(c)

print('--- Iterator example combined with a lambda function ---')
# Lambda / Anonymus function
squared = lambda x: x * x

# print the iterated values
for c in Counter(3, 8):
    print(c, '^2 = ', squared(c))

print('--- Iterator example combined with reduce function ---')
# use reduce on the iterator to gets the product of the counter values
print('product of the values: ', reduce((lambda x, y: x * y), Counter(3, 8)))

print('--- Higher order function example---')


def odd(*x):  # normal function which returns data
    return 'It\'s an odd ' + str(len(x) % 2)


def even(*x):  # normal function which returns data
    return 'It\'s an even ' + str(len(x) % 2)


def get_even_or_odd(list_len):  # function which returns functions depending on the logic
    if list_len % 2 == 0:

        return even
    elif list_len % 2 != 0:
        return odd


my_list = [1, 2, 3]
list_len = len(my_list)
result_function = get_even_or_odd(list_len)
print(result_function(*my_list))

my_list = [1, 2]
list_len = len(my_list)
result_function = get_even_or_odd(list_len)
print(result_function(*my_list))
