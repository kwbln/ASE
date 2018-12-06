class MyClass:
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.name = name