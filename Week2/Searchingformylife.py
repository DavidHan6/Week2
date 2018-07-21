import time
tic = time.time()
def search(inpL, number):
    for index in range(len(inpL)):
        if number == inpL[index]:
            return index

    return -1

print(search(range(0, 20000000), 12345))
toc = time.time()
print(toc - tic)
