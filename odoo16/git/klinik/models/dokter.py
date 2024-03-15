from odoo import fields, models

class Dokter(models.Model):
        _name = "klinic.doctor"
        _description = "Klinic Doctor"

        name = fields.Char(string="Nama", required=True)
        specialization = fields.Char(string="Spesialisasi")
        phone = fields.Char(string="Nomor Telepon", required=True)
        address = fields.Text(string="Alamat", required=True)
        practice = fields.Text(string="Jadwal Praktek")
        patient_ids = fields.One2many('klinic.patient', 'doctor_id', string="Pasien yang Ditangani")
