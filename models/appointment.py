from odoo import models, fields, api, _

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'appointment'
    _order = 'name desc'

    def action_confirm(self):
        for record in self:
            record.state = 'confirm'
    def action_done(self):
        for record in self:
            record.state = 'done'
    def _get_default_note(self):
        return "Default note"

    def _get_default_patient(self):
        hospital = self.env['hospital.patient'].sudo().search([('id', '=', 1)])
        if hospital:
            return hospital.id
        return

    name = fields.Char(string='Appointment ID',
                       required=True,
                       copy=False,
                       readonly=True,
                       index=True,
                       default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient',
                                 string='Patient',
                                 required=True,
                                 default=_get_default_patient)
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    notes = fields.Text(string='Registration note', default=_get_default_note)
    appointment_date = fields.Date(string='Date', required=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirm'),
                              ('done', 'Done'),
                              ('cancelled', 'Cancelled')],
                             string='Status',
                             default='draft')
    doctor_note = fields.Text(string='Note')
    pharmacy_note = fields.Text(string='Note')
    appointment_lines = fields.One2many('hospital.appointment.lines', 'appointment_id', string='Appointment Lines')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

class HospitalAppoinmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Appointment Lines'

    product_id = fields.Many2one('product.product', string='Medicine')
    product_qty = fields.Integer(string='Quantity')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment ID')