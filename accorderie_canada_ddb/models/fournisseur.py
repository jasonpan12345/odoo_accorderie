from odoo import _, api, models, fields


class Fournisseur(models.Model):
    _name = "fournisseur"
    _description = "Model Fournisseur belonging to Module Tbl"

    adresse = fields.Char(string="Field Adresse")

    codepostalfournisseur = fields.Char(string="Field Codepostalfournisseur")

    courrielcontact = fields.Char(string="Field Courrielcontact")

    courrielfournisseur = fields.Char(string="Field Courrielfournisseur")

    datemaj_fournisseur = fields.Datetime(string="Field Datemaj_fournisseur")

    faxfounisseur = fields.Char(string="Field Faxfounisseur")

    name = fields.Char(string="Field Name")

    noaccorderie = fields.Integer(
        string="Field Noaccorderie",
        required=True,
    )

    nofournisseur = fields.Integer(
        string="Field Nofournisseur",
        required=True,
    )

    nomcontact = fields.Char(string="Field Nomcontact")

    nomfournisseur = fields.Char(string="Field Nomfournisseur")

    noregion = fields.Integer(
        string="Field Noregion",
        required=True,
    )

    notefournisseur = fields.Text(string="Field Notefournisseur")

    noville = fields.Integer(
        string="Field Noville",
        required=True,
    )

    postecontact = fields.Char(string="Field Postecontact")

    telfournisseur = fields.Char(string="Field Telfournisseur")

    visible_fournisseur = fields.Integer(string="Field Visible_fournisseur")
