import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

def create_xml_from_folder(root_dir, output_file="folder_structure.xml"):
    # Create the root element <categories>
    categories = ET.Element("categories")

    def add_folder_to_xml(parent_element, folder_path):
        # Get the folder name from the path
        folder_name = os.path.basename(folder_path)
        
        # Create a new <category> element with the folder name as an attribute
        category = ET.SubElement(parent_element, "category")
        category.set("name", folder_name)
        
        # Get all subdirectories in the current folder
        try:
            subdirs = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
            # Recursively add subfolders
            for subdir in sorted(subdirs):  # Sort for consistent order
                subdir_path = os.path.join(folder_path, subdir)
                add_folder_to_xml(category, subdir_path)
        except PermissionError:
            print(f"Permission denied for {folder_path}, skipping...")

    # Start processing from the root directory
    add_folder_to_xml(categories, root_dir)

    # Convert the ElementTree to a pretty-printed XML string
    rough_string = ET.tostring(categories, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")

    # Write the XML to a file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    print(f"XML file generated: {output_file}")

# Example usage
if __name__ == "__main__":
    # Specify the root directory to scan
    root_directory = "."  # Change this to your directory path
    
    # Ensure the root directory exists
    if not os.path.exists(root_directory):
        print(f"Directory '{root_directory}' does not exist. Creating sample structure...")
        # Create a sample folder structure for testing
        os.makedirs(os.path.join(root_directory, "Folder01"), exist_ok=True)
        os.makedirs(os.path.join(root_directory, "Folder02", "SubFolder01"), exist_ok=True)
    
    # Generate the XML file
    create_xml_from_folder(root_directory, "folder_structure.xml")