class User:
    def __new__(cls, name, age):
        print("__new__ called")
        # create the new empty instance (very rarely customized in practice)
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, age):
        print("__init__ called")
        self.name = name
        self.age = age

    def __str__(self):
        return f"User(name={self.name}, age={self.age})"


u1 = User("Alice", 25)
print(u1)