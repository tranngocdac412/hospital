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
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/data.xml',
        'data/mail_template.xml',
        'data/sequence.xml',

        'wizards/create_appointment.xml',

        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml',

        'reports/patient_card.xml',
        'reports/report.xml',

        'views/menu.xml'
    ],
    'qweb': [],
    "license": "AGPL-3",
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': 1
}