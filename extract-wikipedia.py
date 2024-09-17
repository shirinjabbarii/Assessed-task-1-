import wikipediaapi

# Initialize the Wikipedia API with a proper user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent="Mozilla/5.0 (compatible; ShirinBot/1.0; +shirinjabbari799@gmail.com)"
)

# Specify the Wikipedia page title for the actor
page_title = "The Weeknd"  # Replace with the actor's name of your choice

# Get the page
page = wiki_wiki.page(page_title)

# Check if the page exists
if page.exists():
    # Extract the main text content
    text = page.text

    # Save the text to a file
    with open("wikipedia.txt", "w", encoding='utf-8') as file:
        file.write(text)
        print("Text successfully extracted and saved to wikipedia.txt")
else:
    print(f"The page {page_title} does not exist on Wikipedia.")
