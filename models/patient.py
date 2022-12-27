from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char('Patient Name')

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name'

    patient_name = fields.Char('Name', required=True)
    patient_age = fields.Integer('Age', track_visibility='always')
    age_group = fields.Selection([('major', 'Major'), ('minor', 'Minor')], 'Age Group', compute='_compute_age_group')
    notes = fields.Text('Notes')
    image = fields.Binary('Image')
    name = fields.Char('Test')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], 'Gender')
    name_seq = fields.Char(string='Order Reference',
                           required=True,
                           copy=False,
                           readonly=True,
                           index=True,
                           default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New') == _('New')):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result

    @api.depends('patient_age')
    def _compute_age_group(self):
        for record in self:
            if record.patient_age:
                if record.patient_age < 18:
                    record.age_group = 'minor'
                else:
                    record.age_group = 'major'

    @api.constrains('patient_age')
    def _check_age_gt5(self):
        for record in self:
            if record.patient_age <=5:
                raise ValidationError(_('The age must be greater than 5'))