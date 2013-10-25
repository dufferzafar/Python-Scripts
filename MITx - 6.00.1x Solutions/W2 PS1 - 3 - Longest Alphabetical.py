s = 'abcdefqazacd'
s = 'azcbobobegghakl'
s = 'abcbc'

s = s.lower()

opMax = ""
op = s[0]

for a in range(1, len(s)):
    if ord(s[a]) >= ord(s[a-1]):
        op = op + s[a]
    else:
        if len(op) > len(opMax):
            opMax = op
        op = s[a]

if len(op) > len(opMax):
    opMax = op

print("Longest substring in alphabetical order is: " + opMax)