# app.py

blogs = {} # blog_name : Blog object

def menu():

    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()

def print_blogs():
    # Print the available blogs
    for blog in blogs.values():
        print(f'- {blog}')

