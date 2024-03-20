from odoo import api, models, fields
from odoo.exceptions import ValidationError


class DataPembelian(models.Model):
    _name = "data.pembelian"
    _description = "Data Pembelian"
    _log_access = False
    _rec_name = "name_costumer"

    id_costumer = fields.Integer(string="ID_Costumer", required=True)
    name_costumer = fields.Char(string="Name", required=True)
    date_costumer = fields.Date(string="Date", required=True)
    cake = fields.Selection([
        ("nastar", "Nastar"),
        ("putri salju", "Putri Salju"),
        ("donut", "Donut"),
        ("kastangel", "Kastangel"),
        ("prolltape", "Prolltape"),
    ], string="Cake", required=True)
    price_unit = fields.Float(string="Price_Unit")
    quantity = fields.Integer(string="Quantity")
    total = fields.Float(string="Total", compute="_compute_total_price")
    city = fields.Char(string="City")
    state_id = fields.Many2one('res.country.state', string="State")
    active = fields.Boolean(string="Active")
    # bagian untuk description
    tooping = fields.Boolean(string="Extra Tooping")
    total_price_tooping = fields.Integer(string="Price Tooping")

    @api.depends("price_unit", "quantity")
    def _compute_total_price(self):
        for recods in self:
            recods.total = (recods.price_unit * recods.quantity)
            if recods.total <= 0:
                raise ValidationError("value should a be positive")

    @api.onchange("tooping")
    def _onchange_tooping(self):
        for record in self:
            if record.tooping == True:
                record.total_price_tooping = 6000
            else:
                undo = record.total_price_tooping - 6000
                record.total_price_tooping = undo

    def action_cancel(self):
        for record in self:
            record.price_unit = 0
        return True

    @api.constrains("quantity")
    def _check_quantity(self):
        for record in self:
            if record.quantity <= 0:
                raise ValidationError("Quantity must be greater then zero")


class DataPembayaran(models.Model):
    _name = "data.pembayaran"
    _description = "Data Pembayaran"
    _log_access = False

    partner_id_pembeli = fields.Many2one('data.pembelian', string="Costumer")
    partner_city = fields.Integer(string="ID_CostumerCity", related="partner_id_pembeli.id_costumer")
    partner_state = fields.Many2one("res.country.state", related="partner_id_pembeli.state_id")
    date_payment = fields.Date(string="Date Pembayaran", required=True)
    type_payment = fields.Selection([
        ("dana", "DANA"),
        ("flip", "FLIP"),
        ("permata bank", "Permata Bank"),
        ("mandiri", "Mandiri"),
        ("bca", "BCA"),
        ("bri", "BRI")
    ], string="Type Of Payment", required=True)

    cash = fields.Boolean(string="Cash")
    tf = fields.Boolean(string="Transfer")
    keterangan = fields.Boolean(string="Lunas")
