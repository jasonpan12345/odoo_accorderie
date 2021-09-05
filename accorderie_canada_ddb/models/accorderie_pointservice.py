from odoo import _, api, models, fields


class AccorderiePointservice(models.Model):
    _name = "accorderie.pointservice"
    _description = "Accorderie Pointservice"
    _rec_name = "nom"

    datemaj_pointservice = fields.Datetime(string="Datemaj pointservice")

    membre = fields.One2many(
        comodel_name="accorderie.membre",
        inverse_name="point_service",
        help="Membre relation",
    )

    noaccorderie = fields.Many2one(
        comodel_name="accorderie.accorderie",
        required=True,
    )

    nom = fields.Char(help="Nom du point de service")

    notegrpachatpageclient = fields.Text()

    ordrepointservice = fields.Integer()
