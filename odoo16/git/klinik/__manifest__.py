{
    'name':'Hospital',
    'summary':"""Odoo 16 Tutorials""",
    'description':"""Odoo 16 Development 
    """,
    'license':'OPL-1',
    'author':'Fajar Abdillah Ahmad',
    'website':'www.odoo.com',
    'category':'Tutorials',
    'depends':['web','base','product'],
    'data':[
        'security/ir.model.access.csv',
        'view/klinik_view.xml',
        'view/klinik_action_patient.xml',
        'view/klinik_menu_patient.xml',
    ],
    'demo':[],
    'application':True,
}