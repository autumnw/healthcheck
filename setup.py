from setuptools import setup, find_packages
import sys, os

version = '1.0.1'

setup(name='healthcheck',
      version=version,
      description="Provide a health check for health master-slave node",
      long_description="""\
Provide a health check for health master-slave node""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Autumn Wang',
      author_email='shoujinwang@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      scripts=['bin/healthcheck'],
      data_files=[('/etc/init.d', ['bin/healthcheckd']),
                  ('/etc/healthcheck', ['conf/config.json', 'conf/logging.json', 'conf/detect.sh'])],
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
