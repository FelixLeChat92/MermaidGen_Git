from setuptools import setup, find_packages

setup(
    name='mermaid_gen',
    version='0.1.0',
    description='Un package pour générer des diagrammes Mermaid',
    author='FelixLeChat92',
    author_email='votre_email@example.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'IPython',
    ],
)