from os import environ

SESSION_CONFIGS = [
    dict(
       name='leave_wait_page',
       display_name="Leave group matching page after X seconds if no match is found",
       num_demo_participants=3,
       app_sequence=['leave_wait_page']
    ),
    dict(
       name='dropout_example',
       display_name="Reduce waiting times by 'fast-forwarding' if a timeout occurs",
       num_demo_participants=4,
       app_sequence=['dropout_example']
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '&+l3g($!(yzmnpkei0*s6670t=#fzv_nzu-^qn(efj7q26ufpk'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
