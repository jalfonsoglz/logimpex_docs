from odoo import fields, models, api


class Docs(models.Model):
	_inherits = {
		'ir.attachment': 'ir_attachment_id',
	}
	_name = 'logimpex.docs'
	_description = 'Gestión de Documentos'
	_rec_name = 'name'
	_order = 'name'

	name = fields.Char(string='Nombre')
	partner_id = fields.Many2one('res.partner', string='Cliente', required=True, index=True, tracking=True)
	document = fields.Many2one('ir.attachment', string='Documento', required=True, ondelete='cascade')
	document_filename = fields.Char(string='Nombre del documento')
	document_tag = fields.Many2many('logimpex.docs.tags', string='Etiquetas')
	note = fields.Text(string='Descripción', copy=False, tracking=True)

	def unlink(self):
		self.mapped('ir_attachment_id').unlink()
		return super(Docs, self).unlink()
