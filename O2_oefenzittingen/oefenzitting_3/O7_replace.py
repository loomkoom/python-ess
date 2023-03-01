def replace_substring(replacee, content, replacement):
    """A function that replaces a given substring in a given content string.
    The function must accept the substring as first argument, the content string as second argument,
    and the replacement substring as third argument.
    The function must always return a string.

    Every occurrence of replacee in the content string has to be replaced by replacement.

    HINT: Use text slicing to change the string of replacee by replacement in content similar to:
    content = content[:i] + replacement + content[i + len(replacee):]

    Example output:
        replace_substring('e', "methodiek van de informatica", "a") # returns "mathodiak van da informatica"
        replace_substring('ten', "hottentottententententoonstelling", "stuff") # returns "hotstufftotstuffstuffstuffstufftoonstelling"
    """

    for i in range(len(content)-len(replacee)+1):
        if content[i:i+len(replacee)] == replacee:
            content = content[:i] + replacement + content[i + len(replacee):]
    return content


def replace_kv1(content, key_value_pairs):
    """This function takes a content string and a set of key-value pairs.
    The key-value pairs are always of the form "{key1=value1;key2=value2}"
    The function changes the keys in the content by its corresponding value.

    For example:
        replace_kv("Today will be {{weather-type}}.", "{weather-type=sunny}") # Returns "Today will be sunny."
        replace_kv("His name is {{name}}, he is {{years}} years old.", "{name=John;years=42}") # Returns "His name is John, he is 42 years old."

    HINT: use the substring replacement function that you just made!
        Try to make a while-loop over the length of the key-value pairs string.
        In the loop, identify when you see key, a value, and the start of the next key-value pair.
        Compare the characters "=" and ";" to identify the parts.
        Before the start of the next-key value pair, you can use the previous substring method to do the
        replacement in the content.
    """


    get_key = False
    get_value = False
    key = ''
    value = ''
    for n in range(len(key_value_pairs)):
        char = key_value_pairs[n]

        if char == '{':
            get_key = True
        elif char == '=':
            get_key = False
            get_value = True
        elif char == ';' or key_value_pairs[n] == '}':
            print(content,key + " = " + value, sep = " | ")
            content = replace_substring("{{" + key + "}}", content, value)
            get_key = True
            get_value = False
            key = ""
            value = ""
        elif get_key:
            key += key_value_pairs[n]
        elif get_value:
            value += key_value_pairs[n]
    print(content)
    return content

def replace_kv2(content, key_value_pairs):

    key_start = 1
    value_start = 0
    for n in range(len(key_value_pairs)):
        char = key_value_pairs[n]

        if char == '=':
            key = key_value_pairs[key_start:n]
            value_start = n+1

        elif char == ';' or char == '}':
            value = key_value_pairs[value_start:n]
            key_start = n+1
            print(content,key + " = " + value, sep = " | ")
            content = replace_substring("{{" + key + "}}", content, value)

    print(content)
    return content

#TESTS
assert replace_substring('e', "methodiek van de informatica", "a")== "mathodiak van da informatica"
assert replace_substring('ten', "hottentottententententoonstelling", "stuff") == "hotstufftotstuffstuffstuffstufftoonstelling"
assert replace_substring('e',"ee","ee") == "eeee"
assert replace_substring('e',"eee","eee") == "eeeeeeeee"

assert replace_kv1("Today will be {{weather-type}}.", "{weather-type=sunny}") == "Today will be sunny."
assert replace_kv1("His name is {{name}}, he is {{years}} years old.", "{name=John;years=42}") == "His name is John, he is 42 years old."
print("\n")
assert replace_kv2("Today will be {{weather-type}}.", "{weather-type=sunny}") == "Today will be sunny."
assert replace_kv2("His name is {{name}}, he is {{years}} years old.", "{name=John;years=42}") == "His name is John, he is 42 years old."
