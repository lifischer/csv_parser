from setuptools import setup 

setup(
    name='CSV Parser',
    version='0.1',
    py_modules=['csv_parser'],
    install_requires=[
        'Click', 'pandas'],
    entry_points='''
        [console_scripts]
        csv_parser=csv_parser:cli
    ''',
)
# to install the programm 
# python setup.py install
# python csv_parser plot data/oktoberfest...