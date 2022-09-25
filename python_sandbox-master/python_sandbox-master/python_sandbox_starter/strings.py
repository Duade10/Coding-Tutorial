# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

""" STRINGS CONCATENATION """

first_name = 'Timi'
last_name = 'Otunla'
print("My first name is " + first_name + " and my last name is " + last_name )


""" USING POSITIONAL ARGUMENTS """
# 1ST METHOD
print("My first name is {first_name} and my last name is {last_name}".format(first_name=first_name, last_name=last_name))

# 2ND METHOD
my_name = "My first name is {first_name} and my last name is {last_name}"
print(my_name.format(first_name="Abdullahi", last_name="Bello"))


""" FORMATTED STRINGS """
print(f"My first name is {first_name} and my last name is {last_name}")


"""RECEIVING INPUT FROM USERS"""

# Using the input() function

phone = input('What type of phone do you use? ')
color_of_trouser = input("What color is the trousers that you're wearing? ")
print(f"You use a {phone} phone and a wearing a {color_of_trouser.lower()} trouser")



