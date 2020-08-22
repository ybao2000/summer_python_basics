s1 = "I am a very happy string"
s2 = "happy python"
s3 = "1234"

# string is a special kind of tuple

c = s1[0]
print(c)

c2 = s1[-1]
print(c2)

# use in to check if a char is in a string
v2 = 'a'
res = v2 in s1
print(res)

# use : to get substring
sub2 = s1[-3: -1]
print(sub2)

# if start is 0, you can omit it
print("-------------")
sub3 = s1[:2]
sub3_2 = s1[2:] # this means go to the end
sub3_3 = s1[3:1:-1]
print(sub3, len(sub3))
print(sub3_2)
print(sub3_3)

# merge 2 string
print(s1+s2)

# multiply
print(s1*3)

###########string is not mutable
# s1[0] = "Y"

# multi-line string
# first way - use triple single-quote
ms = '''slslsls
slslsllsls'''
print(ms)

# second way - use triple double-quote
ms2 = """twinkle twinle little star
how i wonder what you are"""
print(ms2)

########difference between string and tuple: string is comparable
# how is it compared? ---- according to ASCII code
s5 = "char "
s6 = "char"
print(s5 < s6, s5 == s6, s5 > s6)

# string escape
# third way - use single-quote/double-quote and escape (discuss it later)
# different os system has different rules about this: MacOS, Linux (don't use \r)
ms3 = "holy holy holy\r\nmolly molly molly"  # \r - carriage return \n - next line
print(ms3)

# other string escape
# \\ => \, \t => tab, \' => ', \" => "
print("I want \\\\")
print("a\tb\tc")

# I Dont' what ESCAPE
# please use r to avoid escape (raw)
# similar to f (format)
filepath = r"D:\ABAITC\Courses\Python Basics\summer_camp\temp"
print(filepath)

# unicode
s_chinese = "中国"
print(s_chinese)
print("\u4E2D\u56FD")

# chemark
print("\u2715, \u2705")