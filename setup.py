# coding=utf-8

plugin_identifier = "seven"

plugin_package = "octoprint_seven"

plugin_name = "OctoPrint-Seven"

plugin_version = "0.1.0"

plugin_description = "Send SMS after OctoPrint job completion."

plugin_author = "seven communications GmbH & Co. KG"

plugin_author_email = "support@seven.io"

plugin_url = "https://github.com/seven-io/octoprint"

plugin_license = "MIT"

plugin_requires = ['requests']

plugin_additional_data = []

plugin_additional_packages = []

plugin_ignored_packages = []

additional_setup_parameters = {}

from setuptools import setup

try:
    import octoprint_setuptools
except:
    print(
        "Could not import OctoPrint's setuptools, are you sure you are running that under "
        "the same python installation that OctoPrint is installed under?"
    )
    import sys

    sys.exit(-1)

setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
    identifier=plugin_identifier,
    package=plugin_package,
    name=plugin_name,
    version=plugin_version,
    description=plugin_description,
    author=plugin_author,
    mail=plugin_author_email,
    url=plugin_url,
    license=plugin_license,
    requires=plugin_requires,
    additional_packages=plugin_additional_packages,
    ignored_packages=plugin_ignored_packages,
    additional_data=plugin_additional_data,
)

if len(additional_setup_parameters):
    from octoprint.util import dict_merge

    setup_parameters = dict_merge(setup_parameters, additional_setup_parameters)

setup(**setup_parameters)
