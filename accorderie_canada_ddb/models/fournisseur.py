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

    noaccorderie = fields.Integer(required=True)

    nofournisseur = fields.Integer(required=True)

    nomcontact = fields.Char()

    nomfournisseur = fields.Char()

    noregion = fields.Integer(required=True)

    notefournisseur = fields.Text()

    noville = fields.Integer(required=True)

    postecontact = fields.Char()

    telfournisseur = fields.Char()

    visible_fournisseur = fields.Integer(string="Visible fournisseur")
