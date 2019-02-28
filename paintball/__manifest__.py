# -*- coding: utf-8 -*-
{
    'name': "paintball",

    'summary': """
        Gestión de empresas de paintball
        """,

    'description': """
        Gestión de empresas de paintball
    """,

    'author': "Samuel Garcia Paton",
    'website': "http://www.paintball.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
