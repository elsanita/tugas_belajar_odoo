# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TestModel(models.Model):
    _name = "test.model"
    _description = "model for karyawan"

    name = fields.Char("Name")
    
