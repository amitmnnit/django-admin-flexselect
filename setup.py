#! coding=utf8
from distutils.core import setup

setup(
    name='django-admin-flexselect',
    version='0.4.0',
    author=u'Nishad Musthafa',
    author_email='nishadmusthafa@gmail.com',
    packages=['flexselect'],
    url='https://github.com/plivo/django-admin-flexselect',
    license='Public Domain',
    description='Dynamic select fields for the Django Admin that just works combined with chosen.js.',
    long_description=open('README.markdown').read(),
    package_data={'flexselect': ['static/flexselect/js/flexselect.js']},
)
