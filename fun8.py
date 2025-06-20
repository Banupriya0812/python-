
   # to Find Duplicates in a List

# def find_duplicates(a):
#     seen = set()
#     duplicates = set()

#     for item in a:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)
#     return list(duplicates)

# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 8, 7, 6, 4]
# d = find_duplicates(numbers)
# print("Duplicate elements:", d)



            # to find the maximum of three numbers
# def max_three(a,b,c):
#     return max(a,b,c)

# print(max_three(15,6,43))



        # to count the number of vowels in a string   
# def vowels_count(i):
#     return sum(1 for char in i if char.lower() in 'aeiou')
# print(vowels_count("maadhava"))

     

    #    to merge two dictionaries
# dict1 = {'a':1, 'b':2}
# dict2 = {'c':3, 'd':4}
# merged = {**dict1, **dict2}
# print(merged)



        #   to find common elements in two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
elements = list(set(list1) & set(list2))
print(elements) 
        