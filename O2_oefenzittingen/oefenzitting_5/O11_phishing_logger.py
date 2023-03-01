"""
   we consider unsafe browsing to happen:
   when I type the same password, into a site that is the same length as another, but differs by exactly one character

  """

safebrowsingsession1 = {"google.com": "abc123", "youtube.com": "another_password"}
safebrowsingsession2 = {"google.com": "abc123", "goagle.com": "abc124"}
unsafebrowsingsession = {"google.com": "abc123", "goagle.com": "abc123"}


## checkt of een wachtwoord meerdere keren gebruikt wordt

# def check(website_pw):
#     passwords = website_pw.values()
#     for pw in passwords:
#         if list(passwords).count(pw) > 1:
#             return "unsafe"
#     return "safe"
def check_one_letter_diff(word1, word2):
    """
    We check whether the domain names differ by exactly one character
    """
    difference = False
    if len(word1) == len(word2):
        for i in range(len(word1)):
            print(word1[i],word2[i])
            if word1[i] != word2[i]:
                if difference:
                    return False
                difference = True
    return difference


def check(website_pw):
    """
    we check whether the logging session should be considered safe or not
    """
    keys = website_pw.keys()
    for key_1 in keys:
        for key_2 in keys:
            if key_1 != key_2 and (website_pw[key_1] == website_pw[key_2]):
                if check_one_letter_diff(key_1, key_2):
                    return "unsafe"
    return "safe"


assert (check(safebrowsingsession1)) == "safe"
assert (check(safebrowsingsession2)) == "safe"
assert (check(unsafebrowsingsession)) == "unsafe"
