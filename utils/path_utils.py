import os


def get_themes_path() -> str:
    """
    Получает путь к директории с темами приложения.

    :return: Строка, представляющая абсолютный путь к директории с темами.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    themes_dir = os.path.abspath(os.path.join(current_dir, '..', 'themes'))
    return themes_dir

def get_translate_path() -> str:
    """
    Получает путь к директории с файлами перевода приложения.

    :return: Строка, представляющая абсолютный путь к директории с файлами перевода.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    translations_dir = os.path.abspath(os.path.join(current_dir, '..', 'translations'))
    return translations_dir


