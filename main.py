# task 1

# while True:
#     x = int(input("Enter any number: "))
#     if x >= -1 and x <= 17:
#         print("Входить")
#     else:
#         print("Не входить")

# task 2

# while True:
#     x = int(input("Enter any number: "))
#     if x <= -3 or x >= 7:
#         print("Входить")
#     else: 
#         print("Не входить")
#         break

# task 7
# x = int(input("Enter any 4 digit number: "))
# if 1000 <= x <= 9999:
#     if x % 7 == 0 or x % 17 == 0:
#         print("Beautiful")
#     else:
#         print("Not beautiful")

# else:
#     print("Not a 4 digit number")

# text = input("Write something: ")
# amount = int(input("Write how many times will the text repear itself: "))
# for i in range(amount):
#     print(text)

text = input("Write something: ")
for i in range(10):
    print(i, text)