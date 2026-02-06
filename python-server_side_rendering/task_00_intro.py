import os

def generate_invitations(template, attendees):
    # -------- Check input types --------
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # -------- Check empty inputs --------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # -------- Placeholders --------
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # -------- Process each attendee --------
    for index, attendee in enumerate(attendees, start=1):
        output_text = template

        for field in placeholders:
            value = attendee.get(field)

            # Replace missing or None values with "N/A"
            if value is None:
                value = "N/A"

            output_text = output_text.replace(f"{{{field}}}", str(value))

        # -------- Create output file --------
        filename = f"output_{index}.txt"

        with open(filename, "w") as file:
            file.write(output_text)

