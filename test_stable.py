from indexed_integer import IndexedInteger
import random

def create_list(n=100):
    return [IndexedInteger(random.randint(0, 20), i) for i in range(n)]

def convert_list(integer_list):
    return [IndexedInteger(num, i) for i, num in enumerate(integer_list)]

def unstable_sort(l):
    l_copy = l.copy()
    random.shuffle(l_copy)
    return sorted(l_copy)


def stable_sort(unsorted_list):
    pass
    # Put your stable sort algorithm here, you don't need to modify your code at all, just change the parameter value
    # 'unsorted_list' to the name of what you call your list of integers
    # If you want to use a specific list instead of a randomly generated one you can call convert_list() on your list of integers
    # And pass it into this function, you need to use convert_list, because it will convert the numbers to my IndexedInteger class
    # You can either return your new sorted list, or don't return anything if you are sorting in place






def check_stable(l):
    for i in range(len(l)-1):
        if l[i] == l[i+1] and l[i].index >= l[i+1].index:
            return False, f'{l[i]} at current index {i} had original index {l[i].index} -- {l[i+1]} at current index {i+1} had original index {l[i+1].index}'
    return True, 'Your sorting appears to be stable! (In this case)'

#while True:
l = create_list(100)

print('BEFORE: ', l)
new_l = stable_sort(l) # We don't have to do it in place
if new_l:
    l = new_l # If the function returns something, set the list to that
print('AFTER: ', l)
print('EXPECTED:', unstable_sort(l))
print('Stable?: ', check_stable(l), 'THIS OUTPUT IS NOT A SUFFICENT ANSWER FOR THIS PART OF THE QUESTION, ONLY TO BE USED AS A BASIC CHECK DONT USE IT')
print('Sorted?:', l == unstable_sort(l))



