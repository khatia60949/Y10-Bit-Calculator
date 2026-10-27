# asks users for file type (integer / image / text / xxx)
def get_filetype():

    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check if it's a text
        elif response in ['text', 't', 'txt']:
            return "text"

        # check if it's an image
        elif response in ['image', 'p', 'img']:
            return "image"

        # if the response is invalid, output an error
        else:
            print("Please enter a valid file type")


# Main routine goes here
while True:
    file_type = get_filetype()

    # if user chose 'i', ask if they want an image / integer
    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"You chose {file_type}")

    if file_type == "xxx":
        print("Thank you for using the bit calculator")
        break
