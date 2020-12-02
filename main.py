# look at both files and count the number of "if" s
# append the number to the end of the file
# compare the numbers of both files

with open("if.txt", "r") as file1:
    count1 = 0
    for line in file1:
        if "if " in line:
            count1 = count1 + 1
        elif "If " in line:
            count1 = count1 + 1

with open("if.txt", "a") as file1:
    file1.write("\n" + str(count1))

with open("mam.txt", "r") as file2:
    count2 = 0
    for line in file2:
        if "if " in line:
            count2 = count2 + 1
        elif "If " in line:
            count2 = count2 + 1

with open("mam.txt", "a") as file2:
    file2.write("\n" + str(count2))

if count1 == count2:
    print("They both have an equal amount")
elif count1 > count2:
    print("'if' by Rudyard Kipling has more")
elif count1 < count2:
    print("'mam' by J.P. McEvoy has more")


