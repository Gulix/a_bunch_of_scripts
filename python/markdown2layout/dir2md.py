import os
import tidy_md

def concat_files(files, destination_file):
    '''Concat all files in the list to one file'''

    concat_data = ''
    for filename in files:
        with open(filename, 'r', encoding="utf-8") as fileIn:
            concat_data += fileIn.read()
            concat_data += '\n'

    concat_data = tidy_md.tidy_text(concat_data, remove_links=True)
    
    with open(destination_file, 'w', encoding="utf-8") as fileOut:
        fileOut.write(concat_data)

def get_ordered_md_files(dir_path):
    '''Returns all the markdown files of a directory'''
    tab = [ ]
    for root, dir, f in os.walk(dir_path):
        for file in f:
            if file.endswith(".md"):
                filename = os.path.join(root, file)
                tab.append(filename)
    return tab