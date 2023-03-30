#a=[8,2,3,0,7]; create a function that prints the sum of a list.

def sum_list(a):
    sum = 0
    for i in a:
        sum += i
    return sum

print(sum_list([8,2,3,0,7]))

#6. a=Hello; create a function to reverse a string.

def reverse_string(a):
    return a[::-1]

print(reverse_string('Hello'))

#a=[1,2,3,1,4,3,3,5,3,4,5]; create a function that returns a unique list.

def unique_list(a):
    return list(set(a))

print(unique_list([1,2,3,1,4,3,3,5,3,4,5]))

# create a function to find the number of lines containing '2'. in a file.

def count_2():
    with open('test.txt', 'r') as f:
        count = 0
        for line in f:
            if '2' in line:
                count += 1
    return count

print(count_2())

#Create a function to read test.txt and find the number of lines containing '00'.

def count_00():
    with open('test.txt', 'r') as f:
        count = 0
        for line in f:
            if '00' in line:
                count += 1
    return count

print(count_00())

#Create a function to read test.txt and find the number of lines ending with '3'.

def count_lines_ending_with_3(filename):
    count = 0
    with open('test.txt', 'r') as f:
        for line in f:
            if line.strip().endswith('3'):
                count += 1
    return count

print(count_lines_ending_with_3('test.txt'))

#num3.lst; create a function to find how many numbers are even.

def count_even_numbers():
    count = 0
    with open('num3.lst', 'r') as f:
        for line in f:
            if int(line) % 2 == 0:
                count += 1
    return count

print(count_even_numbers())
