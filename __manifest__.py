# -*- coding: utf-8 -*-
{
    'name': "jt_debrand",

    'summary': "Odoo debranding",

    'description': "",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '2.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'data/mail_templates.xml',
        # 'views/portal_templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
