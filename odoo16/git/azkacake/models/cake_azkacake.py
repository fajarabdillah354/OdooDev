from odoo import api, models, fields

class CakeAzka(models.Model):
    _name = "data.cake"
    _description = "Data Cake"
    _log_access = False

    name_product = fields.Char(string="Product Name", required=True)
    category_product = fields.Char(string="Category")
    quantity_product = fields.Integer(string="Quantity", default=0)




