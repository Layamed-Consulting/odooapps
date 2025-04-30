{
    'name': "POS RECEIPT QTY",
    'summary': "Add in receipt quantity total",
    'description': """
Compatibility:
--------------
✅ Odoo Enterprise
✅ Odoo Community


Support:
--------
For support, contact us at: contact@layamedconsulting.com
    """,
    'author': 'Layamed Consulting Sarl',
    'version': '17.0.1.0.0',
    'category': 'Point of Sale',
    'version': '1.0',
    'depends': ['point_of_sale'],
    'data': [
        'views/views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_cheque_Information/static/src/app/**/*',
        ],
    },

    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'price': 2.00,
    'currency': 'USD',
    'installable': True,
    'application': True,
    'auto_install': False,
}
