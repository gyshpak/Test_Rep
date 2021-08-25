import sys
our_list = []

print('Insert number')
our_number = int(sys.stdin.readline())
our_string = str(our_number)

our_summa = 0
for i in our_string:
    our_list.append(i)
    our_summa += int(i)

print("sum of digits = ",our_summa)

our_list.reverse()
revers_number = int("".join([str(l) for l in our_list]))
print("revers of our number = %d"%(revers_number))

our_list.sort()
sort_number = int("".join([str(l) for l in our_list]))
print("sort of our number = %d"%(sort_number))

a=1
b=5
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)
a,b=b,a
print(a,b)