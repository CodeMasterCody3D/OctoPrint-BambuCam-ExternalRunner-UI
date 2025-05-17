# coding=utf-8
from setuptools import setup

plugin_identifier = "bambucam_runner"
plugin_package = "octoprint_bambucam"
plugin_name = "OctoPrint-BambuCam Runner"
plugin_version = "0.3.0"
plugin_description = "Runs external bambucam.py script with OpenCV and displays camera stream URLs."
plugin_author = "Cody Dixon"
plugin_author_email = "codydixon71@gmail.com"
plugin_url = ""
plugin_license = "AGPLv3"
plugin_requires = ["opencv-python"]

try:
    import octoprint_setuptools
except:
    import sys
    sys.exit(-1)

setup(**octoprint_setuptools.create_plugin_setup_parameters(
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
    additional_data=["templates"]
))
