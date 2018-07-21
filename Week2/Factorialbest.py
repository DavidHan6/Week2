def Factorial():
    n = input("what is your number")
    Answer = 1
    while n >= 0:
        Answer = Answer * n
        n -= 1
print(Factorial())
