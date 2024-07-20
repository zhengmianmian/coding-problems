"""
 update a char in a string frequently
 cast it to a list first
 then do operations
 finally cast it back to a string
"""
s= 'abcd'
s=list(s)
s[0]='l'
s=''.join(s)
print(s)