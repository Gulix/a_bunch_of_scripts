import dir2md
import tidy_md

dir_path = './data'


text = 'Un premier lien [[Test.md|Bidule]] suivi dun autre : [[Test.md|Bidule]]'
corrected = tidy_md.tidy_remove_links(text)


files = dir2md.get_ordered_md_files(dir_path)

print(files)
print("€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€")

data = dir2md.concat_files(files, "./test.md")