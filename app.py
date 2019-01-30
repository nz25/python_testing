# app.py
MENU_PROMPT = '''Enter
"c" to create a blog
"l" to list blogs
"r" to read one
"p" to create a post
"q" to quit
Your selection: '''

blogs = {} # blog_name : Blog object

def menu():

    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)

def print_blogs():
    # Print the available blogs
    for blog in blogs.values():
        print(f'- {blog}')


if __name__ == '__main__':
        menu()