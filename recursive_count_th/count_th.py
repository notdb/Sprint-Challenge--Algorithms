'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

#exit condition is when len(word) minus word.index is 2
counter = 0
def count_th(word):
    if word.find('th') == -1:
        return 0 
    return word.find('th', count_th(word.find('th')+2))
    
count_th('arthgyleth')
