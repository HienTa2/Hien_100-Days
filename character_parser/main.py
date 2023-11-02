# Import the etree module from the lxml library
from lxml import etree


# Define the function that will process the XML file
def find_note_txt_with_line_numbers(xml_file):
    # Try block to catch any parsing errors
    try:
        # Parse the XML file and directly get the root element
        root = etree.parse(xml_file).getroot()
    # Catch exceptions (errors) that may occur during parsing
    except Exception as e:
        # Print the error message if parsing fails
        print(f"Error parsing XML file: {e}")
        # End the function early in case of error
        return

    # Iterate over all elements in the XML tree with the tag 'NOTE_TXT'
    for note_txt in root.iter('NOTE_TXT'):
        # Calculate the length of the text content, removing any leading or trailing whitespaces
        text_length = len(note_txt.text.strip()) if note_txt.text else 0
        # Check if the text content is 1000 characters or more
        if text_length >= 3000:
            # Print a message showing the line number and character count of the tag
            print(
                f"NOTE_TXT with more than 1000 characters found at line {note_txt.sourceline}: {text_length} characters")
            # Uncomment the following line if you want to print the content of the tag
            # print(note_txt.text.strip())


# Call the function with the name of the XML file and put in the same directory
find_note_txt_with_line_numbers('PUT XML File here')
