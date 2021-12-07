Welcome to Group O's Web Scraper 

Below, we will provide a few instructions on how to run our code, including a layout and the imports you would have to download.


Layout: Once you open the project folder, you will see 6 files:(htmlFinder.py, linkFinder.py, picFinder.py, tagFinder.py, 
	WebsiteFetch.py, main.py). These are the 5 features implemented, alongside the main.py which runs whichever function
	you would like to call. 

Feature Descriptions:
	1) htmlFinder: In this feature, the child will be prompted to enter a website of their choice. (Let's say they input "ign").
	  Our porgram will then fetch the data from www.ign.com, find the html code, and output it to a txt file.
	
	2) linkFinder: In this feature, the child will be prompted to enter something they would like to search (in the same sense
	   they would use a "google search"). Once they input what they want, we will output the top 10 search results into a CSV file.

	3) picFinder: In this feature, the child will be prompted to enter what image they would like to search. Followed by the amount 
	   of pictures they want. The program will then output the pictures to a folder called "Images_1" in jpg format. 
	
	4) tagFinder: In this feature, the child will be prompted to enter a webiste of their choice. The program will then output each element
	   and tag of that website's code. It will also display the occurence of each element. 

	5) WebsiteFetch: In this feature, the child will be prompted to enter a website of their choice. The program will then bring the child to
	   their website of choice, without the need of an internet browser.

Imports/Libraries to download: 
	- 'pip install webbrowser'
	- 'pip install requests'
	- 'pip install os'
	- 'pip install googlesearch'
	- 'pip install pandas'
	- 'pip install beautifulsoup4'

Sample inputs to console: 

	1) htmlFinder: 
		- "Hi, how can I help you?" -> 'i want to see the code of a website'
		- "Enter the website in which you would like to see the code:" -> 'ign'
	

	2) linkFinder: 
		- "Hi, how can I help you?" -> 'i want to search for something'
		- "What do you want to search?" 'toys'

	
	3) picFinder: 
		- "Hi, how can I help you?" -> 'i want to see pictures'
		- "What images do you want to search?" -> 'marvel'
		- "How many pictures do you want?" -> '3'


	4) tagFinder: 
		- "Hi, how can I help you?" -> 'i want to see the tags of a website'
		- "Enter the website in which you would like to see the HTML elements for:" -> 'ign'


	5) WebsiteFetch: 
		- "Hi, how can I help you?" -> 'i want to go to a website'
		- "Enter the website in which you would like to visit: " -> 'youtube'

	