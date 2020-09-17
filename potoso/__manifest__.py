# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'PO in SO',
    'version': '1.1',
    'summary': 'By using you can management purchase order from sales order.',
    'description': "this is for description",
    'category': 'Accounting',
    'website': '',
    'depends': ['base', 'sale_management', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_order_inherited.xml',
        'views/purchase_order_inherited.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 10.00,
    'currency': 'EUR'
}
