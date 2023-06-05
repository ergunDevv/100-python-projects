
# Args syntax
# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return print(total)


# add(2, 4, 5, 6)

# kwargs syntax
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# calculate(1, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.make)
