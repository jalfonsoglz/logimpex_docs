from odoo import fields, models, api


class Docs(models.Model):
	_name = 'logimpex.docs'
	_description = 'Gestión de Documentos'

	name = fields.Char()
	partner_id = fields.Many2one('res.partner', string='Cliente', required=True, index=True, tracking=True)
	document = fields.Binary(string='Documento', required=True, index=True)
	document_filename = fields.Char(string='Nombre del documento')
	document_tag = fields.Many2many('logimpex.docs.tags', string='Etiquetas')
	note = fields.Text(string='Descripción', copy=False, tracking=True)
