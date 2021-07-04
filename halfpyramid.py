"""
Get an input from the user and generate pattern in the order as that can be referred below:
NB: Concept of nested loops will be helpful



INPUT: 
5
OUTPUT:
*
**
***
****
*****


INPUT:
3
OUTPUT:
*
**
***

"""

def halfPyramidStar(N):
    for i in range(N):
        for j in range(0, i + 1):
            print("*", end = "")
        print()
  
N=int(input("Enter input"));
halfPyramidStar(N);
