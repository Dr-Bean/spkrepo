# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


tests_require = ['Flask-Testing',
                 'factory-boy', 'Faker',
                 'lxml', 'urltools',
                 'coveralls']

install_requires = ['Flask',
                    'Flask-SQLAlchemy',
                    'Flask-Security',
                    'Flask-Admin==1.0.8', 'Pillow',
                    'Flask-RESTful',
                    'Flask-Cache', 'redis',
                    'python-gnupg', 'requests',
                    'Flask-Migrate', 'alembic>=0.7.0',
                    'Flask-Script',
                    'Flask-DebugToolbar']

dev_requires = ['sphinx', 'sphinx_rtd_theme']


setup(
    name='spkrepo',
    version='0.1',
    license='MIT',
    url='https://github.com/Diaoul/spkrepo',
    description='Synology Package Repository',
    long_description=open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
    author='Antoine Bertin',
    author_email='diaoulael@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: System :: Archiving :: Packaging'
    ],
    install_requires=install_requires,
    test_suite='spkrepo.tests.suite',
    tests_require=tests_require,
    extras_require={'tests': tests_require,
                    'dev': tests_require + dev_requires}
)
