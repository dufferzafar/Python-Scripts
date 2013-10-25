s = 'asdbobkhjbobkolbobplobob'
# s = 'azcbobobegghakl'

# print(s.find('bob'))
# print(s[0:8])
#

count = 0
p = 0
while s.find('bob', p) != -1:
    p = s.find('bob', p)
    # print(p)
    p = p + 2
    count += 1

print("Number of times bob occurs is: " + str(count))