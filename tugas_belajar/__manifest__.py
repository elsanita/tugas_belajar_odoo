# -*- coding: utf-8 -*-
{
    'name': "tugas_belajar",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale', 'point_of_sale'],

    # always loaded
    'data': [
        'data/sequence.xml',
        'reports/daily_report_action.xml',
        'reports/daily_report_pdf_template.xml',
        'security/ir.model.access.csv',
        'views/karyawan/karyawan_form_view.xml',
        'views/karyawan/karyawan_server_actions.xml',
        'views/karyawan/karyawan_tree_view.xml',
        'views/karyawan/karyawan_view_actions.xml',
        'views/rule_komisi_karyawan/rule_komisi_karyawan_form_view.xml',
        'views/rule_komisi_karyawan/rule_komisi_karyawan_server_actions.xml',
        'views/rule_komisi_karyawan/rule_komisi_karyawan_tree_view.xml',
        'views/rule_komisi_karyawan/rule_komisi_karyawan_view_actions.xml',
        'views/rule_komisi_karyawan/sale_inherit.xml',
        'views/history_komisi_karyawan/history_komisi_karyawan_server_actions.xml',
        'views/history_komisi_karyawan/history_komisi_karyawan_tree_view.xml',
        'views/history_komisi_karyawan/history_komisi_karyawan_view_actions.xml',
        'views/pos/pos_order_form.xml',
        'views/project/project_form_view.xml',
        'views/project/project_server_actions.xml',
        'views/project/project_tree_view.xml',
        'views/project/project_view_actions.xml',
        'views/report/report_form_view.xml',
        'views/report/report_server_actions.xml',
        'views/report/report_tree_view.xml',
        'views/report/report_view_actions.xml',
        'views/top_menu_view.xml',
        'wizards/views/rule_komisi_karyawan_form_wizard.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            'tugas_belajar/static/src/js/models.js',
            'tugas_belajar/static/src/js/Orderline.js',
            'tugas_belajar/static/src/js/ProductScreen.js',
            'tugas_belajar/static/src/xml/pos_cashier_inherit.xml',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
