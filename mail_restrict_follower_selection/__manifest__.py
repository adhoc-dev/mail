# Copyright (C) 2015 Therp BV <http://therp.nl>
# Copyright (C) 2017 Komit <http://www.komit-consulting.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Restrict follower selection",
    "version": "18.0.1.0.0",
    "author": "Therp BV,Creu Blanca,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Social Network",
    "website": "https://github.com/OCA/mail",
    "summary": "Define a domain from which followers can be selected",
    "depends": ["mail"],
    "data": ["data/ir_config_parameter.xml", "data/ir_actions.xml"],
    "demo": ["demo/ir_config_parameter_demo.xml"],
    "installable": True,
}
