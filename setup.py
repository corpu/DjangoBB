from distutils.core import setup

# TODO: This setup script currently creates two redundant packages - djangobb and djangobb_forum that are identical

setup(name='djangobb_forum',
    version='1.0',
    package_dir = {'djangobb_forum': 'djangobb/djangobb_forum'},
    packages=[
        'djangobb_forum', 'djangobb_forum.management', 
        'djangobb_forum.management.commands', 'djangobb_forum.markups', 
        'djangobb_forum.migrations', 'djangobb_forum.templatetags', 'djangobb_forum.tests'],
    package_data={'djangobb_forum': [
        'fixtures/*.json',
        'templates/forum/feeds/*',
        'templates/forum/lofi/*',
        'templates/forum/profile/*',
        'templates/forum/*.html',
        'templates/search/indexes/djangobb_forum/*.txt',
    ]},
)