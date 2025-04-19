# Problem 2: Use REPL and print the table of 5 using it. was done in the terminal.

# Now Problem 3: Install an external module and use it to perform an operation of your interest.

import requests

# URL of the webpage to fetch
url = 'https://www.crunchyroll.com/news/latest'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Successfully fetched the webpage!")
    # Print the first 500 characters of the HTML content
    # Display only the first 500 characters for brevity
    print(response.text[:500])
else:
    print(
        f"Failed to retrieve the webpage. Status code: {response.status_code}")


# ANOTHER MODULE

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("My name is Qiran")
# engine.runAndWait()
