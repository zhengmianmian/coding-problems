"""
We can render an ASCII art pyramid with N levels by printing N rows of asterisks, 
where the top row has a single asterisk in the center and each successive row has two additional asterisks on either side.

Here's what that looks like when N is equal to 3.

  *  
 *** 
*****
And here's what it looks like when N is equal to 5.

    *    
   ***   
  ***** 
 ******* 
********* 
Can you write a program that generates this pyramid with a N value of 10?
"""

def pyramid(n):
    width = 2 * n - 1
    half = width // 2
    for i in range(n):
        t = 2 *(i+1) -1
        # half space, t *, half space
        print(' ' * half, end='')
        print('*' * t, end='')
        print(' ' * half, end='')
        print()
        half = half - 1

pyramid(10)