print("password strength checker\n")
password = input ("enter your password:")

unique_chars= set(password)

unique_count = len(unique_chars)
length = len(password)
print("\nanalyzing password....\n")
print("password length:", length)
print("unique characters", unique_count)

if unique_count < 3:
    print("password is short")
elif unique_count <= 6:
    print("too short")
elif unique_count <= 10:
    print("medium length")
else:
    print("long password")
