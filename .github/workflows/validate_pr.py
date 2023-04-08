import os
import sys
from lxml import html

def get_names_from_readme(readme_path):
    with open(readme_path, "r") as file:
        readme_content = file.read()

    tree = html.fromstring(readme_content)
    table = tree.xpath('//table')[0]
    rows = table.xpath('.//tr')
    names = []

    for row_index, row in enumerate(rows):
        cols = row.xpath('.//td')
        if len(cols) == 7:  # Only process rows with exactly 7 columns
            for col_index, col in enumerate(cols):
                name_element = col.xpath('.//b')
                if name_element:
                    name = name_element[0].text.strip()
                    line_num = name_element[0].sourceline
                    names.append((name, line_num))
        else:
            print(f"Debug: Found {len(cols)} columns in row {row_index + 1}. Skipping row.")

    return names

def main():
    base_names = get_names_from_readme("README.md")
    head_names = get_names_from_readme("head/README.md")

    print(f"Debug: Base names: {base_names}")
    print(f"Debug: Head names: {head_names}")

    # Check for duplicates
    head_name_dict = {name: line_num for name, line_num in head_names}
    if len(head_name_dict) != len(head_names):
        duplicates = [line_num for name, line_num in head_names if head_names.count(name) > 1]
        print(f"Error: Duplicate names found on lines: {', '.join(map(str, duplicates))}")
        sys.exit(1)

    # Check if name is added at the end of the table
    added_names = list(set(head_name_dict.keys()) - set(name for name, _ in base_names))
    if len(added_names) != 1:
        print("Error: Only one name should be added.")
        sys.exit(1)

    added_name = added_names[0]
    if added_name != head_names[-1][0]:
        print(f"Error: Names should be added at the end of the table. Line: {head_names[-1][1]}")
        sys.exit(1)

    # Check if the table structure is maintained
    tree = html.fromstring(open("head/README.md", "r").read())
    table = tree.xpath('//table')[0]
    rows = table.xpath('.//tr')

    for row in rows:
        cols = row.xpath('.//td')
        if len(cols) > 7:
            print(f"Error: There should be no more than 7 columns in each row. Line: {cols[7].sourceline}")
            sys.exit(1)

if __name__ == "__main__":
    main()
