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

def cel_to_fahr(temp):
    return float(temp) * 9 / 5 + 32

def fahr_to_cel(temp):
    return (float(temp) - 32) * 5 / 9

print(cel_to_fahr(28))
print(fahr_to_cel(108))

'''
n = 1
while (n < 5):
    print("n=",n)
    n = n + 1
print("loop finished!")
'''
'''
for n in range(1, 5):
    print("n=",n)
print("loop finished")
'''

for n in range(1, 4):
    for j in ["a","b","c"]:
        print("n=",n,"j=",j)
