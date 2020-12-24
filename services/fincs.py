import re
import csv
from bs4 import BeautifulSoup as bs
from services.bm_algorithm import boyer_moore_match


def csv_reader(file_obj):
    """
    Read a csv file
    :return: list 404 pages, count of pages
    """
    reader = csv.reader(file_obj)
    count_404, count_all = 0, 0
    list_404 = []
    for row in reader:
        count_all += 1
        if row[1] == '404':
            count_404 += 1
            list_404.append(row[0])

    return list_404, count_404


def xml_reader(file_obj):
    """

    :param file_obj:
    :return: list sites url with its len
    """
    map_list = []
    soup = bs(file_obj, "html.parser")
    str_urls = str(soup.get_text()).replace(" ", "").split('\n')
    for elem in str_urls:
        if elem != '':
            map_list.append(elem)

    return map_list, len(map_list)


def get_data(csv_path, xml_path):
    with open(csv_path, "r") as f_obj:
        link404, c_link404 = csv_reader(f_obj)

    with open(xml_path, "r") as f_obj:
        site_link, c_site_link = xml_reader(f_obj)

        with open('file_input/site_urls.txt', 'w') as file:
            for row in site_link:
                file.write(row + '\n')

    data = {}
    data['404_links'] = {
        'counts': c_link404,
        'links': link404
    }
    data['sitemap'] = {
        'counts': c_site_link,
        'links': site_link
    }

    return data


def slice_link(link: str) -> list:
    link = link.split('/')
    return list(reversed(link))


def foring(test_link, sitemap_links):
    for part in test_link:
        if part == '':
            continue
        else:
            for links in sitemap_links:
                result = boyer_moore_match(links, part)
                if result is True:
                    if part == links.split('/')[-1]:
                        return links


def start(csv_path, xml_path):
    # csv_path = "file_input/https_tdlider-spb.ru_443_f395b614ee2111737e8e400b.csv"
    # xml_path = "file_input/sitemap.xml"

    data = get_data(csv_path=csv_path, xml_path=xml_path)
    sitemap_links = data['sitemap']['links']

    bite_links = data['404_links']['links']

    # test_link = '/kraski_i_emali/kraski_i_emali/nts_132/'
    # test_link = test_link.split('/')
    # test_link.reverse()

    BIG_RESULT = {}
    BIG_TRASH = []

    for bite in bite_links:
        e = re.sub(r'/p/\d', '', bite)
        q = re.sub('catalog', '', e)
        test_link = slice_link(q)

        link = foring(test_link, sitemap_links)
        if link == None:
            BIG_TRASH.append(bite)
        else:
            BIG_RESULT['https://tdlider-spb.ru' + bite] = [link]

    return BIG_RESULT, BIG_TRASH


