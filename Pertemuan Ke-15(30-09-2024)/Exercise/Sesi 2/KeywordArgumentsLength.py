def kwargs_length(**kwargs):
  return len(kwargs)

# Example Test Code 1
dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))

# Example Test Code 2
dictionary = {}
print(kwargs_length(**dictionary))