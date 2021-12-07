import os
import requests
from bs4 import BeautifulSoup

# We will be using google as the search engine
Search_Target = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

# the header
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

# The folder that will store the photos we will download
Folders_of_Images = 'Images_1'


def main():
    save_images_to_pc()


def save_images_to_pc():
    # check if folder to store exist, if not, create one
    if not os.path.exists(Folders_of_Images):
        os.mkdir(Folders_of_Images)

    # ask the user for what to search and how many images do they want
    target = input('What images do you want to search? ')
    numbers_of_images_wanted = int(input('How many images do you want? '))

    print('Searching For Images....')

    # create the url with the target entered by user
    search_url = Search_Target + 'q=' + target

    # request the url with the header
    response = requests.get(search_url, headers=head)
    html = response.text  # To get actual result i.e. to read the html data in text mode

    # find all img tag where class='rg_i Q4LuWd'
    soup = BeautifulSoup(html, 'html.parser')  # html.parser is used to parse/extract features from HTML files
    results = soup.findAll('img', {'class': 'rg_i Q4LuWd'})

    # extract the links of requested number of images and append those links to a list
    counter = 0
    imagelinks = []
    for result in results:
        try:
            link = result['data-src']
            imagelinks.append(link)
            counter = counter + 1
            if counter >= numbers_of_images_wanted:
                break

        except KeyError:
            continue

    print(f'Found {len(imagelinks)} images')
    print('Start downloading to PC...')

    # open the image links and save them to the folder
    for i, imagelink in enumerate(imagelinks):
        response = requests.get(imagelink)

        imagename = Folders_of_Images + '/' + target + str(i + 1) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)

    print('Download Finished!\n')

    ##################################################
    # Test case for pic_finder()
    if os.path.exists('Images_1'):
        print("File exists. Test Case Successful.")
    else:
        print("File DNE. Test Case Unsuccessful.")
    ##################################################