s = 'aeious'

s= s.lower()

count = 0

for a in range(len(s)):
    if (s[a] == 'a'):
        count = count + 1
    elif (s[a] == 'e'):
        count = count + 1
    elif (s[a] == 'i'):
        count = count + 1
    elif (s[a] == 'o'):
        count = count + 1
    elif (s[a] == 'u'):
        count = count + 1

print("Number of vowels: " + str(count))