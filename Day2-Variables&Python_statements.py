# Variables & Python Statements

import keyword
import this
import os
import random
import math

dir(os)
['DirEntry',
 'F_OK',
 'GenericAlias',
 'Mapping',
 'MutableMapping',
 'O_APPEND',
 'O_BINARY',
 'O_CREAT',
 'O_EXCL',
 'O_NOINHERIT',
 'O_RANDOM',
 'O_RDONLY',
 'O_RDWR',
 'O_SEQUENTIAL',
 'O_SHORT_LIVED',
 'O_TEMPORARY',
 'O_TEXT',
 'O_TRUNC',
 'O_WRONLY',
 'P_DETACH',
 'P_NOWAIT',
 'P_NOWAITO',
 'P_OVERLAY',
 'P_WAIT',
 'PathLike',
 'R_OK',
 'SEEK_CUR',
 'SEEK_END',
 'SEEK_SET',
 'TMP_MAX',
 'W_OK',
 'X_OK',
 '_AddedDllDirectory',
 '_Environ',
 '__all__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_check_methods',
 '_execvpe',
 '_exists',
 '_exit',
 '_fspath',
 '_get_exports_list',
 '_walk',
 '_wrap_close',
 'abc',
 'abort',
 'access',
 'add_dll_directory',
 'altsep',
 'chdir',
 'chmod',
 'close',
 'closerange',
 'cpu_count',
 'curdir',
 'defpath',
 'device_encoding',
 'devnull',
 'dup',
 'dup2',
 'environ',
 'error',
 'execl',
 'execle',
 'execlp',
 'execlpe',
 'execv',
 'execve',
 'execvp',
 'execvpe',
 'extsep',
 'fdopen',
 'fsdecode',
 'fsencode',
 'fspath',
 'fstat',
 'fsync',
 'ftruncate',
 'get_exec_path',
 'get_handle_inheritable',
 'get_inheritable',
 'get_terminal_size',
 'getcwd',
 'getcwdb',
 'getenv',
 'getlogin',
 'getpid',
 'getppid',
 'isatty',
 'kill',
 'linesep',
 'link',
 'listdir',
 'lseek',
 'lstat',
 'makedirs',
 'mkdir',
 'name',
 'open',
 'pardir',
 'path',
 'pathsep',
 'pipe',
 'popen',
 'putenv',
 'read',
 'readlink',
 'remove',
 'removedirs',
 'rename',
 'renames',
 'replace',
 'rmdir',
 'scandir',
 'sep',
 'set_handle_inheritable',
 'set_inheritable',
 'spawnl',
 'spawnle',
 'spawnv',
 'spawnve',
 'st',
 'startfile',
 'stat',
 'stat_result',
 'statvfs_result',
 'strerror',
 'supports_bytes_environ',
 'supports_dir_fd',
 'supports_effective_ids',
 'supports_fd',
 'supports_follow_symlinks',
 'symlink',
 'sys',
 'system',
 'terminal_size',
 'times',
 'times_result',
 'truncate',
 'umask',
 'uname_result',
 'unlink',
 'unsetenv',
 'urandom',
 'utime',
 'waitpid',
 'waitstatus_to_exitcode',
 'walk',
 'write']

dir(random)
['BPF',
 'LOG4',
 'NV_MAGICCONST',
 'RECIP_BPF',
 'Random',
 'SG_MAGICCONST',
 'SystemRandom',
 'TWOPI',
 '_Sequence',
 '_Set',
 '__all__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_accumulate',
 '_acos',
 '_bisect',
 '_ceil',
 '_cos',
 '_e',
 '_exp',
 '_floor',
 '_inst',
 '_log',
 '_os',
 '_pi',
 '_random',
 '_repeat',
 '_sha512',
 '_sin',
 '_sqrt',
 '_test',
 '_test_generator',
 '_urandom',
 '_warn',
 'betavariate',
 'choice',
 'choices',
 'expovariate',
 'gammavariate',
 'gauss',
 'getrandbits',
 'getstate',
 'lognormvariate',
 'normalvariate',
 'paretovariate',
 'randbytes',
 'randint',
 'random',
 'randrange',
 'sample',
 'seed',
 'setstate',
 'shuffle',
 'triangular',
 'uniform',
 'vonmisesvariate',
 'weibullvariate']

dir(math)
['__doc__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'acos',
 'acosh',
 'asin',
 'asinh',
 'atan',
 'atan2',
 'atanh',
 'ceil',
 'comb',
 'copysign',
 'cos',
 'cosh',
 'degrees',
 'dist',
 'e',
 'erf',
 'erfc',
 'exp',
 'expm1',
 'fabs',
 'factorial',
 'floor',
 'fmod',
 'frexp',
 'fsum',
 'gamma',
 'gcd',
 'hypot',
 'inf',
 'isclose',
 'isfinite',
 'isinf',
 'isnan',
 'isqrt',
 'lcm',
 'ldexp',
 'lgamma',
 'log',
 'log10',
 'log1p',
 'log2',
 'modf',
 'nan',
 'nextafter',
 'perm',
 'pi',
 'pow',
 'prod',
 'radians',
 'remainder',
 'sin',
 'sinh',
 'sqrt',
 'tan',
 'tanh',
 'tau',
 'trunc',
 'ulp']

os.listdir
<function nt.listdir(path=None)>

os.listdir()
['.git',
 '.ipynb_checkpoints',
 'Day1.py',
 'Day2- Variables and Python Statements.ipynb',
 'README.md']

math.sqrt(25)
5.0

random.choice([1,3,6,9,15])
9
a = 5
b = 10
c = a + b

print(c)
15

b = "hello"
print(b)
hello

import keyword
print(keyword.kwlist)
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

dir(keyword)
['__all__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'iskeyword',
 'issoftkeyword',
 'kwlist',
 'softkwlist']

for number in [1,2,3,4]:
    print(number**2)
1
4
9
16

import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

'''Plugging in variables into a string: String Formatting
#Task: write a program that asks for a user's name and the city where they live. 
#Then return a message to the user and tell them that they are welcome, and that you like their city.'''

name = input("please, enter your name: ")
city = input("Enter the name of your city: ")
income = input("Enter your income: ")

please, enter your name: Phyllis
Enter the name of your city: Memphis
Enter your income: 450
name = input("please, enter your name: ")
city = input("Enter the name of your city: ")
income = input("Enter your income: ")

print(f"Hi {name}, Welcome to Landmark. I like your city, {city}")
print(f"If we double your income, it will be {income*2}")

please, enter your name: peter
Enter the name of your city: cityA
Enter your income: 345

Hi peter, Welcome to Landmark. I like your city, cityA
If we double your income, it will be 345345

# note that everything collected with input is 
# interpreted as a string
# 5*2 is not the same as "5"*2

5*2
10

"5"*2
'55'

eval("5")*2
10

print(f"Hi {name}, Welcome to Landmark. I like your city, {city}")
print(f"If we double your income, it will be {eval(income)*2}")

Hi peter, Welcome to Landmark. I like your city, cityA
If we double your income, it will be 690

print("Hi {0}, Welcome to Landmark. I like your city, {1}".format(name,city))
Hi peter, Welcome to Landmark. I like your city, cityA

print("Hi {}, Welcome to Landmark. I like your city, {}".format(name,city))
Hi peter, Welcome to Landmark. I like your city, cityA

print("Hi {0}, Welcome to Landmark. I like your city, {0}".format(name,city))
Hi peter, Welcome to Landmark. I like your city, peter

print("Hi {1}, Welcome to Landmark. I like your city, {1}".format(name,city))
Hi cityA, Welcome to Landmark. I like your city, cityA


# library==> package==> file(modules)==> statement(unit of code)==> expressions
#examples of expressions
'''
- a numeric literal:
    - 5
- string literal:
"green"
- a variable: should already be created:
age
- a combination of values
10 + 5
'''
# Assignment statement:
'''a statement that has an equals to (=) sign
name = "John" is an assignment statement where value john is assigned to variable called name.'''

#forms of assignment statements
'''a basic assignment statement:
name = "john"
tuple assignment - positional:
name, city = "john", "Texas"
list assignment - positional:
[name, city] = ["john", "Texas"]
sequence assignment - general
x = y = z = 10
extended sequence unpacking
a * b = [1,2,3,4,5]'''

# tuple assignment:
(name, age, city) = ("mary", "15", "Lakeway")
print(name)
mary

print(city)
Lakeway

name, age, city = "mary", "15", "Lakeway"
print(age)
15

#list assignment
[age, city] = [14, "kiambu"]
print(city)
kiambu

# sequence assignment:
x = y = z = 18
print(z)
18

# extended sequence unpacking: x = 1, z = 2, y = 3,4,5
x, z, *y = [1,2,3,4,5]
print(y)
[3, 4, 5]

print(z)
2

print(x)
1

# augmented statements:
x = 10
print("first x: ", x)
x = x + 5

print("second x: ", x)
first x:  10
second x:  15

x = x + 5
print("second x :", x)
second x : 20

# implicit statement (for for loops)

print()

#for autocompletion "shift+tab"

# sep="" (separator)

print("hello", "world")
hello world

print("hello", "world", sep="")
helloworld

print("hello", "world", sep=" ")
hello world

print("hello", "world", sep=",,,,")
hello,,,,world

print("hello", "world", sep="...")
hello...world

# end = separate lines
print("hello", "world", sep="...")
print("hello", "world", sep="...", end="")
hello...world
hello...world

print("hello", "world", sep="...", end="")
print("hello", "world", sep="...", end="")
hello...worldhello...world

print("hello", "world", sep="...", end=" ")
print("hello", "world", sep="...", end=" ")
hello...world hello...world 

print("hello", "world", sep="...", end=" ahahahaha ")
print("hello", "world", sep="...", end="")
hello...world ahahahaha hello...world
 
 
 
 