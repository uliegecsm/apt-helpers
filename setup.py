from setuptools import setup

setup(
    name             = 'system-helpers',
    version          = '0.1',
    license          = 'MIT',
    url              = 'https://github.com/uliegecsm/system-helpers',
    install_requires = [
        'typeguard',
    ],
    packages = [
        'system_helpers.apt',
        'system_helpers.update_alternatives',
    ],
    package_dir = {
        'system_helpers.apt' : 'system_helpers/apt',
        'system_helpers.update_alternatives' : 'system_helpers/update_alternatives',
    },
    entry_points = {
        'console_scripts': [
            'apt-helpers = system_helpers.apt.script:main',
            'update-alternatives-helpers = system_helpers.update_alternatives.script:main',
        ],
    },
)
