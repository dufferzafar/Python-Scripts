s = 'aeious'

s= s.lower()

count = 0

for a in range(len(s)):
    if s[a] in 'aeiou':
        count += 1

print("Number of vowels: " + str(count))