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


#Decorators:
# https://www.geeksforgeeks.org/decorators-in-python/?ref=header_ind

def decorator(func):
  
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator
def greet():
    print("Hello suri")
greet()
