names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [long_name.upper() for long_name in names if len(long_name) > 5]
print(long_names)