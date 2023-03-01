# Create string literal with the first lines of Shakespeare's Macbeth
macbeth_text = " When shall we three meet again, In thunder, lightning or in rain? \n" \
               "When the hurleyburley's done, When the battle's lost and won.\n" \
               "That will be ere the set of sun.\n" \
               "here the place?\n" \
               "Upon the heath.\n" \
               "There to meet with Macbeth.\n" \
               "A cacophany of bloodcurdling yelps and inhuman screams, cutting through the noise of the storm.\n" \
               "I come, Graymalkin!\n" \
               "Paddock calls.\n" \
               "Lightning momentarily reveals three deformed shapes linking hands in a grotesque dance.\n" \
               "Fair is foul, and foul is fair: Hover through the fog and filthy air.\n" \
               "A mighty crash of thunder, a terrifying whiteness, then darkness and silence."

# Print the text
print("\nOriginal text")
print("=============\n")
print(macbeth_text + "\n")

# Ask the user for a name and replace "Macbeth" with that name
name = input("Please type a name: ")
macbeth_text = macbeth_text.replace("Macbeth",name)

# Print the modified text
print("\nModified text")
print("=============\n")
print(macbeth_text)
