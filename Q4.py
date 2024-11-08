#section b q4

isbn = []
for i in range (0,13):
    digit = int(input("Please enter next digit of ISBN: "))
    isbn.append(digit)

CalculatedDigit  = 0 
Count = 0

while Count < 12:
    CalculatedDigit = CalculatedDigit + isbn[Count]
    Count = Count + 1
    CalculatedDigit = CalculatedDigit + (isbn[Count] * 3)
    Count = Count + 1

while CalculatedDigit >= 10:
    CalculatedDigit = CalculatedDigit - 10

CalculatedDigit = 10 - CalculatedDigit

if CalculatedDigit == 10:
    CalculatedDigit = 0

if CalculatedDigit == isbn[-1]:
    print("Valid ISBN")
else:
    print("Invalid ISBN")
