import csv


def csv_to_data(file_name='contacts.csv'):
    with open(file_name, newline='', encoding='utf-8') as f:
        csv_f = csv.reader(f, delimiter=';')
        data = []
        for row in csv_f:
            data.append(row)
    return data


def export_to_txt(data=csv_to_data()):
    with open('contacts.txt', 'w', encoding='utf-8') as txt:
        for row in data:
            txt.write(f'{row}\n')
    return data
