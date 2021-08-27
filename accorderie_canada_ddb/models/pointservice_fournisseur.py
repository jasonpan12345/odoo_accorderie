from odoo import _, api, models, fields


class PointserviceFournisseur(models.Model):
    _name = "pointservice.fournisseur"
    _description = "Model Pointservice_fournisseur belonging to Module Tbl"

    datemaj_pointservicefournisseur = fields.Datetime(
        string="Datemaj pointservicefournisseur"
    )

    name = fields.Char()

    nofournisseur = fields.Many2one(
        comodel_name="fournisseur",
        required=True,
    )

    nopointservice = fields.Many2one(
        comodel_name="pointservice",
        required=True,
    )
