from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Dokter(models.Model):
        _name = "klinic.doctor"
        _description = "Klinic Doctor"
        _rec_name = "doctor_name"


        doctor_name = fields.Char(string="Nama", required=True)
        specialization = fields.Char(string="Spesialisasi", invisible=True)
        phone = fields.Char(string="Nomor Telepon", size=12)
        address = fields.Text(string="Alamat")
        practice = fields.Text(string="Jadwal Praktek")
        patient_ids = fields.One2many('klinic.patient', 'doctor_id', string="Dokter Penanggung Jawab")

        @api.constrains("phone")
        def _throw_error_digit(self):
                for line in self:
                        if line.phone.size > 12:
                                raise ValidationError("Too many digits")
