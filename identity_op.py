#identity operator
data="bhavya"
data_1=data
print("data id : ",id(data))
print("data_1 id : ",id(data_1))
print(data_1 is data)
print(data_1 is "std")
print(data_1 is "data")

print("____________")

name="bhanu"
data=name
print("name id : ",id(name))
print("data id : ",id(data))
print(data is not name)
print(data is not "name")
