#!/usr/bin/python3
""" 
Intro to SSR
"""
import os


def generate_invitations(template, attendees):
    """
    Generates customized invitation files from a template string and 
    a list of attendee dictionaries.
    """
    # 1. Check Input Types
    if not isinstance(template, str):
        print(
            f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list):
        print(
            f"Error: Invalid input type for attendees. Expected list, got {type(attendees).__name__}.")
        return

    # Check if all items in the attendees list are dictionaries
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print(
                f"Error: Invalid input type inside attendees list. Expected dict, got {type(attendee).__name__}.")
            return

    # 2. Handle Empty Inputs
    if not template or template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # List of placeholders expected in the template string
    placeholders = ["{name}", "{event_title}",
                    "{event_date}", "{event_location}"]

    # 3. Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        invitation_content = template

        for placeholder in placeholders:
            # Strip braces to match dictionary keys (e.g., '{name}' becomes 'name')
            key = placeholder.strip("{}")

            # Fetch the value from the dictionary
            value = attendee.get(key)

            # Replace missing or None data with "N/A"
            if value is None:
                value = "N/A"
            else:
                value = str(value)

            # Hint 1: Use Python's string replace method
            invitation_content = invitation_content.replace(placeholder, value)

        output_filename = f"output_{index}.txt"

        # Hint 2 & 3: Use os.path.exists and try-except blocks to safely write the file
        try:
            if os.path.exists(output_filename):
                # File exists already; it will be cleanly overwritten as per requirements
                pass

            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(invitation_content)

        except IOError as e:
            print(
                f"Error: An unhandled file I/O exception occurred for {output_filename}: {e}")
