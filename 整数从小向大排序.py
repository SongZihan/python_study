p = [5,9,3,1,4,9]
for i in range(len(p)):
    left = i
    for j in range(i+1,len(p)):
        if p[j]<p[left]:
            p[left],p[j] = p[j],p[left]
print(p)


