import random

# Find Min
# Find Max
# Squeeze Sort

data = [1,23,4,41,32,21,12,14,2]
print(data)
random.shuffle(data)  # Randomly shuffle the data

def FindMin(data):
    # if empty, return
    # loops through data
    # if data[i] < min, set min = data[i]
    # return min
    for i in range(1, len(data)):
        min = data[0]
        if data[i] < min:
            #print(min)
            min = data[i]
    return min 

print(FindMin(data))


x = ["a", "b", "c", "d"]
dd = {}
for i in x:
    dd[i] += -1
print(dd)






# def SqueezeSort(data, size):
#   # data: array to be sorted
#   # size: number of elements in data
#   #
#   pass



# def functionname():
#     # This is a function that does nothing
#     pass




# # List (Mutable)
# thislist = [2,34,1] , d = dict{} , tuple(), str = "fbwuifubiwq"
# thislist[0]             # Get list's element, index 0 - element 1 a[index]
# thislist  = list(range(1:10))
# thislist = [x for x in fruits]
# thislist = [x if x != "banana" else "orange" for x in fruits]; makes Banana -> Orange
# thislist = list(("apple", "banana", "cherry")) 
# thislist = [], use .append() to add
# thislist = [None] * 10
# '''
# ",".join(Iterable of strings), insert "," between elements, returns string
# .append(object) - 1 required argument. Append object to list at the end
# .insert(1, object) - 2 required argument. Insert object at position and cascade the rest
# .extend(iterable) - 1 required argument. Append iterable (list) to list at the end
# del a[1] # Deletes the element at index 1. Otherwise, raises IndexError if index is out of range
# a.remove(2) # Removes the first occurrence of 2. Otherwise, raises ValueError if not found
# a.pop(2) # Removes the element at index 2, which is 3. Otherwise, removes last element
# a.clear() # Removes all elements from the list
# '''







# # Dict (Mutable)
# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "food": ["apple", "banana"]
# }
# # Get Value
# my_dict.get("email", _value to return if key not found; default to None_)
# my_dict["email"]
# my_dict["steps"][1] # 2nd element in "Steps" Key
# # Remove
# del my_dict["key"]
# # Add
# my_dict["new_key"] = new_value
# my_dict.update({"new_key" : new_value }) # Useful for adding multiple key-value
# my_dict.setdefault("new_key", new_value) # Add if key doesn’t exist, otherwise return current value
# # Update
# my_dict[7] = 3 – method 1 to update 
# my_dict["key"] = “Jane” 
# my_dict.update({7:3}) – method 2 to update 
# # Loop
# for key in my_dict: 
#     print(key, my_dict[key])
# for key, value in my_dict.items() : 
#     print (key, value) 
# listkey = list(my_dict.keys())      # Get all keys
# listvalue = list(my_dict.values())  # Get all values
# for i, pair in enumerate(my_dict): 
# # Tuple Unpacking
# key, value = pair[0], pair[1]
# (key,value) = pair 



# # String (Immutable)
# letters = "abcdefgh"
# letters = "abcdefgh"[0:3]  # Slicing
# letters[2] = "s"           # Error, strings are immutable


# # Tuple (Immutable)
# x = list(enumerate([1, 2, 3, 4])); # List of Tuple
# x = (1, 2, 3)  # Tuple
# listx = list(x)       # Convert Tuple to List
# listx.append(1)       # Tuple with 4 elements
# listx.extend([4, 5])  # Extend List with more elements
# x = tuple([1, 2, 3])  # Convert List to Tuple


# int()            # Method & Function
# customfoo()      # Call function



# aclass.property  # Access property 



# # Troubleshooting
# '''
# - print the output step by step to see
# - TypeError: int + str, cannot concatenate str to int
# - ValueError
# - AttributeError
# - IndexError
# - KeyError
# '''

# A = [1, 2, 3, 4, 5]
# for i in range(len(A)):
#     if A[i] > A[i + 1]:
#         #WRONG #i, i+1 = i+1, i  # Tuple Unpacking. Swap elements if A[i] > A[i + 1]
#         #print(A[i], A[i + 1])  # Print elements before swapping
#         A[i], A[i + 1] = A[i + 1], A[i]  # Swap elements in list



# class parentClass:
#     # def __init__(self):
#     # def __init__(self, value):
#     def __init__(self, value = "1"):
#         self.id_ = value
#         self._stored_property = value    # Getter and Setter
#         self._computed_property = value  # Only Getter

#         self._private_attribute = value  # Private attribute

#     @property # Getter 
#     def stored_property(self):
#         return self._stored_property
    
#     @stored_property.setter  # Setter for stored_property attribute
#     def stored_property(self, value):
#         self._stored_property = value
    

#     @property # Getter
#     def computed_property(self):
#         self._computed_property = self.id_ * 2
#         return self._computed_property
    
#     @computed_property.setter  # Setter for computed_property attribute
#     def computed_property(self):
#         raise ValueError("computed_property is read-only and cannot be set")

#     # Method
#     def customfunction(self, value: int, value2: int):
#         # does computation using class' variables/attributes
#         return value + value2

#     def move(self, input: int):
#         x = input + 1
#         y = x * 2
#         return y

#     # Special Method
#     def __str__(self):
#         return f"parentClass(id_={self.id_}, stored_property={self.stored_property})"





# # Step 2 Create Object Instance of parentClass
# aclass = parentClass()
# pclass = parentClass(10)

# # Step 3 Accessing attributes and methods
# #print("ID:", aclass.id_) POINTLESS
# print("Stored Property:", aclass.stored_property)      # CLASSNAME.GETTER
# pclass.stored_property = 20                            # CLASSNAME.GETTER = // to assign & call setter

# print("computed Property:", pclass.computed_property)  # CLASSNAME.GETTER
# pclass.computed_property = "something"                 # This will not work, as computed_property is read-only

# output = pclass.customfunction(5, 10)                  # Call method with parameters






# # Composition 
# class HasA:
#     def __init__(self, value: int = 1) -> None:
#         self.id_ = value                # self.id_ is int type

#         # Create Object Instance of parentClass INSIDE another class
#         self._child = parentClass(value) # parentClass object (child) & Attribute HasA

#     @property
#     def child(self):
#         return self._child
    
#     @child.setter
#     def child(self, value):
#         self._child = value

#     def __str__(self):
#         return f"HasA(id_={self.id_}, child={self.child})"


# sclass = HasA()
# print(sclass.child) # based on __str__ in HasA()
# sclass.child = 30

# print(sclass.child.customfunction)  # COMP_CLASSNAME.ATTRIBUTE_L170.METHOD_FROM_PARENT_CLASS
# sclass.child.stored_property = 40



# class IsA(parentClass):
#     def __init__(self, value = 1, add_value2 = 1) -> None:
#         super().__init__(value)
#         self.id_ = add_value2       # New attribute for IsA class

#     def attack(self):               # Method defined in child class
#         pass
    

#     def move(self):                 # Overrides parentClass move method
#         pass

#     def move(self, input):          # Extends move method of ParentClass
#         super().move(input)
#         y = x * 4 # Overwrites old y
#         y = y + 2 # Does new stuff
#         return y

# # IsA class object is an instance of parentClass

# RT = IsA()
# RT.move()         # inherited from parent
# RT.attack()       # defined in child


# '''
# __init__ method with attributes name and age, 
# has_y_chromosome set to None and cannot be changed after initalisation

# methods
# - name and age has getter-setter
# - is_adult, more then 18
# - has_y_chromosome() - returns True if has_y_chromosome is True, False otherwise
# - __lt__, by age
# - __gt__, by age
# - __eq__, by all attributes
# '''

# class human:






















# '''
# f(n) = approx math expression of code time, x^2 + x + 10
# g(n) = bound, x^2, x
# as input increases (n = input)

# Theta: Strictly upper and lower bound. Strictly growing at the same rate as g(n)
# Where f = x^2, as n increases
# x^2 = Theta(x^2), 

# Big-O: Upper Bound, grows at most as fast as g(n)
# Where f = x^2, as n increases
# f(n) <= g(n)
# x^2 = O(x^2),



# Calculating Computation Time without experimental code running

# Single Line Operation = Q(1)
# if __: = Q(1) 
# while (i < 20) = Q(1) x (whatever nested)
# for i in range(20) = Q(1) x (whatever nested)


# for _ in range(n) = Q(n) x (whatever nested); _ denotes unused variable
# while (i < n) = Q(n) x (whatever nested)
# for i in range(n) = Q(n) x (whatever nested)

# for I in range(3*n**2) = Q(n^2) x (whatever nested)
# for I in range(3*n**3) = Q(n^3) x (whatever nested)
# for I in range(3**3) = Q(1) x (whatever nested)

# while () binary tree = O(log2(n)) x (whatever nested)

# Constant Time: 
# 	- O(1)
# 	- 2 x O(1) x O(1) = O(1) 
# 	- Add, simplifies
# 		- Q(1) + Q(n)  = Q(n)
# 		- Q(1) + Q(1) = Q(1)
# 		- O(nlog(n))+O(nlog(n)) = O(nlog(n))
# 	- Multiple, Always priotise O(n)
# 		- O(1) x O(n) = O(n)
# 		- O(n/2) = O(n)
# O(n) x O(n) = O(n^2)



# for i in range(n):
#     print(i)
#     for i in range(n):
#         print()
# Q(n) ( Q(1) + Q(N) * Q(1) ) = Q(n^2)

# '''


# # Recursion

# def factorial(n):
#     # Base Case: Terminating
#     if n == 0 or n == 1:
#         return 1
    
#     # Recursive Case: Call the function itself + reduce the probl3m

#     # Tree Recrusion: O(e^n)
#     else:
#         factorial(n-1)
#         factorial(n-1)
#         pass

#     # Simple Recursion: O(n)
#     else:
#         return n * factorial(n - 1)  # Recursive call with reduced problem size

#     #  Binary Recursion: O(log n)
#     else:
#         for i in range(n): # with this, it will be O(nlogn)
#             pass
#         return n * factorial(n - 1) + factorial(n - 2)  # M1: Recursive call with two branches
#         return factorial(n//2)                          # M2: Recursive call with one branch, halving the problem size
    

