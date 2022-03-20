from odoo import fields, models, api


class DocsTags(models.Model):
	_name = 'logimpex.docs.tags'
	_description = 'Etiquetado de Documentos'

	name = fields.Char()
	color = fields.Integer()
