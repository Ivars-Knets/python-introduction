# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0
i = 0
# seek user input for ten numbers 
while i<10:
    userInput = int(float(input("Enter any 2-digit number: ")))
    
# check to see if number is even and if yes, add to list_sum
# print incorrect value warning  when ValueError exception occurs
    try:
        number = userInput
        if number >= 10 and number < 100:
            user_list.append(number)
            if number % 2 == 0:
                list_sum += number
            i += 1
        else:
            print('Invalid number, try again.')

    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))