import os
import sys
import zipfile
import xml.dom.minidom

def count_pages_in_docx(file_path):
    try:
        document = zipfile.ZipFile(file_path)
        dxml = document.read('docProps/app.xml')
        uglyXml = xml.dom.minidom.parseString(dxml)
        page = uglyXml.getElementsByTagName('Pages')[0].childNodes[0].nodeValue
        return int(page)
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return 0

def main(directory_path):
    total_count = 0

    for filename in os.listdir(directory_path):
        if filename.endswith('.docx'):
            file_path = os.path.join(directory_path, filename)
            page_count = count_pages_in_docx(file_path)
            print(f"{filename}: Word Page count: {page_count}")
            total_count += page_count

    print(f"Total Word Page count in directory: {total_count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: word-page.py <directory>")
        sys.exit(1)

    directory_path = sys.argv[1]

    if not os.path.isdir(directory_path):
        print(f"'{directory_path}' is not a valid directory.")
        sys.exit(1)

    main(directory_path)
