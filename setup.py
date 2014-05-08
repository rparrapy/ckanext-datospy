from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-datospy',
    version=version,
    description="CKAN Extension with containing customizations for a Paraguay CKAN instance.",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Rodrigo Parra',
    author_email='rodpar07@gmail.com',
    url='',
    license='Affero GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.datospy'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        paraguay_theme=ckanext.datospy.theme:ParaguayThemePlugin
        paraguay_dataset = ckanext.datospy.dataset:ParaguayDatasetFormPlugin
        paraguay_resource = ckanext.datospy.resource:ParaguayResourceFormPlugin
    ''',
)
