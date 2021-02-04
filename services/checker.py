import requests as re


def link_checker(links: list):
    no_redirect = list()
    for link in links:
        r = re.get(link)
        if str(r.history[0]) == '<Response [301]>':
            continue
        else:
            no_redirect.append(link)
    if no_redirect:
        return no_redirect
    else:
        return True

