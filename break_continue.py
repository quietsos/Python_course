
#break statement is used for stop the loop in a fixed position.

for i in range(1, 11):
    if i == 5:
        break
    print(i)


# continue statement is used for overlaping a stirng or number in a fixed position
# suppose we want to overlap 5 in a sequence of 1 to 10 ranges of number

for i in range(1,11):
    if i == 5:
        continue
    print(i)