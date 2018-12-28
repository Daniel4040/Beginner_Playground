num_Base10 = int(input("Your number is: "))
y = 0
num_Base2 = ""

while (2**y) <= (num_Base10 / 2):
    y +=1

print("The number of times 2 goes into your number is: " + str(y))

for i in range(y, -1, -1):
    if (num_Base10 - 2**i) >= 0:
        num_Base2 = num_Base2 + "1"
        num_Base10 = num_Base10 - (2 ** i)
    else:
        num_Base2 = num_Base2 + "0"


    print(num_Base10)

print(num_Base2)

count= 0
max_consec_count = 0

for i in num_Base2:
    if i == '1':
        count +=1
    elif count > max_consec_count:
        max_consec_count = count;
        count = 0
    else:
        count = 0
if count > max_consec_count: max_consec_count = count

print(max_consec_count)
