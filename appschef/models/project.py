# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AppschefProject(models.Model):
    _name = "project"
    _description = "model for projects"

    name = fields.Char()
    teknologi = fields.Selection(
        [
            ("py", "Python"),
            ("kt", "Kotlin"),
            ("java", "Java"),
            ("dart", "Dart"),
            ("goolang", "Goolang"),
        ]
    )
    tipe_project = fields.Selection(
        [
            ("et", "Extended Team"),
            ("fb", "Fixed Bid"),
            ("dt", "Dedicated Team"),
        ]
    )
