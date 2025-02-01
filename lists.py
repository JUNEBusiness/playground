fruits = ["Apple", "Mango", "Banana", 'Watermelon', "Orange", "Beetroot", 6]

# for fruit in fruits:
#     print("fruit =", fruit)

# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[-1])

""" Intead of using repetitive printing we can use a wonderful tool called loops,"""

# for i in range(10):
#     # print(f"number {i}")
#     print("meow")

# for i in range(10):
#     print(f"number {i}")


# [0,1,2,3,4,5,6,7,8,9]
# for number in range(7):
#     print(fruits[number])

""" Modifying our code since we know that range gives somewhat like a list, why don't we use
    the fruits list directly"""

# for fruit in ["Apple", "Mango", "Banana", 'Watermelon', "Orange", "Beetroot", 6]:
#     print(fruit)

"""Lists are mutable i.e can be reassigned another element"""
fruits[0] = "Plum"
for fruit in fruits:
    print(fruit)