{
    "name": "Demo Accorderie Canada",
    "version": "12.0.1.0",
    "author": "TechnoLibre",
    "license": "AGPL-3",
    "website": "https://technolibre.ca",
    "depends": ["accorderie_canada_ddb_data"],
    "data": [
        "data/user_demo.xml",
        "data/accorderie_accorderie.xml",
        "data/accorderie_membre.xml",
        "data/accorderie_offre_service.xml",
        "data/accorderie_demande_service.xml",
        "data/accorderie_echange_service.xml",
    ],
    "installable": True,
    "pre_init_hook": "pre_init_hook",
}
