__author__ = 'Rodrigo Parra'

import ckan.controllers.package as package
import ckan.plugins.toolkit as toolkit
import ckan.plugins as plugins
import json
from logging import getLogger

log = getLogger(__name__)


class ParaguayDatasetFormPlugin(plugins.SingletonPlugin,
                             toolkit.DefaultDatasetForm, package.PackageController):
    """
    Custom dataset form plugin.
    """

    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IPackageController)

    _custom_fields = ['valid_from', 'valid_until', 'valid_spatial', 'update_frequency']



    def get_helpers(self):
        return {
            'dpy_get_custom_fields': self._get_custom_fields,
        }

    def _get_custom_fields(self):
        return self._custom_text_fields

    def is_fallback(self):
        return True

    def package_types(self):
        return []

    def _modify_package_schema_for_edit(self, schema):
        log.debug('Edit package!')
        for field_name in self._custom_fields:
            schema[field_name] = [toolkit.get_validator('ignore_missing'),
                    toolkit.get_converter('convert_to_extras')]

    def _modify_package_schema_for_read(self, schema):
        log.debug('Show package!')
        for field_name in self._custom_fields:
            schema[field_name] = [toolkit.get_converter('convert_from_extras'),
                toolkit.get_validator('ignore_missing')]

    def create_package_schema(self):
        schema = super(ParaguayDatasetFormPlugin, self).create_package_schema()
        self._modify_package_schema_for_edit(schema)
        return schema

    def update_package_schema(self):
        schema = super(ParaguayDatasetFormPlugin, self).update_package_schema()
        self._modify_package_schema_for_edit(schema)
        #log.debug(schema)
        return schema

    def show_package_schema(self):
        log.debug('Show package!')
        schema = super(ParaguayDatasetFormPlugin, self).show_package_schema()
        ## todo: Do not remove custom fields from extras when rendering!
        ## but this is used when loading the model too...
        self._modify_package_schema_for_read(schema)
        #log.debug(schema)
        return schema


    ##############################################################################

    def read(self, entity):
        log.debug('read')

    def create(self, entity):
        log.debug('create')


    def edit(self, entity):
        log.debug('edit')


    def authz_add_role(self, object_role):
        log.debug('authz_add_role')

    def authz_remove_role(self, object_role):
        log.debug('authz_remove_role')

    def delete(self, entity):
        log.debug('delete')

    def after_create(self, context, pkg_dict):
        log.debug('Creooooooo')
        return pkg_dict

    def after_update(self, context, pkg_dict):
        return pkg_dict

    def after_delete(self, context, pkg_dict):
        return pkg_dict

    def after_show(self, context, pkg_dict):
        return pkg_dict

    def before_search(self, search_params):
        return search_params

    def after_search(self, search_results, search_params):
        return search_results

    def before_index(self, pkg_dict):
        log.debug('Indeeeeexxxx')
        data_dict = json.loads(pkg_dict['data_dict'])
        extras_name = set()
        extras_description = set()
        extras_attributes = set()
        extras_values = set()

        for resource in data_dict['resources']:
            log.debug(resource)
            if 'schema' in resource:
                try:
                    schema = json.loads(resource['schema'])
                    for field in schema['fields']:
                        extras_name.add(field['name'])
                        extras_description.add(field['description'])
                except ValueError:
                    log.info("Entry 'schema' is not valid JSON. This should not happen.")
                except KeyError:
                    log.info("JSON Table Schema syntax problem.")

            if 'dynamic' in resource:
                try:
                    for attr in json.loads(resource['dynamic']):
                        extras_attributes.add(attr['key'])
                        extras_values.add(attr['value'])
                except ValueError:
                    log.info("Entry 'dynamic' is not valid JSON. This should not happen.")
                except KeyError:
                    log.debug(json.loads(resource['dynamic']))
                    log.info("Syntax problem. 'key' and 'value' are mandatory for each attribute.")

        pkg_dict['extras_name'] = ' '.join(extras_name)
        pkg_dict['extras_description'] = ' '.join(extras_description)
        pkg_dict['extras_attributes'] = ' '.join(extras_attributes)
        pkg_dict['extras_values'] = ' '.join(extras_values)

        return pkg_dict

    def before_view(self, pkg_dict):
        return  pkg_dict
