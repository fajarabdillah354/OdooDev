from odoo import models, fields

class DataAdmin(models.Model):
    _name = "data.admin"
    _description = "Data Admin"
    _log_access = False

    admin_name = fields.Char(string="Name Admin", required=True)
    admin_email = fields.Char(string="Email")
    id_admin = fields.Integer(string="Admin ID",required=True)
    access_admin = fields.Boolean(string="Active Admin")



