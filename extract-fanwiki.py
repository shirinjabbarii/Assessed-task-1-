import fandom

# Set the wiki you want to search within
fandom.set_wiki("jojo")

# Define the character's page title based on your student number
character_name = "Jonathan Joestar"  # Character corresponding to the last digit 0

# Search for the character page
character_page = fandom.page(character_name)

# Ensure the page is found
if character_page is not None:
    # Extract the content from the page
    page_content = character_page.content

    # Check if the content is a dictionary and extract the main text
    if isinstance(page_content, dict) and 'content' in page_content:
        main_text = page_content['content']
    else:
        main_text = str(page_content)  # Fallback to ensure content is string

    # Save the text to a file
    with open("fanwiki.txt", "w", encoding='utf-8') as file:
        file.write(main_text)
        print("Text successfully extracted and saved to fanwiki.txt")
else:
    print(f"No page found for {character_name} on Jojo Wiki.")
