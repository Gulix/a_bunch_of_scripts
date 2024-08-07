import dir2md

dir_path = './python/markdown2layout/data'

files = dir2md.get_ordered_md_files(dir_path)

print(files)
print("€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€")

data = dir2md.concat_files(files, "./python/markdown2layout/test.md")