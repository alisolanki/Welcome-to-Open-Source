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
                names.append(name)

    # Check for duplicates
    if len(names) != len(set(names)):
        print("Error: Duplicate names found.")
        sys.exit(1)

    # Check if name is added at the end of the table
    added_names = os.environ['GITHUB_HEAD_REF']
    if added_names not in names[-1]:
        print("Error: Names should be added at the end of the table.")
        sys.exit(1)

    # Check if only one name is added
    if len(names) - len(rows) * 7 != 1:
        print("Error: Only one name should be added.")
        sys.exit(1)

if __name__ == "__main__":
    main()
