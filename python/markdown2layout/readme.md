A link to follow : https://stackoverflow.com/questions/70513062/how-do-i-add-custom-formatting-to-docx-files-generated-in-pandoc

'''
pandoc -o custom-reference.odt --print-default-data-file reference.odt
'''

pandoc -S test_input.md -o test_output.docx --reference-docx ./custom_styles.docx --filter ./test_filter.py

pandoc -S test.md -o test.odt --reference-odt ./custome-reference.odt