from pathlib import Path
# Absolute Path
# Relative Path
# Path()#if parameters aren't passed its referred to current directory
# path = Path("ecommerce")
# print(path.exists())
# print(path.is_dir())

# path = Path("newDir1")
# print(path.mkdir())
# print(path.rmdir())

# path=Path()
# print(path.glob('*.*'))#with this we can search directories in the current path
# *.* gives all files in the current directory
# print(path.glob('*.py')) # searches all the .py files
# these returns generator objects
# for file in path.glob('*.py'):
#     print(file)

#fiels and directories in current part
# for file in path.glob('*'):
#     print(file)