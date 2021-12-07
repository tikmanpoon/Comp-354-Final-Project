from picFinder import save_images_to_pc
from htmlFinder import html_finder
from tagFinder import tag_finder
from WebsiteFetch import website_fetch
from linkFinder import link_finder

# Pre-defined libraries used to determine what does the user want to do
word_for_html_finder = ["content", "html", "code"]
word_for_pic_finder = ["pictures", "picture", "images", "image", "photos", "photo"]
word_for_tag_finder = ["tag", "tags", "components", "component", "elements", "element"]
word_for_fetch_website = ["go", "access"]
word_for_change_colour = ["find", "know", "search"]
word_for_exiting_program = ["exit", "quit", "leave", "done"]

# The loop of the main program
while True:

    # Initialize booleans to record if we find any match from what the user entered
    # All were set to false and will be set to true if matched are found
    call_html_finder = False
    call_pic_finder = False
    call_tag_finder = False
    call_web_fetch = False
    call_colour_changer = False
    exiting_program = False

    # Ask the user for the input
    choice = input("Hi, How can I help you?\n").lower()


    # Split the String and put it into an array
    choice_word_array = choice.split()

    # Check if any word in the array matches any keyword
    # If yes, break the for loop and continue
    for word in choice_word_array:

        if word in word_for_html_finder:
            call_html_finder = True
            break

        elif word in word_for_pic_finder:
            call_pic_finder = True
            break

        elif word in word_for_tag_finder:
            call_tag_finder = True
            break

        elif word in word_for_fetch_website:
            call_web_fetch = True
            break

        elif word in word_for_change_colour:
            call_colour_changer = True
            break

        elif word in word_for_exiting_program:
            exiting_program = True
            break

    # Checking if any of the boolean is set to true.
    # If any of them is true, call the corresponding function
    # if not, repeat the loop and start from the beginning
    if call_html_finder:
        html_finder()

    elif call_pic_finder:
        save_images_to_pc()

    elif call_tag_finder:
        tag_finder()

    elif call_web_fetch:
        website_fetch()

    elif call_colour_changer:
        link_finder()

    elif exiting_program:
        print("Thank you!")
        print("Have a great day! Bye!")
        break
    else:
        print("Sorry, I don't understand what do you mean.")
        print("Let's try again! \n")







