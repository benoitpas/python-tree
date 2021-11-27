import functools

def add_id(tree, init):
    if( len(tree) > 0):
        v = tree[0]
        rest = functools.reduce( lambda a,e :  a, tree[1:], "coco")
        r = [(v,init)]
    else:
        r = tree
    return r

t = ['a', ['b'], ['c', ['d'], ['e']]]
print(t)
print(add_id(t, 0))