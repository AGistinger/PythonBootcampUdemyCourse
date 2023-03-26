import zipfile
import re
import os

# Extract Zipfile for Instructions
zip_obj = zipfile.ZipFile("unzip_me_for_instructions.zip", "r")
zip_obj.extractall("Instructions")

# Open each file and search for a phone number
regex_phone = r"\d{3}-\d{3}-\d{4}"
folder_names = ["One", "Two", "Three", "Four", "Five"]
folder_loc = "C:\\Users\\gistadr\\Documents\PythonUdemyBootcamp\\AdvancedModulesPuzzle\\AdvancedModulesPuzzle\\Instructions\\extracted_content"


# Create function to search through folders and files and return the phone number
def find_phone_num(folders, loc, regex):
    phone_numbers = []

    # Go into each individual folder location
    for folder in folders:
        folder_loc = loc + "\\" + folder
        dir_list = os.listdir(folder_loc)

        # Go into each file in the folder
        for file in dir_list:
            file_loc = folder_loc + "\\" + file
            file = open(file_loc, "r")
            file_string = file.read()

            # Search the strings in the text for a phone number
            if re.search(regex, file_string):
                phone_number = re.search(regex, file_string)
                phone_numbers.append(phone_number.group())

            # Close file when not used
            file.close()

    # Return all phone numbers found in files
    return phone_numbers


# Function to print out a list of items found
def print_list(item_list):
    for item in item_list:
        print(f"Phone Number: {item}")


phone_numbers = find_phone_num(folder_names, folder_loc, regex_phone)
print_list(phone_numbers)
