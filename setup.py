from setuptools import setup

setup(
    name='MicroFlack-Common',
    description='Common MicroFlack classes and functions',
    version='0.6',
    packages=['microflack_common'],
    install_requires=[
        'cachetools',
        'docker',
        'flask-httpauth',
        'kazoo',
        'python-etcd',
        'pyjwt'
    ]
)
