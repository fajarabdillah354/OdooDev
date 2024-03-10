{
    'name':'Azka Shop',
    'summary':"""toko yang menyediakan aneka cake""",
    'description':"""kami menyediakan : 
        - nastar
        - bolu keju
        - donuts
        - prolltape
    """,
    'license':'OPL-1',
    'author':'Fajar Abdillah Ahmad',
    'website':'www.odoo.com',
    'category':'Sales',
    'depends':['base'],
    'data':[
        'security/azkacake_groups.xml',
        'security/azkacake_security.xml',
        'security/ir.model.access.csv',
        'view/data_azkacake_view.xml',
        'view/data_azkacake_action.xml',
        'view/data_azkacake_menu.xml'

    ],
    'demo':[],
    'application':True,
}