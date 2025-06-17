{
    'name': 'SICS To-Do',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Manage advanced to-do tasks with priorities, categories, and due dates',
    'description': """
        A custom Odoo app to manage to-do tasks with advanced features like
        prioritization, due dates, categories, and a Kanban dashboard.
    """,
    'author': 'Dabala Yonas',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_task_views.xml',
        'views/todo_menu.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}