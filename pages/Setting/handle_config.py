import os
from cryptography.fernet import Fernet


def create_config_if_not_exists(file_path='config.ini'):
    if not os.path.exists(file_path):
        config_content = """[Database]
host = your_db_host
port = your_db_port
database = your_db_name
user = your_db_user
password = your_db_password

[AppSettings]
language = Russian
theme = Light
scale = 100
"""
        with open(file_path, 'w') as file:
            file.write(config_content)
        print(f"Config file '{file_path}' created with default values.")
    else:
        print(f"Config file '{file_path}' already exists.")


def read_config(file_path='config.ini'):
    config = {}
    current_section = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith(';') or line.startswith('#'):
                continue

            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                config[current_section] = {}
            else:
                key, value = line.split('=', 1)
                config[current_section][key.strip()] = value.strip()

    return config

def encrypt_password_db():
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    text_to_encrypt = "Hello, World!"
    cipher_text = cipher_suite.encrypt(text_to_encrypt.encode())
    print("Cipher Text:", cipher_text)
    decrypted_text = cipher_suite.decrypt(cipher_text).decode()
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    create_config_if_not_exists()

    # Чтение конфигурации
    config = read_config()

    # Получение параметров подключения к базе данных
    db_config = config.get('Database', {})
    print("Database Configuration:", db_config)

    # Получение настроек приложения
    app_settings = config.get('AppSettings', {})
    print("App Settings:", app_settings)
