while True:
    name = input("enter your name dear: ")
    dob =int(input("enter a date of birth: "))

    print(dob)

    if dob <2002:
        print("THANKYOU!!",name ,"DOB IS ACCEPTED ")
        break

    else:
        print("wrong dob",dob)