# Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

flower_dict = {}

with open('data/flowers.txt', 'r') as flower_file:
    for line in flower_file.readlines():
        line_split = line.split(": ")
        flower_dict[line_split[0]] = line_split[1]


user_name = input('Enter your name: ')
user_letter = user_name[0].upper()

print("Your special flower is a {}".format(flower_dict[user_letter]))