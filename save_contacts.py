def save_to_csv(contact_info):
    with open('contacts.csv', 'a', encoding='utf-8') as bd:
        for i in range(len(contact_info)):
            if i != len(contact_info) - 1:
                bd.write(f'{contact_info[i]};')
            else:
                bd.write(f'{contact_info[i]}')
        bd.write('\n')
