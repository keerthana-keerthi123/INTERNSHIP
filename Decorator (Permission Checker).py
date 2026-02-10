# Decorator
def admin_only(func):
    def wrapper(username):
        if username == "admin":
            return func(username)
        else:
            print("Access Denied")
    return wrapper

# Function with decorator
@admin_only
def dashboard(username):
    print(f"Welcome {username}, this is the dashboard.")

# Test
dashboard("admin")   # Works
dashboard("guest")   # Access Denied
