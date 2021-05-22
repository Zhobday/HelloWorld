def fizzbuzz(x):

    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
        return
    elif x % 3 == 0:
        print("fizz")
        return
    elif x % 5 == 0:
        print("buzz")
        return
    print(x)

fizzbuzz(750)






