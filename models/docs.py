from odoo import fields, models, api


class Docs(models.Model):
	_name = 'logimpex.docs'
	_description = 'Gestión de Documentos'
	_rec_name = 'name'
	_order = 'name'

	name = fields.Char(string='Nombre')
	partner_id = fields.Many2one('res.partner', string='Cliente', required=True, index=True, tracking=True)
	document = fields.Binary(string='Documento', copy=False)
	document_filename = fields.Char(string='Nombre del documento', copy=False)
	document_tag = fields.Many2many('logimpex.docs.tags', string='Etiquetas', copy=False)
	note = fields.Text(string='Descripción', copy=False, tracking=True)
