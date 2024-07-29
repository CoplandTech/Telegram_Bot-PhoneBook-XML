## УДАЛЕНИЕ СООБЩЕНИЙ ПОСЛЕ ЮЗЕРА ##
try:
        await message.delete()
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")

# def fetch_contacts_from_xml(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'xml')
#     contacts = []

#     for menu in soup.find_all('Menu'):
#         department_name = menu.get('Name', '')
#         for unit in menu.find_all('Unit'):
#             contact_data = {
#                 "name": [{
#                     "Name": unit.get('Name', ''),
#                     "middleName": unit.get('Middle', '')
#                 }],
#                 "organizations": [{
#                     "department": department_name,
#                     "jobTitle": unit.get('JobTitle', '')
#                 }],
#                 "phoneNumbers": [
#                     {"type": "internal_phone", "value": unit.get('Phone1', '')},
#                     {"type": "corporate_phone", "value": unit.get('Phone2', '')},
#                 ],
#                 "emailAddresses": [{
#                     "value": unit.get('Email', '')
#                 }]
#             }
#             contacts.append(contact_data)
    
#     return contacts

# contacts = fetch_contacts_from_xml(URL)

# for contact in contacts:
#     print(contact)