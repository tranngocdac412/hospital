from odoo import models, fields, api, _

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'appointment'

    name = fields.Char(string='Appointment ID',
                       required=True,
                       copy=False,
                       readonly=True,
                       index=True,
                       default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient',
                                 string='Patient',
                                 required=True)
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    notes = fields.Text(string='Registration note')
    appointment_date = fields.Date(string='Date', required=True)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result