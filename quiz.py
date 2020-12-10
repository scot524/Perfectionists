#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import re


class List:

    def __init__(__self__, test_data=''):
        __self__.__list__ = []
        if test_data != '':
            for record in test_data.split('\n'):
                (name, email, phone) = record.split(',')
                __self__.new(name, email, phone)

    def new(
        __self__,
        name,
        email,
        phone,
        ):
        __self__.__list__.append({'name': (None if name == ''
                                  else name), 'email': (None if email
                                 == '' else email),
                                 'phone': (None if phone == ''
                                  else phone)})

    def list(__self__):
        for record in __self__.__list__:
            print (record['name'], record['email'], record['phone'])

    def find(__self__, key, value):
        if value is None:
            return None
        found = False
        result = 0
        for record in __self__.__list__:
            if record[key] == value:
                found = True
                break
            result += 1
        return (result if found else None)

    def remove(__self__, index):
        del __self__.__list__[index]


class Contacts(List):

    pass


class Leads(List):

    pass


contacts_test = \
    '''Alice Brown,,1231112223
\
Bob Crown,bob@crowns.com,
\
Carlos Drew,carl@drewess.com,3453334445
\
Doug Emerty,,4564445556
\
Egan Fair,eg@fairness.com,5675556667'''

leads_test = \
    ''',kevin@keith.com,
\
Lucy,lucy@liu.com,3210001112
\
Mary Middle,mary@middle.com,3331112223
\
,,4442223334
\
,ole@olson.com,'''
contact_db = Contacts(contacts_test)

# contact_db.list()

lead_db = Leads(leads_test)

# lead_db.list()

if __name__ == '__main__':
    contacts_test = \
        '''Alice Brown,,1231112223
\
Bob Crown,bob@crowns.com,
\
Carlos Drew,carl@drewess.com,3453334445
\
Doug Emerty,,4564445556
\
Egan Fair,eg@fairness.com,5675556667'''

    leads_test = \
        ''',kevin@keith.com,
\
Lucy,lucy@liu.com,3210001112
\
Mary Middle,mary@middle.com,3331112223
\
,,4442223334
\
,ole@olson.com,'''
    contact_db = Contacts(contacts_test)

#    contact_db.list()

    lead_db = Leads(leads_test)

#    lead_db.list()

    reg_json_strings = \
        ['''{
  "registrant":
     {
        "name": "Lucy Liu",
        "email": "lucy@liu.com"
     }
}''',
         '''{
"registrant":
 {
    "name": "Doug",
    "email": "doug@merry.com",
    "phone": "4564445556",
 }
}''',
         '''{
"registrant":
 {
    "name": "Uma Thurman",
    "email": "uma@thurs.com"
 }
}''']
    for reg_json in reg_json_strings:
        reg_json = re.sub(',[ \t\r\n]+}', '}', reg_json)
        reg_json = re.sub(",[ \t\r\n]+\]", ']', reg_json)
        registrant = json.loads(reg_json)
        name = (registrant['registrant']['name'] if 'name'
                in registrant['registrant'].keys() else None)
        email = (registrant['registrant']['email'] if 'email'
                 in registrant['registrant'].keys() else None)
        phone = (registrant['registrant']['phone'] if 'phone'
                 in registrant['registrant'].keys() else None)
        if contact_db.find('email', email) != None \
            or contact_db.find('phone', phone) != None:
            continue
        lead_index = lead_db.find('email', email) \
            or lead_db.find('phone', phone)
        if lead_index != None:
            print ('adding ', name)
            lead_db.remove(lead_index)
            contact_db.new(name, email, phone)

    contact_db.list()
    exit(0)
