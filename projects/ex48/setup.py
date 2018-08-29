try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Zhen Cao',
    'url': '',
    'download_url': '',
    'author_email': 'fiocz09@gmail.com',
    'version': '0.1',
    'install_requirements': ['nose'],
    'packages': ['lexicon'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
