def custom_christmas_tree(n):
   
    tree = ""
    for i in range(n):
        stars = "*" * (2 * i + 1)
        spaces = " " * (n - i - 1)
        tree += spaces + stars + "\n"

    trunk_space = " " * (n - 1)
    tree += trunk_space + "|" + "\n"

    return tree

print(custom_christmas_tree(6))