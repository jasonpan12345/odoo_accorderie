from odoo import _, api, models, fields


class Pointservice(models.Model):
    _name = "pointservice"
    _description = "Model Pointservice belonging to Module Tbl"

    datemaj_pointservice = fields.Datetime(string="Datemaj pointservice")

    name = fields.Char()

    noaccorderie = fields.Many2one(
        comodel_name="accorderie",
        required=True,
    )

    nomembre = fields.Many2one(comodel_name="membre")

    nompointservice = fields.Char()

    nopointservice = fields.Integer(required=True)

    notegrpachatpageclient = fields.Text()

    ordrepointservice = fields.Integer()
