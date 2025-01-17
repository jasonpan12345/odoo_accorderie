{
    "name": "Accorderie website",
    "category": "Website",
    "version": "12.0.1.0",
    "author": "TechnoLibre",
    "license": "AGPL-3",
    "website": "https://technolibre.ca",
    "depends": ["website", "accorderie_canada_ddb"],
    "data": [
        "data/ir_attachment.xml",
        "data/ir_ui_view.xml",
        "data/website_page.xml",
        "data/website_menu.xml",
        "views/portal_templates.xml",
        "views/webclient_templates.xml",
    ],
    "installable": True,
    "pre_init_hook": "pre_init_hook",
}
