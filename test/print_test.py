print("Apple", "Banana", "Pear", "Peach", sep=", ", end=" are fruit")
print()

a = 4
b = "Frank"
c = "True"

# concatenate way
print("a is", a, ",b is", b, ",c is",  c)

# format way --- a lot of developers are still using it, but it's deprecated, becuase there are better to do it
# format of "3d" -- only for int, means when convert int to string, it will add leading space
print("a is {0:3d}, b is {1}, c is {2}".format(a, b, c))
a = 444
b = "Frank"
c = "True"
print("a is {0:3d}, b is {1}, c is {2}".format(a, b, c))

# f-string is a better (only available after version 3.6)
# f-string (format string)
print(f"a is {a:3d}, b is {b}, c is {c}")

# what is r-string (raw string)
print(r"a is {a:3d}, b is {b}, c is {c}")