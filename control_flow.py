if 2 + 2 == 4:
  print("2 and 2 is four")
  print("arithmetic works")
else:
  print("2 and 2 is not four")


num = 15

if num < 10:
  print("number is less than 10")
elif num > 10:
  print("number is greater than 10")
else:
  print("Number is equal to 10")


want_cake = "yes"
have_cake = "no"

if want_cake == "yes":
    print("We want cake...")
    if have_cake == "no":
        print("But we don't have any cake")
    elif have_cake == "yes":
        print("And it's our lucky day")
else:
    print("The cake is a lie.")