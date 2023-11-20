# -*- coding: utf-8 -*-
{
    "name": "Module Appschef",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    "description": """
        This module was created as learning material for creators
    """,
    "author": "Viendev",
    "website": "https://www.viendev.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Employees",
    "version": "16.0.0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/views.xml",
        "views/templates.xml",
        "views/karyawan/karyawan_view.xml",
        "views/karyawan/karyawan_action.xml",
        "views/project/project_view.xml",
        "views/project/project_action.xml",
        "views/report/report_view.xml",
        "views/report/report_action.xml",
        "reports/report.xml",
        "reports/daily_report_template.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
