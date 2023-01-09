from odoo import models, fields, api, _

class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_date = fields.Date(string='Appointment Date')

    def create_appointment(self):
        pass
        new_data = {}
        new_data['patient_id'] = self.patient_id.id
        new_data['appointment_date'] = self.appointment_date
        self.env['hospital.appointment'].sudo().create(new_data)