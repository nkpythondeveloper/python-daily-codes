# To reverse a string

# By slicing method
def reverse_string_slicing(given_str):
    return given_str[::-1]

# By Extra Space
def reverse_string_extra(given_str):
    extra = []
    n = len(given_str)
    for i in range(n-1,-1,-1):
        extra.append(given_str[i])
    return ''.join(extra)

if __name__ == "__main__":
    given_string = "Hello World!"
    print(reverse_string_slicing(given_string))
    print(reverse_string_extra(given_string))

"""
Output
>>> !dlroW olleH

:: CONCEPT -> Slicing
[start:stop:step]
start - inclusive
stop - non inclusive
step - move by how many

Here we are using [::-1] -> nothing:nothing:-1


>>> !dlroW olleH

:: CONCEPT -> Extra Space
Here we are iterating over the given string from end to the start,
appending each element to a new extra space[list], 
then returning a ''.join on that extra space.

"""