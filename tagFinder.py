from bs4 import BeautifulSoup
import requests


def tag_finder():
    # Assign URL by asking the child for input
    chosen_url = input("Enter the website in which you would like to see the HTML elements for: \n")

    # Make a complete url
    url = "https://www." + chosen_url + ".com"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content using any parser
    soup = BeautifulSoup(html_content, "html.parser")

    # List to store types of tags and number of tags
    tag_names = []
    tag_names_without_duplicate = []
    tag_count = []

    # Store all tags into the list tag_names
    for tag in soup.find_all():
        tag_names.append(tag.name)

    # Take out all the duplicate tag names
    tag_names_without_duplicate = list(dict.fromkeys(tag_names))

    # Count the occurrence for each tag
    for tag in tag_names_without_duplicate:
        count = tag_names.count(tag)
        tag_count.append(str(count))

    # Print the result of each tag
    for i in range(len(tag_names_without_duplicate)):
        print("'" + tag_names_without_duplicate[i] + "' appeared " + tag_count[i] + " times")

    # Set and print total types and numbers of tags
    total_types_of_tags = str(len(tag_names_without_duplicate))
    total_number_of_tags = str(len(tag_names))

    print("\n" + total_types_of_tags + " types of tags are founded")
    print(total_number_of_tags + " tags are founded in total.\n")





