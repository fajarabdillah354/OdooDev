from odoo import api,fields,models

class DiscountAzka(models.Model):
    name_product = fields.Char(string="Name Product", required=True)
    discount_product = fields.Float(compute="_check_discount")
    total = fields.Float(compute="_check_discount")
    value = fields.Float(string="")
    discount = fields.Float(string="Discount")

    @api.depends('value','discount')
    def _check_discount(self):
        for record in self:
            discount = record.value * record.discount
            record.discount_product = discount
            record.total = record.value - discount

