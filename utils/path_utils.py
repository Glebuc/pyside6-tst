import os

def get_themes_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    themes_dir = os.path.abspath(os.path.join(current_dir, '..', 'themes'))
    return themes_dir

def get_translate_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    translations_dir = os.path.abspath(os.path.join(current_dir, '..', 'translations'))
    return translations_dir


themes_path = get_themes_path()
translations_path = get_translate_path()
print(themes_path)
print(translations_path)
