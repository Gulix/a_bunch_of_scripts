# Code used to tidy up the markdown
# I usually use Obsidian to write Markdown, and that markdown is sometimes messy (linebreaks, for example).
# I want to generate "adequate" and consistent markdown files, so this code here has this purpose
# The basics are from that library : https://mdformat.readthedocs.io/en/stable/users/installation_and_usage.html
# The code could be upgraded with specific needs

import mdformat
import re

def tidy_text(text, remove_links = False):

    tidied = text
    if remove_links:
        tidied = tidy_remove_links(tidied)

    tidied = mdformat.text(tidied)
    return tidied

def tidy_remove_links(text):
    # Remove any kind of links in the markdown
    # For our purpose (concat multiple files), links will often be useless

    # [[My Link|My text]]
    rx = r'\[\[([^\|\]]+)\|([^\|\]]+)\]\]'
    returned_text = re.sub(rx, r'\2', text)

    # [My text](My link)
    rx = r'\[([^\]]+)\]\(([^\)]+)\)'
    returned_text = re.sub(rx, r'\1', returned_text)

    return returned_text