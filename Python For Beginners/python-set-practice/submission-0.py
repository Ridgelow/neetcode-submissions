from typing import List

def contains_duplicate(words: List[str]) -> bool:
    mylist = (words)
    myset = set(words)
    length = len(myset)
    length2 = len(mylist)
    if length == length2:
            return False     
    else:
            return True
            

# we are going to take the length, and then compare it to each
#in the length using a for loop


# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
