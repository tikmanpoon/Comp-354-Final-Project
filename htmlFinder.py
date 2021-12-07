import requests
import os

# The function for the html finding feature
def html_finder():

    # Ask the user what website do they want see the code of
    chosen_url = input("\nEnter the website in which you would like to see the code: ")

    # Create a complete url
    url = "https://www." + chosen_url + ".com"

    print("\nDownloading content of " + url)

    # Request the url and write its source code to a local file called "html_code.tct"
    r = requests.get(url)
    with open('html_code.txt', 'w', encoding='utf-8') as file:
        file.write(r.text)

    print("Writing to file...")
    print("Finished\n")

    ##################################################
    # Test case for html_finder()
    filepath = "./html_code.txt"
    if os.path.isfile(filepath):
        print("File exists. Test Case Successful.")
    else:
        print("File DNE. Test Case Unsuccessful.")
    ##################################################
