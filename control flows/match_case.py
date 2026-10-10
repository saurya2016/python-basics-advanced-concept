# concept of match case :-> what is match case match case is similar to a switch statement how the work of a match case is : it takes a value and match that valueb on a different cases aganist different values and if any value matched that value than the block of code of a perticular case will be executed that is a match case for you.print

#  here is a example of match case how it works :->


number = int(input("enter a number between 1 and 10 : "))

match number:
    case 3 :
        print("you won $100")

    case 7 :
        print("you won a mug")

    case 9 :
        print("you won a choclate")

    case _:
        print("you won nothing")


# _ : what is this ? this is default case.  for default case we use this : _(symbol). 

