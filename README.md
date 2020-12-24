# SEO-UTILS: error 404 urls checker

![GitHub](https://img.shields.io/github/license/StudioDivier/seo-urls?label=license) ![GitHub followers](https://img.shields.io/github/followers/aliensowo)
![GitHub last commit](https://img.shields.io/github/last-commit/StudioDivier/seo-urls) ![GitHub repo size](https://img.shields.io/github/repo-size/StudioDivier/seo-urls)

____

## LAST UPD

*25.12.2020*

--  `v1.1-release` добавлено: 
* формирование отдельных json-файлов хранящих упорядоченные 
коллекции валидных и невалидных ссылок
* формирование директории `rules301` с файлами, которые хранят отфильтрованные по каталогам 
    правила редиректа 301 для `.htaccess`
 

____

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

### Результат выполнения
*directory: `file_output`*

**1** `result.json` - json-файл с сожержимым в формате:
    
    <:dict>
    {
        <:str>  'битая ссылка':
        <:list> [<:str> 'найденное совпадение'],
    }
    
**2** `bite_link.json` - json-файл с ссылками по которым не было найдено совпадение и 
представляет обычный список с элементами `:str` . Требуют проверки человеком.

**3** `filter_data.json` - временный json-файл, в котором содержаться отфильтрованные по 2-ому уровню ссылки

    <:dict>
    {
        <:str>:
        <:lsit> [<:str>],
    }
    
**4** `invalid_data.json` - временный json-файл, в котором сожержаться отфильтрованные по 2-ому уровню ссылки

    <:dict>
    {
        <:str>:
        <:lsit> [<:str>],
    }
    
    
**!** `filter_data.json` и `invalid_data.json` хранят в себе коллекцию упорядоченных валидных и невалидных 
ссылок соответственно. В дальгейгем будут участвовать в формировании базы ссылок для отправления на переиндексацию.

*directory: `rules301`*

**5** В папке `rules301` хранятся `.txt` файлы, именами которых являются директории(каталоги и/или подкатологи) сайта, 
т.е. отформатированные по каталогам для условного удобства заполнения файла `.htaccess` , 
а также в дальнейшем будет использоваться для кластеризации ссылок отправляемых на переиндескацию. 
Содержимое файлов представляет собой строки вида:

    Redirect 301 /catalogkleypol/ https://tdlider-spb.ru/kley/kleypol
 


## CHECK-LIST

    
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

- [x] формирование файла(-ов) с готовыми правилами для .htaccess

- [ ] встроенный сервис по отправке страниц на переиндексацию

- [ ] таск манагер по переадресации

- [ ] отдельный глобавльный файл для настроек

- [ ] коментарии

- [ ] метод добавление строк в файл `.htaccess`