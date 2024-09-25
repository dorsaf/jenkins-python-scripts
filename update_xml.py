import xml.etree.ElementTree as ET
import sys

def update_xml(file_path, tag, new_value):
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Find the tag
        element = root.find(tag)
        if element is not None:
            # Update the tag's value
            element.text = new_value
            # Save the updated XML file
            tree.write(file_path)
            print(f"Updated '{tag}' with new value: {new_value}")
        else:
            print(f"Tag '{tag}' not found in the XML file.")

    except ET.ParseError:
        print(f"Error parsing XML file: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python update_xml.py <file_path> <tag> <new_value>")
        sys.exit(1)

    # Get the arguments from the command line
    file_path = sys.argv[1]
    tag = sys.argv[2]
    new_value = sys.argv[3]

    update_xml(file_path, tag, new_value)
