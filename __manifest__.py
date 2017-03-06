# -*- coding: utf-8 -*-
{
    'name': "Agenda INDESE",

    'summary': """
        Gestión de tareas automáticas""",

    'description': """
        Cada usuario recibe en este módulo diariamente el trabajo a realizar.
    """,

    'author': "INDESE",
    'website': "http://www.indese.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'INDESE',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
