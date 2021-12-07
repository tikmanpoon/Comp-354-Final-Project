from googlesearch import search
import pandas as pd
import os

def link_finder():
    # Ask for the input
    query = input("What do you want to search?")

    # Get the top 10 links of the searching result
    link_file = []
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        link_file.append(j)

    # Creating a csv file template
    link_csv = pd.DataFrame({
        'link_file:': link_file
    })

    print("\nProcessing.....")
    print("\n...")
    print("\nDone")
    # Output the file
    link_csv.to_csv('listOfLinks.csv')

    ##################################################
    # Test case for linkFinder()
    filepath = "./listOfLinks.csv"
    if os.path.isfile(filepath):
        print("File exists. Test Case Successful.")
    else:
        print("File DNE. Test Case Unsuccessful.")
    ##################################################
