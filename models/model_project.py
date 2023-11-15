from odoo import models, fields, api


class appschef_project(models.Model):
    _name = "appschef.appschef_project"
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
