"""To complete this kata you need to be able to define a class that implements
__getitem__(), __str__(), __repr__(), and possibly __len__()."""


class Test(object):

    # This function prints the type
    # of the object passed as well
    # as the object item
    def __getitem__(self, items):
        print(type(items), items)
test = Test()
test[5]
test[5:65:5]
test['GeeksforGeeks']
test[1, 'x', 10.0]
test['a':'z':2]
test[object()]

messages = Test()
messages[1, 2, 3, 4, 5]   # prints "my messages are: [1,2,3,4].
# print(messages)
# base=[1,2,3,4]
# a=SecureList(base)