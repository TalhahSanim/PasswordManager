# Define encryption function
def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 66)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

# Define decryption function
def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char
    return result


# Main program
while True:
    shift = 5  # define shift outside if statement

    # Print welcome message and menu options
    print("Welcome to DigiCore Password Manager")
    print("This program is designed to create, save and secure passwords")
    print("")
    print("Options")
    menu = input("Would you like to save a new password or view existing ones? "
                 "\n1. Input a new password"
                 "\n2. View passwords"
                 "\n3. Help"
                 "\n4. Exit\n")

    if menu == '1':
        # Prompt user for software name, username, and password
        SoftwareName = input("Enter the software name: ")
        Username = input("Enter the username for this software: ")
        Password = input("Enter your password for this software: ")

        # Open file in append mode and write encrypted data
        #Print Password is saved successfully
        file = open("securePasswordData.txt", "a")
        file.write(
            encrypt(SoftwareName, shift) + ";|" + encrypt(Username, shift) + ";|" + encrypt(Password, shift) + "\n")

        print("Password saved successfully.")

        # Close the file
        file.close()

    elif menu == '2':
        # Open file in read mode and print decrypted data
        file = open("securePasswordData.txt", "r")
        print("Software\tUsername\tPassword")
        for i in file:
            data = i.strip().split(";|")
            if len(data) < 3:
                continue
            decrypted_software = decrypt(data[0], shift)
            decrypted_username = decrypt(data[1], shift)
            decrypted_password = decrypt(data[2], shift)
            print(decrypted_software + "\t\t" + decrypted_username + "\t\t" + decrypted_password)

        # Close the file
        file.close()

    elif menu == '3':
        # Print help menu
        print("Press 1 to input a password to save a new password to the system")
        print("Press 2 to view currently saved passwords")
        print("Press 3 to get help")
        print("Press 4 to exit the system")

    elif menu == '4':
        # Print goodbye message and exit the System
        print("Goodbye!")
        break

    else:
        # Print error message for incorrect input
        print("Invalid choice. Please try again.\n")

    # Prompt user to press enter to continue
    input("Press Enter to continue...")
