# -*- coding: utf-8 -*-
{
    'name': "a18alejandrodv_inmo",

    'summary': "Gestión de Pisos y Alquileres para Inmobiliarias",

    'description': """
        Long description of module's purpose
    """,

    'author': "A18AlejandroDV",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/pisos.xml',
        'views/alquiler.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}