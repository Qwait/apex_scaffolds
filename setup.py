from setuptools import find_packages
from setuptools import setup

version = '0.9.0'

setup(
    version=version,
    name='Apex Scaffolds',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    entry_points = """\
        [paste.paster_create_template]
        raja=apex_scaffolds:RajaTemplate
    """
)