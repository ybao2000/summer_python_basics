# recursive means inside a function, the same function was called

# function is a template

# string, substring
# recursive
def foo(text):  # this is the definition
  if not text:  # this is a stopper (means no longer call itself)
    return
  # print(text)
  print(text[0])
  foo(text[1:]) # we have a call to the same function, text[1:]

foo("Hello World")  # this is the code to call function foo

