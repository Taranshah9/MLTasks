lst = ['0001', '0011', '0101', '1011', '1101', '1111']
new_lst = []
temp1 = 0
temp2 = 0

for item in lst:
    new_lst.append(int(item, 2))
i = int(len(new_lst))
for item in new_lst:
     for j in range(0, len(new_lst)):
         if i > 2:
             new_lst.sort()
             temp1 = new_lst[i-2]
             new_lst.pop(i-2)
             temp2 = new_lst[i-3]
             new_lst.pop(i-3)
             new_lst.append(temp1+temp2)
             i -= 1
         else:
             break


new_lst.sort()
print(new_lst)