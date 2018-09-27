string = input()
counter = 1
i = 0
while i + 1 < len(string):
    if string[i] == string[i + 1]:
        counter += 1
    else:
        print(string[i], sep="", end="")
        print(counter, sep="", end="")
        counter = 1
    i += 1
j = 2
while string[len(string) - 1] == string[len(string) - j]:
    j += 1
print(string[len(string) - 1], sep="", end="")
print(j - 1, sep="", end="")
