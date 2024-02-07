{
    'name': "sale order customization",
    'version': '15.0.',
    'summary': """sale order customization""",
    'description': """Zinfog Task""",
    'depends': ['base', 'sale', 'account'],

    'data': [
        'views/sale_order_views.xml',
        'views/product_template.xml',
        'views/account_move.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}
