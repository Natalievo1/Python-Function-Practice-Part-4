from typing import List

def max_num(numOne: int, numTwo: int, numThree: int):
    max_value = numOne
    if max_value < numTwo:
        max_value = numTwo
    if max_value < numThree:
        max_value = numThree
    
    return max_value
    
def mult_list(nums: List) -> int:
    sum_of_nums = 1
    for x in nums:
        sum_of_nums *= x
    
    return sum_of_nums

def rev_string(word: str) -> str:
    length_of_word = len(word)
    rev_word = ""
    for i in range(length_of_word):
        rev_word += word[length_of_word - (i + 1)]
    
    return rev_word

def num_within(num: int, beginning_range: int, ending_range: int) -> bool:
    if ending_range > 0:
        if num >= beginning_range and num <= ending_range:
            return True
    if ending_range < 0:
        if num <= beginning_range and num >= ending_range:
            return True

    return False

def pascal(n: int):
    #first iteration
    initial_pascal_iter = [0,1,0]
    current_pascal_iter = []
    for value in range(n):
        # insert at first index 0 
        current_pascal_iter.insert(0, 0)
        length_of_initial = len(initial_pascal_iter)
        for idx in range(1,  length_of_initial):
            value = initial_pascal_iter[idx - 1] + initial_pascal_iter[idx]
            current_pascal_iter.append(value)
        # append 0 to the end
        current_pascal_iter.append(0)
        initial_pascal_iter = current_pascal_iter.copy()
        current_pascal_iter.clear()
    
    # remove 0's since they are not apart of the end result
    for x in range(2):
        initial_pascal_iter.remove(0)
    
    return initial_pascal_iter

def main():
    print("max_num_____________")
    print(max_num(1,2,3))
    print(max_num(10,5,4))
    print(max_num(-1,0,-8))
    print("--------------------")

    print("mult_list____________")
    print(mult_list([1,2,3,5,6]))
    print(mult_list([-10,-20,5,6,7]))
    print("---------------------")

    print("rev_string___________")
    print(rev_string("Hello World"))
    print(rev_string("natalie ojeda"))
    print(rev_string(""))
    print("---------------------")

    print("num_within___________")
    print(num_within(3,2,4))
    print(num_within(3,1,3))
    print(num_within(-10, 0, -11))
    print(num_within(-8, 0, -5))
    print("---------------------")

    print("pascal___________")
    print(pascal(3))
    print(pascal(7))
    print(pascal(5))
    print("---------------------")


if __name__ == "__main__":
    main()