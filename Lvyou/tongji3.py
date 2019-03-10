import os

count=0

for i in [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.json']:
    #count+=len(open(i, 'r').readlines())
    for count1,line in enumerate(open(i, 'r')):
        count1 += 1
    count+=count1
print(count)