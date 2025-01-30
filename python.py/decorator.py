# # def decorator_name(func):
# #     def wrapper(*args, **kwargs):
# #         # Modify or extend functionality here
# #         print("Before the function call")
# #         result = func(*args, **kwargs)
# #         print("After the function call")
# #         return result
# #     return wrapper

# # @decorator_name
# # def my_fun():
# #     print("Inside the function")
# # my_fun()


# class Example:
#     @staticmethod
#     def static_method():
#         return "This is a static method"

#     @classmethod
#     def class_method(cls):
#         return f"This is a class method for {cls}"

#     @property
#     def computed_property(self):
#         return "This is a computed property"

# e = Example()
# print(e.computed_property)









# def memoize(func):
#     cache = {}
#     def wrapper(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]
#     return wrapper


# @memoize
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(10))




def requires_authentication(func):
    def wrapper(user):
        if not user.get("is_authenticated"):
            raise PermissionError("User not authenticated")
        return func(user)
    return wrapper

@requires_authentication
def view_account(user):
    return f"Welcome {user['name']}!"

user = {"name": "Alice", "is_authenticated": True}
print(view_account(user))
