from setuptools import setup

setup(
    name='Temperature',
    version='1.0',
    long_description=__doc__,
    packages=['app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=1.0',
        'Flask-SQLAlchemy>=2.4',
        'Flask-wtf>=0.14',
        'pymysql>=0.9'
    ]
)