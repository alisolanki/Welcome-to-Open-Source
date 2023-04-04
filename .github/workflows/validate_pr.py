import os
import sys
from lxml import html

def main():
    with open("README.md", "r") as file:
        readme_content = file.read()

    # Parse the table
    tree = html.fromstring(readme_content)
    table = tree.xpath('//table')[0]
    rows = table.xpath('.//tr')
    names = []

    for row in rows:
        cols = row.xpath('.//td')
        for col in cols:
            name_element = col.xpath('.//b')
            if name_element:
                name = name_element[0].text.strip()
                line_num = name_element[0].sourceline
                names.append((name, line_num))

    # Check for duplicates
    name_dict = {}
    duplicate_lines = []
    for name, line_num in names:
        if name in name_dict:
            duplicate_lines.append(line_num)
        else:
            name_dict[name] = line_num

    if duplicate_lines:
        print(f"Error: Duplicate names found on lines: {', '.join(map(str, duplicate_lines))}")
        sys.exit(1)

    # Check if name is added at the end of the table
    added_names = os.environ['GITHUB_HEAD_REF']
    if added_names not in names[-1][0]:
        print("Error: Names should be added at the end of the table.")
        sys.exit(1)

    # Check if only one name is added
    total_names_before = len(names) - 1
    total_names_now = len(rows) * 7
    if total_names_before + 1 != total_names_now:
        print("Error: Only one name should be added.")
        sys.exit(1)

if __name__ == "__main__":
    main()
