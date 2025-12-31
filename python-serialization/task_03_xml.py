#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    
    Args:
        dictionary (dict): The data to serialize.
        filename (str): The name of the output XML file.
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Error writing to XML: {e}")

def deserialize_from_xml(filename):
    """
    Reads an XML file and reconstructs it into a Python dictionary.
    
    Args:
        filename (str): The name of the XML file to read.
        
    Returns:
        dict: The reconstructed dictionary, or None if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text
            
        return deserialized_dict

    except (FileNotFoundError, ET.ParseError) as e:
        print(f"Error reading from XML: {e}")
        return None
