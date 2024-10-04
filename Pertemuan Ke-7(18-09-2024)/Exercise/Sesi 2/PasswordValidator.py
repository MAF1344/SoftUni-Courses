password = input()

is_valid = True

# Check if the password length is between 6 and 10 characters
if not (6 <= len(password) <= 10):
    print("Password must be between 6 and 10 characters")
    is_valid = False

# Check if the password consists only of letters and digits
if not password.isalnum():
    print("Password must consist only of letters and digits")
    is_valid = False

# Check if the password has at least 2 digits
digit_count = sum(char.isdigit() for char in password)
if digit_count < 2:
    print("Password must have at least 2 digits")
    is_valid = False

# If all conditions are met, print "Password is valid"
if is_valid:
    print("Password is valid")


# for i in range(48, 58):
#     print(f"{chr(i)}", end=' ')
# print()
# for i in range(65, 91):
#     print(f"{chr(i)}", end=' ')
# print()
# for i in range(97, 123):
#     print(f"{chr(i)}", end=' ')
