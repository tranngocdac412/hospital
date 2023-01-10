from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals_list):
        res = super(ResPartner, self).create(vals_list)
        print("Working...")
        return res
class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char('Patient Name')

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name'
    _order = 'patient_name'

    def open_patient_appointments(self):
        return {
            'name': _('Appointment'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window'
        }

    def get_appointment_count(self):
        for record in self:
            count = record.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
            record.appointment_count = count

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
    appointment_count = fields.Integer(string='Appointments', compute='get_appointment_count')
    active = fields.Boolean(string='Active', default=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    user_id = fields.Many2one('res.users', string='PRO')
    email = fields.Char(string='Email')

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