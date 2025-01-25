class Example:
    def __init__(self):
        self.protected_attr = "I am protected example"
    def get_attr(self):
        return self.protected_attr

class AnotherExample(Example):
    def __init__(self):
        super()
        self.protected_attr = "I am protected another example"
    def get_attr(self):
        return self.protected_attr


example = Example()
anotherExample = AnotherExample()
print(example.protected_attr)
print(anotherExample.protected_attr) 