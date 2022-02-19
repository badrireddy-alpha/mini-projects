# # write a program to check if a number entered by the user is negative
# a = int(input("enter any number : "))
# if a < 0:
#     print("you entered a negative number")
#     print("enter positive number dude")       # true block
# print("end of code")
#
# # o/p:
# #  enter any number : 30
# # end of code
#
# ####################
# # write a program to check if a number entered by the user is negative
# a = int(input("enter any number : "))
# if a < 0:
#     print("you entered a negative number")
#     print("enter positive number dude")       # true block
# print("end of code")
#
# # o/p:
# #  enter any number : -10
# # you entered a negative number
# # enter positive number dude
# # end of code
##############################
# wap to print if a number is even
# num = int(input("enter any number: "))
# if num % 2 == 0:
#     print("number is even")
#
# print("end of code")
# # o/p:
# # enter any number: 10
# # number is even
# # end of code
#
# # o/p 2
# # enter any number: 7
# # end of code
########################3
# wap to check if a number is odd
# num = int(input("enter any number: "))
# if num % 2 != 0: print("odd number");print("please enter even number dude")

# wap to check if a string is empty
# s = ""
# if not s: # bool(condition) # bool(s)
#     print("string is empty") # True block
# print("end of program")

# wap to check if a number is even or odd
# num = int(input("enter any number : "))
# if num % 2 == 0:
#     print("it is an even number")
# else:
#     print("it is an odd number")
######################333
# wap to check if the user is entering a number or a special character or an alphabet
# s = input("enter any character : ")
# if "a" <= s <= "z" or "A" <= s <= "Z":
#     print("it is an alphabet")
# elif "0" <= s <= "9":
#     print("it is a number")
# else:
#     print("it is a special character")
##################################
# wap to check if the user is entering a number or a special character or an lowercase or uppercase alphabet
# s = input("enter any character : ")
# if "a" <= s <= "z":
#     print("it is an lowercase alphabet")
# elif "A" <= s <= "Z":
#     print("it is an uppercase alphabet")
# elif "0" <= s <= "9":
#     print("it is a number")
# else:
#     print("it is a special character")
###########################################
# wap to print if a string is of even or odd length
# s = input("enter anything : ")
# if len(s) % 2 == 0:
#     print("string is of even length", len(s))
# else:
#     print("string is of odd length", len(s))
############################################
# wap to convert uppercase to lowercase and viseversa if it is a number or a special character print as it is
# user = input("enter any character : ")
# if 'a' <= user <= 'z' or 'A' <= user <= 'Z':
#     if "a" <= user <= "z":
#         print(chr(ord(user) - 32))
#     else:
#         print(chr(ord(user) + 32))
# else:
#     print(user)
# ######################################
# wap to check if a number is even or odd using inline if-else
# num = 1
# print("even number") if num % 2 == 0 else print("odd number")
########################################
# wap to check if entered character is vowel or not
# user = input("enter any character : ")
# if user in "aeiouAEIOU":
#     print("vowel")
# else:
#     print("not an vowel")

# wap to check greatest of three numbers

# a = int(input("enter a : "))
# b = int(input("enter b : "))
# c = int(input("enter c : "))
# if a > b and a > c:
#     print(" a is the greatest number")
# elif b > a and b > c:
#     print(" b is the greatest number")
# else:
#     print("c is the greatest number")
########################################
# wap to check if the ascii value of a character is even or odd
# c = input("enter any character : ")
# if ord(c) % 2 == 0:
#     print("ascii value is even ", ord(c))
# else:
#     print("ascii value is odd", ord(c))
##############################################
# wap to check if a given string is starting with a vowel or not
# i = input("enter any string : ")
# if i[0] in "AEIOUaeiou":
#     print("string is starting with vowel")
# else:
#     print("string is not starting with vowel")
################################################333
# wap to check if a given string is ending with a consonant or not
# c = input("enter any string: ")
# if c[-1] not in "AEIOUaeiou":
#     print("string is ending with consonant")
# else:
#     print("string is ending not with consonants")

###################################################
# wap to check if a given number is a perfect square or not
# num = 25
# sr = num ** 0.5         # 5.0
# sq = int(sr) ** 2       # 5 ** 2
# if num == sq:
#     print("perfect square")
# else:
#     print("not a perfect square")
##################################################
# wap to check if the dictionary is of even or odd length if it is even print it as it is else add
# a key to make it even and print it

# d = {1: 2, 3: 4, 5: 6, 7: 8}
# if len(d) % 2 == 0:
#     print(d)
# else:
#     d.update({"newkey": 10})
#     print(d)
##################################################
balance = 2000
pin = 9987
user_pin = int(input("enter your 4 digit atm pin: "))
if user_pin == pin:
    print("Welcome!!!!!",
          "press 1 to balance check",
          "press 2 to change the pin",
          "press 3 to withdraw ",
          "**************************", sep="\n")
    print()
    user_selection = int(input("enter your choice : "))
    if user_selection == 1:
        print("your balance is :  ", balance)
    elif user_selection == 2:
        new_pin_1 = int(input("please enter a valid 4 digit pin"))
        new_pin_2 = int(input("please confirm your pin : "))
        if new_pin_1 == new_pin_2:
            pin = new_pin_1
            print("your new pin is : ", pin)
        else:
            print("confirmation failed!  pins mismatching")
    elif user_selection == 3:
        entered_amount = int(input("enter withdrawal amount : "))
        if entered_amount % 100 == 0 or entered_amount % 500 == 0:
            if entered_amount <= balance:
                current_bal = balance - entered_amount
                print("please collect your cash! ")
                print(f"your current balance is {current_bal}")
            else:
                print("insufficient funds")
        else:
            print("enter a valid amount")
    else:
        print("please select a valid option")
else:
    print("enter valid pin")

