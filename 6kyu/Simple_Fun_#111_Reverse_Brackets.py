from re import subn
def reverse_parentheses(st):
    while "(" in st:
        st=subn(r"\(([^()]*)\)",lambda x:x.group(1)[::-1],st)[0]
    return st