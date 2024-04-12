{
    'name':'Real Estate',
    'summary':"""Odoo 16 Tutorials""",
    'description':"""Odoo 16 Development 
    """,
    'license':'OPL-1',
    'author':'Fajar Abdillah Ahmad',
    'website':'www.odoo.com',
    'category':'Sales',
    'depends':['web','base','product'],
    'data':[
        'security/estate_groups.xml',
        'security/ir.model.access.csv',
        'view/estate_property_views.xml',
        'view/estate_property_actions.xml',
        'view/estate_property_menu.xml'
        # 'view/klinik_cron_apotek.xml',
        # 'report/klinik_report_product.xml'
    ],
    'demo':[],
    'application':True,
}