import xml.etree.ElementTree as ET
import os
import sys

def update_xml(input_file, output_file, tag_path, new_value):
    try:
        # Check if the input file exists
        if not os.path.exists(input_file):
            print(f"Input file '{input_file}' does not exist.")
            sys.exit(1)

        # Parse the input XML file
        tree = ET.parse(input_file)
        root = tree.getroot()

        # Find the tag using full path (e.g., 'configuration/changelogFile')
        element = root.find(tag_path)
        if element is not None:
            # Update the tag's text value
            element.text = new_value
            # Write to the output file (this creates the file if it doesn't exist)
            tree.write(output_file)
            print(f"Updated '{tag_path}' and wrote the changes to '{output_file}'.")
        else:
            print(f"Tag '{tag_path}' not found in the XML file.")

    except ET.ParseError:
        print(f"Error parsing XML file: {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python update_xml.py <input_file> <output_file> <tag_path> <new_value>")
        sys.exit(1)

    # Get the arguments from the command line
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    tag_path = sys.argv[3]  # e.g., 'configuration/changelogFile'
    new_value = sys.argv[4]

    # Update the XML file
    update_xml(input_file, output_file, tag_path, new_value)
