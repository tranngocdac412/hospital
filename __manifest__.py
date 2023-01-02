# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': '',
    'author': 'D',
    'website': '',
    'company': '',
    'maintainer': '',
    'summary': '',
    "description": '',
    'depends': ['base', 'mail', 'sale'],
    'data': [
        'security/ir.model.access.csv',

        'data/sequence.xml',

        'views/patient.xml',
        'views/appointment.xml',

        # 'reports/patient_card.xml',
        # 'reports/report.xml',


        'views/menu.xml'
    ],
    'qweb': [],
    "license": "AGPL-3",
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': 1
}