# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
        print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
- Enter the type of file you want to calculate (text, image, integer)
- Enter the integer/width & height/text you want to calculate
- Type 'xxx' to end the program
     ''')


# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
        instructions()

print("program continues")
