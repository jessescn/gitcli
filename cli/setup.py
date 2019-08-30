from setuptools import setup

setup(
    name='gitClient',
    version='2.0',
    py_modules=['gitClient'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        gitcli=gitClient:cli
    ''',
)