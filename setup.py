# setup.py
from setuptools import setup, find_packages

setup(
    name='akita-mesh-commander',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'pyserial',
    ],
    entry_points={
        'akita.plugins': [
            'mesh_commander = mesh_commander.core:MeshCommanderPlugin',
        ],
    },
)
