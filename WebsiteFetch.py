import webbrowser

def website_fetch():
    # Assign the website to fetch by asking the child.
    chosen_website = input("Enter the website in which you would like to visit: \n")

    print("Opening website...\n...\n...")
    url = "https://www." + chosen_website

    # Use the webbrowser module to open whichever website the child has chosen.
    webbrowser.open(url)

    print("Done\n")