from odoo import _, api, fields, models


class AccorderieWorkflowState(models.Model):
    _name = "accorderie.workflow.state"
    _description = "Accorderie Workflow State"

    name = fields.Char(string="Nom")

    breadcrumb_show_only_last_item = fields.Boolean(
        string="Fil d'ariane affiché dernier item seulement"
    )

    breadcrumb_value = fields.Char(string="Contenu fil d'ariane")

    data = fields.Char(string="Nom base de données")

    submit_button_text = fields.Char(string="Libellé du bouton envoie")

    diagram_id = fields.Many2one(
        comodel_name="accorderie.workflow",
        string="Diagram",
    )

    disable_question = fields.Boolean(string="Désactiver la question")

    key = fields.Char(string="Identifiant", required=True)

    list_is_first_position = fields.Boolean(
        string="Première position dans la sélection"
    )

    message = fields.Char()

    model_field_name = fields.Char(string="Champs du modèle")

    model_field_name_alias = fields.Char(string="Alias champs du modèle")

    show_breadcrumb = fields.Boolean(string="Afficher le fil d'ariane")

    state_dst_ids = fields.One2many(
        comodel_name="accorderie.workflow.relation",
        inverse_name="state_dst",
        string="Relation destination",
    )

    state_src_ids = fields.One2many(
        comodel_name="accorderie.workflow.relation",
        inverse_name="state_src",
        string="Relation source",
    )

    type = fields.Selection(
        selection=[
            ("selection_static", "Sélection statique"),
            ("selection_dynamique", "Sélection dynamique"),
            ("choix_categorie_de_service", "Choix catégorie de service"),
            ("choix_membre", "Choix membre"),
            ("calendrier", "Calendrier"),
            ("temps", "Temps"),
            ("form", "Form"),
        ]
    )

    xpos = fields.Integer(
        string="Diagram position x",
        default=50,
    )

    ypos = fields.Integer(
        string="Diagram position y",
        default=50,
    )
