# SEO-UTILS: error 404 urls checker

![GitHub](https://img.shields.io/github/license/StudioDivier/seo-urls?label=license) ![GitHub followers](https://img.shields.io/github/followers/aliensowo)
![GitHub last commit](https://img.shields.io/github/last-commit/StudioDivier/seo-urls) ![GitHub repo size](https://img.shields.io/github/repo-size/StudioDivier/seo-urls)

## USING

Файл `sitemap.py` составит полный sitemap.xml сайта и сохранит результат в `file_input\sitemap.xml`.
Также для работы потребуется выгрузка страниц в формате `.csv` с [Яндекс.Вебмастер](https://webmaster.yandex.ru).
При работе возможно создание временных файлов в `~/file_input/`.

Так как идет сверка битых ссылок по sitemap.xml, то результат замены всегда будет валидным
(**!** зависит от свежести файла `sitemap.xml` ),
но для уверенности всегда рекомендую пробежать по файлу `result.json` хотя бы бегло.


Скрипт функционирует на основе алгоритма *Боейра-Мура* по поиску подстроки в строке 
и сравнения значений конечных уровней ссылок.
____

### Для работы программы выполнить команды:

1. `python -m venv venv`

2. Активация виртуального окружения:

    * *nix: `source venv/bin/activate` ; 
    *  win: `venv/Scripts/activate.bat` ;
    
3. `pip install -r requirements.txt`

### Выполнение работы
**!**   _Взаимодействие через терминал имеет статус **в разработке**_

**1.** Для составления карты сайта в файле `sitemap.py` заменить в строке **14** заменить
значение переменной `root_url = '' `

**2.** Для запуска программы (*уже должны быть подготовдены исходные файлы*)  в файле `main.py`
заменить в строках **19, 20** значения переменных `csv_path = '' `, `xml_path = '' ` соответственно.


**3.** Выполнить скрипт `main.py` = > Вывод в печать сигнал и завершении.
Результат смотреть в папке `~/file_output/`

**4** `result.json` - json-файл с сожержимым в формате:
    
    <:dict>
    {
        <:str>  'битая ссылка':
        <:list> [<:str> 'найденное совпадение'],
    }
    
`bite_link.json` - json-файл с ссылками по которым не было найдено совпадение и представляет обычный список с элементами `:str`


##CHECK-LIST

    
- [x] в битых ссылках во время поиска исключается  "/p/"

- [x] в битых ссылках во время поиска исключается "catalog"

- [x] опредление уровня каталога (пример ниже)

    
    "/kraski_i_emali/spetsialnye": [
    "https://tdlider-spb.ru/kraski_i_emali/spetsialnye/grafitovaya"
    ],
    "/gruntovki": [
    "https://tdlider-spb.ru/gruntovki/po-derevu"
    ],
    
    Можно решить с помощью равенства уровня ссылок: 
        => дальше паттерна ссылка уходить не должна  
  
    
- [x] разделить валидный результат от невалидного

- [x] выдача формируется из полной битой ссылки и нормальной

- [x] адекватная директория

- [ ] работа через командую строку