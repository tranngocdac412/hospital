from odoo import models, fields, api, _

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    user_id = fields.Many2one('res.users',
                              string='Related User')