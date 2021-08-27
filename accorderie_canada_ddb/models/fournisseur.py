from odoo import _, api, models, fields


class Fournisseur(models.Model):
    _name = "fournisseur"
    _description = "Model Fournisseur belonging to Module Tbl"

    adresse = fields.Char()

    codepostalfournisseur = fields.Char()

    courrielcontact = fields.Char()

    courrielfournisseur = fields.Char()

    datemaj_fournisseur = fields.Datetime(string="Datemaj fournisseur")

    faxfounisseur = fields.Char()

    name = fields.Char()

    noaccorderie = fields.Many2one(
        comodel_name="accorderie",
        required=True,
    )

    nomcontact = fields.Char()

    nomfournisseur = fields.Char()

    noregion = fields.Many2one(
        comodel_name="region",
        required=True,
    )

    notefournisseur = fields.Text()

    noville = fields.Many2one(
        comodel_name="ville",
        required=True,
    )

    postecontact = fields.Char()

    telfournisseur = fields.Char()

    visible_fournisseur = fields.Integer(string="Visible fournisseur")
