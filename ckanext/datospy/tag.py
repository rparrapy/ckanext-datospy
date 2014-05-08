__author__ = 'Rodrigo Parra'


__author__ = 'Rodrigo Parra'

import ckan.plugins.toolkit as toolkit
import ckan.plugins as plugins

class ParaguayTagPlugin(plugins.SingletonPlugin):
    '''CKAN Plugin containing theming customizations for a Paraguay CKAN instance.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.ITemplateHelpers)

    def get_helpers(self):
        return {
            'dpy_get_custom_fields': self._get_tag_count,
        }


    def _get_tag_count(self):
        pass