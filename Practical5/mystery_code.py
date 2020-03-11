# What does this piece of code do?
# Answer: generate a prime number under 100

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:                         #if the n fail, try another
    p=True
    n = randint(1,100)          #generate a number under 100
    u = ceil(n**(0.5))          #the biggest divisor of n could be
    for i in range(2,u+1):      #check all the divisor could be 
        if n%i == 0:            #if there is a remainder equals to 0, then shows n is not a prime number         
            p=False


     
print(n)
