num = input("Enter Card number: ")
length = len(num)


counter = 1
if 13 <= length <= 16:
    print("***************************************")
    if num[:1] == "5":
        print("**Credit Card Type: MasterCard")
    elif num[:1] == "4":
        print("**Credit Card Type: Visa Card")
    elif num[:2] == "37":
        print("**Credit Card Type: American Express Card")
    elif num[:1] == "6":
        print("**Credit Card Type: Discover Card")
    else:
        print("**Credit Card Type: Invalid Card")
    print("**Credit Card Number:", num)
    print("**Credit Card Digit Length:", length)
    print("***************************************")

else:
    print("Invalid Card Number! Please Try Again")
