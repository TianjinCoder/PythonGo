
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print('decorated')
        if not can_run:
            return "Function will not run"
        print('decorated will return the function')
        return f(*args, **kwargs)
    print('wraps end')
    return decorated
 
@decorator_name
def func():
    return("Inner function is running")
 
can_run = True
print(func())
# Output: Function is running
 
can_run = False
print(func())
# Output: Function will not run