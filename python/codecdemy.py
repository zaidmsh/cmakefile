#!/usr/bin/env python
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    if type(food) == dict:
        for item in food:
            total += food[item]
    elif type(food) == list:
        for item in food:
            return food[item]
    else:
        return item
    return total

print compute_bill()
