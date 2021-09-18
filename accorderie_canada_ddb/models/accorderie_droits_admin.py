from odoo import _, api, models, fields


class AccorderieDroitsAdmin(models.Model):
    _name = "accorderie.droits.admin"
    _description = "Accorderie Droits Admin"

    consulter_etat_compte = fields.Boolean(string="Consulter état de compte")

    consulter_profil = fields.Boolean(string="Consulter profil")

    gestion_dmd = fields.Boolean(string="Gestion demande de services")

    gestion_fichier = fields.Boolean(string="Gestion fichier")

    gestion_offre = fields.Boolean(string="Gestion offre")

    gestion_offre_service = fields.Boolean(string="Gestion offre de services")

    gestion_profil = fields.Boolean(string="Gestion profil")

    gestion_type_service = fields.Boolean(string="Gestion type de services")

    groupe_achat = fields.Boolean(string="Groupe d'achat")

    membre = fields.Many2one(comodel_name="accorderie.membre")

    name = fields.Char()

    saisie_echange = fields.Boolean(string="Saisie échange")

    validation = fields.Boolean()
