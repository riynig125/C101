import random
from urllib import response
response = "y"
while response == "y":
    no =random.randint(1, 6)
    if no == 1:
        print("dice rolled the number 1")
    if no == 2:
        print("dice rolled the number 2")
    if no == 3:
        print("dice rolled the number 3")
    if no == 4:
        print("dice rolled the number 4")
    if no == 5:
        print("dice rolled the number 5")
    if no == 6:
        print("dice rolled the number 6")
    response = input("press y to roll again and n to exit")
    print("\n")
