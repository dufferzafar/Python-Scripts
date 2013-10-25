s = 'asdbobkhjbobkolbobplobob'
s = 'azcbobobegghakl'

s = s.lower()

count = 0
p = 0

while s.find('bob', p) != -1:
    p = s.find('bob', p)
    p += 1
    count += 1

print("Number of times bob occurs is: " + str(count))