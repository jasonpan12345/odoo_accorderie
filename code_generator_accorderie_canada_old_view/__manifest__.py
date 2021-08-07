{
    "name": "Code Generator Accorderie Canada Old View",
    "version": "12.0.1.0",
    "author": "TechnoLibre",
    "license": "AGPL-3",
    "website": "https://technolibre.ca",
    "application": True,
    "depends": [
        "code_generator",
        "code_generator_hook",
        "accorderie_canada_ddb",
    ],
    "installable": True,
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
}
