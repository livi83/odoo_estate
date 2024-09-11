# -*- coding: utf-8 -*-

from odoo import models, fields

class Estate(models.Model):
    _name = 'estate'
    _description = 'Estate Description'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
