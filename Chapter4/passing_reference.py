def fun(someParameter):
    someParameter.append('Hello')

one = [1, 2, 3]
fun(one)
print(one)

# when passing one to fun(), a copy of the reference is used for the paremeter
# even though one and someParameter contain separate references, they both refer to the same list.