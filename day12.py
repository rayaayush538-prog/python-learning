# python
name = ["rahul", "mohan", "aniket", "amit"]

print(name[0:2])

name.append("sohel")
print(name)

name.append("anshika")
name.append("shreya")
name.append("nikhil")
name.append("shivani")
name.append(100)

print(name)

print(name[1:4])

name.append("anish")

print(name)

# yaha tk ke sare code sahi hai 

marks = [40, 20, 16, 76, 100]
print(marks )

marks.append("abhishek rai")
print(marks)

marks.remove(16)
print(marks)

marks.extend("aniket")
print(marks)

marks.extend(["anshika", "shreya", "nikhil"])
print(marks)

""" Bas ye formula yaad rakh:
Add: append → insert → extend
Remove: remove → pop → clear
Order: sort → reverse  """

marks.insert(1, "aalu")
print(marks)
"""
marks.insert(0,"lakshman")
prunt(marks)

# next list """

veg = ["potato", "Onion ", "Tomato", "lady's finger ", " Chilli"]
print(veg)
veg.append("jackfruit")
print(veg)

veg.clear()
print(veg)

veg.append("lemon")
print(veg)

veg.extend(["brinjal", "carrort", "cabbage","tricho-santhes-dioica"])
print(veg)

veg.remove("cabbage")
print(veg)

veg.pop(2)
print(veg)

veg.reverse()
print(veg)

veg.pop()
print(veg)

# end list 