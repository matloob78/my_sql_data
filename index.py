print("I gusy! how are you?")
print("Hi, How are you?")
age = int(input("Enter Age :"))
if age>=18:
    print("Conraulation!")
else:
    print("Sorry!")

na = input("Enter your name :")
if na == "John":
    print("Hello John!")
    if age>=18:
        print("You are eligible to vote!")
else:
    print("Hello " + na + "!")
isUser = int(intput("Enter user age"))
if isUser>= 18:
    print("Access")
    if isUser<18:
        print("Denied!")
print(f"Thank You {isUser}")
