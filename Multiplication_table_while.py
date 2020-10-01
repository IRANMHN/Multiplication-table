def table():
    x = float(input("enter a number to get a table:>"))
    i=1
    while i<=10:
        print(x, "x", i, "=", x*i)
        i += 1
table()
inp = input("press y to continue:>")
if inp.lower()=="y":
    while inp.lower()=="y":
        table()
            inp = input("press y to continue:>")
else:
    print("thanks for using this program see you next time./././.")
