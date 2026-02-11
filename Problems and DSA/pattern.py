#Nested loops
#outer loop for rows(lines) 
#inner loop for columns and connect them somehow to the rows
#print pattern inside the inner loop
#observe symmetry(optional)


'''
Docstring for Problems and DSA.pattern
**** 0->4 stars
**** 1->4
**** 2->4
**** 3->4
'''
def printPatter1(N):
    for i in range(N):
        for j in range(N):
            print("*",end=" ")
        print(" ")
printPatter1(4)
print(" ")

'''
Docstring for Problems and DSA.pattern
*       0->1 stars
**      1->2
***     2->3
****    3->4
'''
def printPatter2(N):
    for i in range(N+1):
        for j in range(i):
            print("*",end=" ")
        print(" ")
printPatter2(4)

'''
Docstring for Problems and DSA.pattern
1       0->1 stars
12      1->2
123     2->3
1234    3->4
'''
def printPatter3(N):
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print(" ")
printPatter3(4)

'''
Docstring for Problems and DSA.pattern
1       0->1 stars
22      1->2
333     2->3
4444    3->4
'''
def printPatter4(N):
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print(" ")
printPatter4(4)
print(" ")

'''
Docstring for Problems and DSA.pattern
**** 1-4 (4-i=1)+1=4 stars in row
***  2-3
**   3-2
*    4-1
'''
def printPattern5(N):
    for i in range(N+1):
        for j in range(1,N-i+1):
            print("*",end=" ")
        print(" ")
printPattern5(4)

def printPattern6(N):
    for i in range(N,0,-1):
        for j in range(i):
            print("*",end=" ")
        print(" ")
printPattern6(4)


'''
Docstring for Problems and DSA.pattern
12345 1-5 (4-i=1)+1=4 stars in row
1234  2-4
123   3-3
12    4-2
1     5-1
'''

def printPattern7(N):
    for i in range(N,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print(" ")
printPattern7(5)

'''
Docstring for Problems and DSA.pattern
SPACE-STARS-SPACE
  *     0-2,1,2
 ***    1-1,3,1
*****   2-0,5,0
Type	    Spaces      Stars
0-index	    N-i-1	    2*i+1
1-index	    N-i	        2*i-1
'''

def printPattern8(N):
    for i in range(N):
        for j in range(N-i-1):
            print(" ",end=" ")
        for j in range(2*i+1):
             print("*",end=" ")
        #for j in range(N-i+1):
         #   print(" ",end=" ")
        print(" ")
printPattern8(5)
'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
def printPattern9(N):
    for i in range(N-1,-1,-1):
        for j in range(N-i-1):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        print(" ")
printPattern9(5)
print("\n")
        
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
printPattern8(5)
def printPattern10(N):
    for i in range(N-2,-1,-1):
        for j in range(N-i-1):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        print(" ")
printPattern10(5)
        
'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
def printPattern10(N):
    for i in range(2*N-1): #10-1=9 rows(0...8)
        if(i<N): #5<5 false
            stars=i+1
        else:
            stars=(2*N)-i-1 #10-5-1=4 stars
        for j in range(stars):
            print("*",end=" ")
        print(" ")
printPattern10(5)



