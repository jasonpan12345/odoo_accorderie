from odoo import _, api, models, fields


class Pointservice(models.Model):
    _name = "pointservice"
    _description = "Model Pointservice belonging to Module Tbl"
    _rec_name = "nom"

    datemaj_pointservice = fields.Datetime(string="Datemaj pointservice")

    noaccorderie = fields.Many2one(
        comodel_name="accorderie",
        required=True,
    )

    nom = fields.Char(help="Nom du point de service")

    notegrpachatpageclient = fields.Text()

    ordrepointservice = fields.Integer()
