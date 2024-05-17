#10 
array = [45,65,87,23,54,2,1,6]
chot = []
nechot = []
for i in array [::-1] :
    if i %  2!=0 :
        nechot.append(i)

for i in array [::-1] :
    if i %  2==0 :
        chot.append(i)
print(chot)
print(nechot)

#8
array = [1,2,4,5,6,2,3,865,334]
k = []
for i in array[::-1]:
    if i % 2 != 0:
        k.append(i)

print(k)

# Задания 9

array = [2,865,334]
k = []
for i in array[::-1]:
    if i % 2 == 0:
        k.append(i)

print(k)
