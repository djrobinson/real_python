#first_num = input("First Number ")
#second_num = input("Second Number ")

#print("First times second:", float(first_num) * float(second_num))

def square(number):
    sqr_num = number ** 2
    return sqr_num

input_num = 5
output_num = square(input_num)

print(output_num)


def return_difference(n1, n2):
    """Return the difference between two numbers.
       Subtracts n2 from n1."""
    return n1 - n2
