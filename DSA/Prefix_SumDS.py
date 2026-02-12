'''
Docstring for DSA.Prefix_SumDS
Prefix sum data structure
comes in,
->hashing
->greedy
->DP

a=[10 20 30 40 50]
find the sum of elements upto ith index number
if i=0 then sum=10
if i=1 then sum=10+20=30 ..so on

a=[10,20,30,40,50]
prefix_sum=[10,30,60,100,150,210,280]
p[0]=0 to 0 index sum
p[1]=0 to 1 index sum ..so on
'''
a=[10,20,30,40,50]
psum=[0 for i in range(len(a))]
print(psum)

'''
sum=0 - (0+10=10)) -(20+10=30)
a=[10,20,30,40,50]
psum=[0,0,0,0,0]
for x in a:
    sum+=x
'''
sum=0
for x in a:
    sum+=x
    print(sum,end=" ")

#prefix sum array
