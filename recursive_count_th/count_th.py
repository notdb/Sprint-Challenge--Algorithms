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

    foo = word.find('th')
    if foo == 0:
       
        print(foo)
        return count_th(word[2:])
    else:
        return count_th(word[foo:])
   
count_th('abcthefthghith')
    
