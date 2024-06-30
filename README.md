# Aramid TsT Graph

## Сборка проекта

```commandline
python setup.py build
```
Возможны сбои при сборки, необходимо проверять на боевых стендах
## Установка зависимостей

Все зависимости, которые необходимо установить указаны в файле requriments.txt

Для установки PySide6, скачайте все исходники необходимые для установки (PySide6, PySide6-Addons, PySide6-Essentials, shiboken6)

Чтобы установить PySide6 пакеты, выполните следующую команду (проследите, что все пакеты лежат в одной папке)

```commandline
pip install PySide6*
```
P.S. основной список зависимостей представлен в файле requirements.txt
## Вызов утилит, входящих в состав PySide6

Для вызова Qt Designer (Средство создания интерфейса)
```commandline
pyside6-designer
```

Для вызова Qt Linguist (Средство организации перевода)
```commandline
pyside6-linguist
```

## Преобразование UI-файлов, файлов ресурсов, файлов переводов

Для преобразования ui-файлов испольуется утилита pyside6-uic (Обратите внимание на расширение файлов в примере):

pyside6-uic — это утилита, используемая для преобразования файлов интерфейса пользователя (UI), созданных с помощью Qt Designer, в исходный код Python. 

```commandline
pyside6-uic <путь до ui файла> -o <итоговый python модуль>
#Пример: pyside6-uic ./main.ui -o ./ui_modules/ui_main.py 
```

pyside6-lrelease.exe .\translations\en.ts  -qm .\translations\en.qm

Для преобразования файлов ресурсов (изображений, переводов, стилей) используется утилита pyside6-rcc (Обратите внимание на расширение файлов в примере):

pyside6-rcc — это утилита, используемая для работы с ресурсами в приложениях PySide6. Она компилирует файлы ресурсов (например, изображения, иконки, файлы стилей и другие статические ресурсы), описанные в файле ресурсов Qt (файл с расширением .qrc), в Python-модуль.

```commandline
pyside6-rcc <путь до qrc файла> -o <итоговый python модуль>
#Пример: pyside6-rcc ./resources.qrc -o ./ui_modules/resources_rc.py
```

Для преобразования файлов переводов используются утилиты pyside6-lrelease pyside6-lupdate (Обратите внимание на расширение файлов в примере):

pyside6-lupdate — это утилита, используемая для обновления файлов перевода Qt (.ts файлы) на основе строк, помеченных для перевода в исходном коде PySide6. 

pyside6-lrelease — это утилита, используемая для компиляции файлов перевода Qt (.ts файлы) в бинарные файлы (.qm), которые используются приложением для локализации.
```commandline
pyside6-lupdate <путь до python-модуля созданный pyside6-uic> <путь до ui-файла> -o <итоговый python модуль>
#Пример: pyside6-lupdate .\ui_modules\ui_main.py .\main.ui -ts .\translations\ru.ts
```

```commandline
pyside6-lrelease <путь до файла сформированный lupdate> -qm <итоговый бинарный файл перевода>
#Пример: pyside6-lrelease .\translations\en.ts  -qm .\translations\en.qm
```