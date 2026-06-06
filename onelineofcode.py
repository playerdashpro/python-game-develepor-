cart = ("alex", ["bob", "charlie"])

print(cart)

cart[1].append("dave")
print("after adding dave: ")
print(cart)

cart[1].remove("bob")
print("after removing bob: ")
print(cart)

cart[1][0] = "eve"
print("after changing charlie to eve: ")
print(cart)

print("owners, cat[0]")
print("items, cat[1]")