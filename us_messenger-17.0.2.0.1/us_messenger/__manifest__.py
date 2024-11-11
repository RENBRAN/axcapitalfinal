{
    "name": """Messengers""",
    "summary": """Messengers integration powered by UnitSoft""",
    "category": "Extra Tools",
    "images": ["static/description/messengers_image.png"],
    "version": "17.0.2.0.1",
    "application": True,
    "author": "UnitSoft",
    "support": "",
    "website": "https://unitsoft.com.ua/",
    "license": "LGPL-3",
    "price": 0,
    "currency": "EUR",
    "depends": ["base_automation", "mail", "queue_job", "base", "crm", "us_multichat"],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "security/us_messenger_groups.xml",
        "security/ir.model.access.csv",
        "views/us_messenger_menus.xml",
        "views/ir_logging_views.xml",
        "views/us_messenger_job_views.xml",
        "views/us_messenger_trigger_cron_views.xml",
        "views/us_messenger_trigger_automation_views.xml",
        "views/us_messenger_trigger_webhook_views.xml",
        "views/us_messenger_trigger_button_views.xml",
        "views/us_messenger_task_views.xml",
        "views/us_messenger_project_views.xml",
        "views/us_messenger_link_views.xml",
        "wizard/us_messenger_mass_mailing.xml",
        "views/res_partner_views.xml",
        "views/mail_message.xml",
        "data/queue_job_function_data.xml",
    ],
    "assets":{
        "web.assets_backend" : [
            "us_messenger/static/src/core/common/*",
            'us_messenger/static/src/core/web/*'
        ],
    },
    "qweb": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": True,
}
