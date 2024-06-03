from odoo import api, fields, models


class Fish(models.Model):
    _name = 'module_inventory.fish'
    _description = 'Test Fish stock'

    order = fields.Integer(string="ลำดับที่")
    product_name = fields.Char(string='ชื่อสินค้า')
    description = fields.Char(string='คำอธิบายสินค้า')
    protein_percent = fields.Float(string='โปรตีน(%)')

