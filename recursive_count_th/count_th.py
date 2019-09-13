'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

#exit condition is when len(word) minus word.index is 2
counter = 0
stored_word = 'arthgyleth'
def count_th(word):
    if len(word) == 0:
        return 0

    foo = word.find("th")
    if foo == 0:
        return count_th(word[2:])
    else:
        
        return count_th(word[foo:])+1
   
   
print(count_th("arthgyleth"))
    
def testFind(word):
   print(word.find("h"))

#testFind('HHHHh')
