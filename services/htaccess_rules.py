import os
import json
import math


def filtring_data():
    with open('file_output/result.json', 'r') as file:
        data = json.load(file)
        filter_data = {}
        invalid_data = {}

        for elem in data:

            if str(data[elem][0].split('/')[3]) not in filter_data:
                filter_data[str(data[elem][0].split('/')[3])] = [str(data[elem][0])]
                invalid_data[str(data[elem][0].split('/')[3])] = [str(elem)]

            if str(data[elem][0].split('/')[3]) in filter_data:
                filter_data[data[elem][0].split('/')[3]].append(data[elem][0])
                invalid_data[data[elem][0].split('/')[3]].append(elem)

        with open('file_output/filter_data.json', 'w', encoding='utf-8') as fd:
            json.dump(filter_data, fd)

        with open('file_output/invalid_data.json', 'w', encoding='utf-8') as id:
            json.dump(invalid_data, id)

    return True


def delete_dublicate():
    path = 'rules301'
    for dirs, folder, files in os.walk(path):
        for file in files:
            uniqlines = set(open(path+'/'+file, 'r', encoding='utf-8').readlines())
            gotovo = open(path+'/'+file, 'w', encoding='utf-8').writelines(set(uniqlines))


def redirect_301():

    if filtring_data():
        with open('file_output/invalid_data.json', 'r') as id:
            invalid = json.load(id)
        with open('file_output/filter_data.json', 'r') as fd:
            valid = json.load(fd)
        links = []
        for elem in valid:
            title = elem
            with open('rules301/{}.txt'.format(title), 'w', encoding='utf-8') as file:
                for i in range(len(valid[elem])):
                    links.append(invalid[elem][i])
                    file.write("Redirect 301 {} {}\n".format(invalid[elem][i], valid[elem][i]))

        with open('file_output/invalid_data.txt', 'w', encoding='utf-8') as id_txt:
            for i in range(len(links)):
                if i % 140 == 0:
                    id_txt.write('# {}\n'.format(i // 140))
                id_txt.write('https://tdlider-spb.ru/{}\n'.format(links[i]))

        delete_dublicate()


