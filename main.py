 # ------------------------------------------------------------------------
# Lab 1
# Problem 1
#Create a list called my_list with the values [1, 5, 'apple', 20.5].
my_list = [1, 5, 'apple', 20.5]
# Using indexing, print the value 'apple' from my_list.
print(my_list[2])
# Add the value 10 to the end of my_list using the append() method. Print the updated list.
print(my_list.append(10))
# Remove the value 20.5 from my_list using the remove() method. Print the updated list.
print(my_list.remove(20.5))
# Reverse the order of the elements in my_list using a method. Print the reversed list.
print(my_list.reverse())

#Problem 2 
# Create a dictionary called person with keys 'name', 'age', 'job' and values 'John', 30, 'teacher'.
person = {'name':'John' , 'age':30 , 'job':'teacher'}
# Print the value corresponding to the 'job' key.
print(person["job"])
# Add a new key-value pair: 'city': 'Paris' to the person dictionary. Print the updated dictionary.
person["city"] = 'Paris'
print(person)
# Remove the 'age' key-value pair from person. Print the updated dictionary.
del person["age"]
print(person)
# Iterate through the person dictionary and print out each key-value pair on a separate line.
for key, value in person.items():
    print(f"{key}, {value}")
# -----------------------------------------------------------------------------


# Importing sys for test function
import sys


# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)


# Function 1: count_vowels
def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.

    Parameters:
    - s (str): The input string

    Returns:
    - int: The number of vowels in the string
    """
    #1. determine what are vowels 
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    #2.make a list for the counted vowels
    vowels_in_word = 0
    #3. take a word, and look for vowels in that word 
    for characters in s:
    #4. take the amount of vowels in that word
        if characters in vowels:
            vowels_in_word += 1 
    #5. return that number of vowels 
    return vowels_in_word
    # TODO: Implement this function


# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)


# Function 2: merge_lists
def extend_list(list_to_extend_into, list_to_append_items_from):
    for item in list_to_append_items_from:
        list_to_extend_into.append(item)
    return list_to_extend_into
def merge_lists(list1: list, list2: list) -> list:
    #while loop
    #if we were to increment i1, would it be a larger index than the index of the value with the larges index in list1
    #add the rest of list 2 to the merged list
    #because list2 is already in orde, and weve finished adding all the values in list1
    if not list1:
        return list2
    if not list2:
        return list1
    merged_list = []
    i1, i2 = 0, 0
    while len(merged_list) < len(list1) + len(list2):
        if list1[i1] < list2[i2]:
            merged_list.append(list1[i1])
            if i1 + 1 == len(list1):
                for item in list2[i2:]:
                    merged_list.append(item)
            else:
                i1 += 1
        else:
            merged_list.append(list2[i2])
            if i2 + 1 == len(list2):
                for item in list1[i1:]:
                    merged_list.append(item)
            else:
                i2 += 1
    return merged_list

    
    #check boths lists for what 

    # TODO: Implement this function
    


# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])


# Function 3: word_lengths
def word_lengths(words: list) -> list:
    """
    Get the lengths of words in a list.

    Parameters:
    - words (list): The list of words

    Returns:
    - list: A list containing the lengths of the words
    """

    #1. make a list for the amount of letters in a word 
    letters_in_word = []
    #2. make a loop to find number of letters in word
    for letters in words:
        letters_in_word.append(len(letters))
    #3. return that number 
    return letters_in_word
    # TODO: Implement this function
    


# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 11])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Function 4: reverse_string
def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Parameters:
    - s (str): The input string

    Returns:
    - str: The reversed string
    """
    list_s = []
    for characters in s:
        list_s.append(characters)
        final_index = len(list_s)-1
    reversed_list_s = [0]*len(list_s)
    for character in list_s:
        reversed_list_s[final_index] = character
        final_index -= 1
    return "".join(reversed_list_s)
    # TODO: Implement this function
    pass


# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    """
    Find the intersection of two lists.

    Parameters:
    - list1 (list): The first list
    - list2 (list): The second list

    Returns:
    - list: The intersection of the two lists
    """
    #0. create an intersection list
    intersection_list: list = []
    #1. select a list, preferbaly first list 
    #2. take that list and iterate it 
    for number in list1:
        #is number in list 2
        #3. check to see what items matches in each list
        if number in list2:
                #4. take those numbers that do match and move into a new intersection list
            intersection_list.append(number)
    #4.5. remove any duplicates, how?
        intersection_list = list(set(intersection_list))
    #5. return the intersection list
    return intersection_list

    # TODO: Implement this function



# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()
