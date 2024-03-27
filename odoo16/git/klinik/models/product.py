from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import date



class Apotek_Klinic_Purchase(models.Model):
    _name = "klinic.apotek"
    _description = "Description Apotek"

    name = fields.Char(string="Name")
    status = fields.Selection([
        ('draft','Draft'),
        ('to_approve','To Approve'),
        ('approved','Approved'),
        ('done','Done')
    ], default='draft')
    tanggal = fields.Date(string="Tanggal")
    klinic_apotek_ids = fields.One2many('klinic.apotek.line', 'klinic_apotek_id', string="Pembelian Obat")


    def action_confirm(self):
        for line in self:
            if line.status == 'approved':
                line.status = 'done'

    def action_to_approve(self):
        for line in self:
            if line.status == 'draft':
                line.status = 'to_approve'

    def action_approved(self):
        for line in self:
            if line.status == 'to_approve':
                line.status = 'approved'

    @api.constrains('name')
    def _check_name(self):
        for line in self:
            if not line.name:
                raise ValidationError("Name isNull cant move")

    def _function_domain_product_id(self):
        product_obj = self.env('product.product').search([('type', '=', 'product')])
        domain = [('id', 'in', product_obj.ids)]
        return domain


    def action_help_wizard(self):
        self.ensure_one()
        return {
            'name': 'Comment',
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'klinic.comment.wizard',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def func_delete_status(self):
        klinik_apotek_obj = self.env['klinic.apotek'].search([('status', '=', 'draft')])
        for line in klinik_apotek_obj:
            line.unlink()
        return True


class Apotek_Purchase_Line(models.Model):
    _name = "klinic.apotek.line"

    klinic_apotek_id = fields.Many2one("klinic.apotek", string="Pharmacy Medicine ID")
    product_id = fields.Many2one('product.product', string="Product ID")
    quantity = fields.Float(string="Quantity", default=0)
    uom_id = fields.Many2one('uom.uom', string="Unit")

    harga_satuan = fields.Float(string="Harga Perstrip")
    sub_total = fields.Float(compute="_compute_subtotal", string="Sub Total")

    @api.onchange('harga_satuan','quantity')
    def _compute_subtotal(self):
        for line in self:
            line.sub_total = line.harga_satuan * line.quantity


class product_template(models.Model):
    _inherit = "product.template"

    product_description = fields.Char(string="Product Description")



