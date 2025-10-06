# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None
    
    freq = {}

    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_count = 0
    most_common = None
    for num, count in freq.items():
        if count > max_count:
            max_count = count
            most_common = num

    return most_common 

"""
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))
print(most_frequent([1, 2, 2, 3, 3]))
print(most_frequent([7, 7, 7, 7, 7,]))
print(most_frequent([]))

Time and Space Analysis for problem 1:
- Best-case: O (n)
One loop through the input list 
No early exits or nested loops

- Worst-case: O (n)
One loop through the input list 
No early exits or nested loops

- Average-case:
One loop through the input list 
No early exits or nested loops

- Space complexity: 
Best case: O(1), all numbers are the same
Average case: O(k), k is number of unique elements
Worse case O(n), all numbers are unique

- Why this approach?
You first want a frequency count for each individual number so you can compare it, while returning none if no number was entered)
Then in my 2nd loop I go through all the frequencies and see if they are more frequent then the last one and put that number as the one that has to be returned
I also put to return None for any empty list

- Could it be optimized?
It could probably be optimized but I know mine would be the simplest and fastest way it is possible
"""

# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    if not nums:
        return None

    unique = []
    seen = set()
    
    for num in nums:
        if num not in seen:
            unique.append(num)
            seen.add(num)
    return unique


"""
print(remove_duplicates([4, 5, 4, 6, 5, 7]))
print(remove_duplicates([]))
print(remove_duplicates([7, 7, 7, 7]))
print(remove_duplicates([3, 1, 2, 2, 1, 3]))


Time and Space Analysis for problem 2:
- Best-case: O(1), input has 1 element creating a set and converting back takes constant time
- Worst-case: O(n), input has n elements, all unique -> need to add all into a set, then convert back to list.
- Average-case: O(n), go through all numbers to scan for duplicates

- Space complexity:
- Best-case: O(1), all numbers are the same
- Worst-case: O(n), all numbers are unique
- Average-case: O(n), some unique numbers some the same

- Why this approach?
You wanna be able to remove duplicates so you make a list into a set which does this, and then make it a list again to be able to preserve order.


- Could it be optimized?
I dont believe this could be optimized, because both the time and space complexity are already good
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    pairs = []
    seen = set()
    
    for num in nums:
        left = target - num
        if left in seen:
            pairs.append((left, num))
        seen.add(num)
    
    return pairs



"""
print(find_pairs([1, 2, 3, 4], 5))
print(find_pairs([], 5))
print(find_pairs([2, 2, 2], 4))
print (find_pairs([3, 3, 4, 5, 6], 9))

Time and Space Analysis for problem 3:
- Best-case: O(n) Even if 1 pair exist you have to loop through the entire list once
- Worst-case: O(n) Still loop through all inputs and have to go through seen everytie
- Average-case: O(n) Always have to go through the list once

- Space complexity:
- Best case: O(1), if no pairs found, pairs list stays empty, seen grows minimally.
- Worst case: O(n), lots of unique pairs and seen set contains all elements.
- Average case: O(n), since seen usually grows with list size.

- Why this approach?
You need to make a list of all the pairs, and a set of seen so you have unique inputs. 
You go through all numbers and see if the number - the target so what is left is in seen and can make a pair with the number to get to the target.

- Could it be optimized?
I dont believe this could be optimized, because both the time and space complexity are already good

Tradeoff is avoiding duplicates vs storing state
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1            
    size = 0                
    arr = [None] * capacity 

    for i in range(n):
        if size == capacity:
            old_capacity = capacity
            capacity *= 2
            new_arr = [None] * capacity

            for j in range(size):
                new_arr[j] = arr[j]
            
            arr = new_arr
            print(f"Resized from {old_capacity} to {capacity}")

        arr[size] = i
        size += 1
        print(f"Added {i}, size={size}, capacity={capacity}")

    
"""
print(add_n_items(0))
print(add_n_items(1))
print(add_n_items(4))
print(add_n_items(6))

Time and Space Analysis for problem 4:
- When do resizes happen?
Once the size equals the capacity

- What is the worst-case for a single append?
The worst-case cost of a single append = O(n), since you must allocate a new list of size 2n (where n was the old capacity).
and then you must copy all n elements into the new list.

- What is the amortized time per append overall?
Amortized cost per insertion = O(1), since most of the time it just adds 1 but in some cases its O(n)

- Space complexity:
At any given time, we store a list of size equal to the current capacity. So it is O(n)

- Why does doubling reduce the cost overall?
If we only increased capacity by +1 each time, every append would trigger a copy → O(n^2) total time for n appends.
By doubling we copy elements only occasionally (at exponential intervals).

Trade-offs: the key trade-offs are between time efficiency, memory usage, and predictability.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    totals = []
    sum = 0
    for num in nums:
        sum += num
        totals.append(sum)
    return totals

"""
print(running_total([1, 2, 3, 4]))
print(running_total([]))
print(running_total([0, 0, 0, 0]))
print(running_total([2, -1, -2, 3]))

Time and Space Analysis for problem 5:
- Best-case: O(n), most visit all elements
- Worst-case: O(n), still just 1 pass
- Average-case: O(n) its allways O(n)

- Space complexity:
We store a new list of the same size as input so O(n) additional space.

- Why this approach?
You have to make a list so you can return all the totals and append it to it after you went through all the numbers 1 by 1

- Could it be optimized?
The time complexity is already O(n) and you will have to go through all the loop atleast once

Trade-off is memory vs preserving the original list.
"""

#Problem 5 Optimized

def running_totals_inplace(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

"""
Computes running totals directly in the input list to save memory.

Performance:
- Time: O(n), one pass through the list.
- Space: O(1), no extra list is created.

Optimization:
- Original version used O(n) extra space to store totals.
- This version overwrites the input list to achieve O(1) space while keeping O(n) time.
- Trade-off: original input values are lost.
"""