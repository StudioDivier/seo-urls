import json
import time
from services.fincs import start
from services.htaccess_rules import redirect_301


def main(csv_path, xml_path):
    good, bad = start(csv_path, xml_path)
    with open('file_output/result.json', 'w', encoding='utf-8') as file:
        json.dump(good, file)
    with open('file_output/bite_link.json', 'w', encoding='utf-8') as file_bad:
        json.dump(bad, file_bad)

    print('complete.')
    return 0


if __name__ == '__main__':

    csv_path = "file_input/https_tdlider-spb.ru_443_f395b614ee2111737e8e400b.csv"
    xml_path = "file_input/sitemap.xml"

    main(csv_path, xml_path)
    redirect_301()

