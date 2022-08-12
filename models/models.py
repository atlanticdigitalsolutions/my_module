from odoo import models, fields

class my_module(models.Model):
	_name = 'my.module'
	name = fields.Char('Nom')
	lastName=fields.Char('Prenom')
	genre=fields.Selection([('Masculin', "M"), ('Feminin', "F")])
	partner_id = fields.Many2one('res.partner', 'Partenaire')
	sale_order_ids = fields.One2many('sale.order', 'my_module_id', string="Sale orders")
	students = fields.Selection([('1', 1), ('2', 2)])
	article_id =fields.Many2one('product.template', 'Article')

class sale_order(models.Model):
	_inherit = 'sale.order'
	my_module_id = fields.Many2one('my.module')