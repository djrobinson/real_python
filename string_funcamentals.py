my_number = "12"

print(int(my_number))

print(float(my_number))

my_float = "12.0"

#print(int(my_float))

print(str(12) + "12")

name = "couch"
num_heads = 7
num_arms = 8

print("{} has {} heads and {} arms".format(name, num_heads, num_arms))


print("{2} has {1} heads and {0} arms".format(name, num_heads, num_arms))

print("{name} has {num_heads} heads and {num_arms} arms".format(
    name="Zaphod", num_heads=2, num_arms=3
))

phrase = "looking inside of this string for a word"

print(phrase.find("inside"))

print(phrase.replace("looking", "searching"))
