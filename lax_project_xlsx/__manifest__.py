{
    'name': "Project xlsx Report",
    'summary': """This module allows to xlsx report of Project from the form view.""",
    'author': "Laxicon Solution",
    'website': "www.laxicon.in",
    'sequence': 101,
    'support': 'info@laxicon.in',
    'category': 'Project',
    'version': '16.0.1',
    'license': 'AGPL-3',
    'description': """This module allows to Xlsx Report of Project from the form view.
    """,
    'depends': ['project', 'report_xlsx'],
    'data': [
        "report/project_xlsx_view.xml",
    ],
    'images':  ["static/description/banner.png"],
    'installable': True,
    'auto_install': False,
    'application': True,
}
