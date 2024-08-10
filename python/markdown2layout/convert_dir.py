import dir2md
import tidy_md
import sys

print("Démarrage de la conversion...")
print("Répertoire à transformer en fichier Markdown : ")
dir_path = input()
print("Fichier final à générer : ")
final_file = input()

files = dir2md.get_ordered_md_files(dir_path)

if len(files) == 0:
    print("Aucun fichier à transformer...")
else:
    print(f"Transformation de {len(files)} fichiers...")
    data = dir2md.concat_files(files, final_file)