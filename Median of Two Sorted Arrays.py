
#nums1 = [2, 3, 4, 7]
#nums2 = [1, 5, 6, 8, 9]


nums1 = [1, 1, 1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 8, 8, 9, 9, 9]
nums2 = [2, 2, 4, 7]

#nums1 = [2]
#nums2 = [1, 2]

total = nums1 + nums2
total = sorted(total)
median = total[len(total)//2]
print(total, "Median=", median)

print(len(nums1), len(nums2), len(nums1)+len(nums2))



l1 = len(nums1)
l2 = len(nums2)

to_find = (l1 + l2)//2

print(to_find)

s1 = 0
s2 = 0
e1 = l1-1
e2 = l2-2
m1 = e1//2
m2 = e2//2

i = 1

n1 = nums1
n2 = nums2

found = -1
answer = -1

while i < 10 and found == -1:    
    
    m1 = (len(n1)-1)//2
    m2 = (len(n2)-1)//2
    
    print()
    print("i=", i, m1, m2)
          
    
    if len(n1) == 1 or len(n2) == 1:
        com = n1+n2
        com = sorted(com)
        answer = com[to_find]
        found = 1
    elif len(n1) == 0:        
        answer = n2[to_find]
        found = 1
    elif len(n2) == 0:
        answer = n1[to_find]
        found = 1
    elif to_find == 0:    
        answer = min(n1[0], n2[0])
        found = 1
    elif m1 == to_find and n1[m1] <= n2[0]:
        answer = n1[m1]
        found = 1
    print(to_find, ":", n1, m1, n1[m1], n2, m2, n2[m2])
        
    if n1[m1] < n2[m2]:
        prev_l = len(n1)
        n1 = n1[m1:]
        n2 = n2[:m2+1]
        to_find = to_find - (prev_l - len(n1))
        
    elif n1[m1] > n2[m2]:
        prev_l = len(n2)
        n2 = n2[m2:]
        n1 = n1[:m1+1]        
        to_find = to_find - (prev_l - len(n2))
        
        temp = n1
        n1 = n2
        n2 = temp
        
    else:
        prev_l = len(n1) + len(n2)
        if len(n1) % 2 == 1:
            n1 = n1[:m1+1]
        else:
            n2 = n2[:m2+1]        
            
        
    print(len(n1), len(n2))
    i+=1
    

print()
print("Answer:", answer)
if median == answer:
    print("Correct answer!!")
else:
    print("INCORRECT. Median is", median)
    