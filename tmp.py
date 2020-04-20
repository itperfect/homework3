class Some:

    def __init__(self, initial = None):
        self.value = initial

    def getVal(self):
        return self.__dict__['value']

    def __setattr__(self, key, new_value):
        if key == 'value' and (key not in self.__dict__ or self.__dict__[key] == None):
                self.__dict__[key] = new_value
        else:
            print("U can't do it")


obj = Some()

obj.value = 2

obj.value = 3

print(obj.value)
