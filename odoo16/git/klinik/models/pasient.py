from odoo import fields, models, api
from datetime import date
from odoo.exceptions import ValidationError


# CREATE MODUL KLINIC.PATIENT
class Patient(models.Model):
    _name = "klinic.patient"
    _description = "Klinic Patient"

    nomor_antrian = fields.Char(string="Nomor Antrian")
    name = fields.Char(string="Nama Lengkap", required=True)
    birth_date = fields.Date(string="Tanggal Lahir", required=True)
    gender = fields.Selection([
        ("laki_laki","Laki-Laki"),
        ("perempuan","Perempuan")
    ],string="Jenis Kelamin")
    address = fields.Text(string="Alamat Pasien", required=True)
    phone_number = fields.Char(string="Nomor Telfon", required=True)
    medical_history = fields.Text(string="Riwayat Medis")
    allergy = fields.Text(string="Alergi Pasien")
    registration_date = fields.Datetime(string="Tanggal Daftar Pasient")
    status = fields.Selection([
        ("aktif","Aktif"),
        ("tidak aktif","Tidak Aktif"),
        ("dll","DLL")
    ],string="Status")
    doctor_id = fields.Many2one('klinic.doctor', string="Dokter Penanggung Jawab")


    # ADD WIDGET
    class wizard_comment(models.Model):

        _name = "klinic.comment.wizard"
        _description = "Comment Wizard"


        name = fields.Char(string="Name")
        komentar = fields.Char(string="Comment")



