# -*- coding: utf-8 -*-
{
    'name': "Logimpex Documents Add-on",

    'summary': """Módulo de Gestión de Documentos Logimpex""",

    'description': """
    
    """,
    'author': "Alfonso Gonzalez (alfonso@ptree.com.mx)",
    'website': "https://ptree.com.mx/",
    'category': 'Customizations',
    'version': '15.0.0.0.1',
    'license': "AGPL-3",
    'sequence': "-97",
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/docs.xml',
        'views/docs_tags.xml',
        'data/partner_docs.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
