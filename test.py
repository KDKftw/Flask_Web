instance = "Instance: Whenever we create a new object we are said to be creating an instance of a class. For example typing the command x = 1 translates to: creating a new instance of the int class with the value 1 and the name x."
method = "Method: You can think of a method as a function that is specific to certain objects and classes. Methods are created within a class and are only visible to instances of that class. An example of a method is .strip(). It can only be used on objects of class str as it is specific to the str class. All methods must be called on an instance of a class. We cannot simply type strip() as we need to include an instance followed by a period before it."
atributes = "Attributes: An attribute is anything that is specific to a certain object. For example the object has an attribute color. We can change that color and modify it and if we create a new turtle object it can have a different color."
paraList = [instance, method, atributes]
print(paraList[1])