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


#Create a function to read num3.lst and sum all the numbers that can be divided by 7 with no remainder.

def sum_numbers_divisible_by_7():
    sum = 0
    with open('num3.lst', 'r') as f:
        for line in f:
            if int(line) % 7 == 0:
                sum += int(line)
    return sum

print(sum_numbers_divisible_by_7())

# a=[3,4,1,6,9,3] create a script that gets six numbers and prints the largest number.

# def get_largest_number():
#     a = []
#     for i in range(6):
#         a.append(int(input('Enter a number: ')))
#     return max(a)

# print(get_largest_number())

#create a script that gets the six numbers from a=[3,4,1,6,9,3]", and print their sum.

def get_sum_of_numbers():
    a = [3,4,1,6,9,3]
    sum = 0
    for i in a:
        sum += i
    return sum

print(get_sum_of_numbers())


#3. lst=['a','c','a','a','b','d','e','r','x','a']; create a script that removes duplicated items from the list.
lst = ['a', 'c', 'a', 'a', 'b', 'd', 'e', 'r', 'x', 'a']

# create an empty list to store unique items
unique_lst = []

# iterate over each item in the original list
for item in lst:
    # check if the item is not already in the unique list
    if item not in unique_lst:
        # add the item to the unique list
        unique_lst.append(item)

# print the unique list
print(unique_lst)



#var type 

str="My name is Josef, and I'm trying to write Python scripts"
str2 = str.split()

print(str2)
type(str2)
