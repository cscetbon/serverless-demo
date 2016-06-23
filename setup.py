from setuptools import setup

# from pennstation import __version__
__version__ = "0.1.0"

def read_requirements(path):
    requirements = []
    validate = lambda req: req and not req.startswith('-')
    with open(path, 'rb') as fd:
        requirements = [req.strip() for req in fd.readlines() if validate(req)]
    return requirements

install_requires = read_requirements('dev-requirements.txt')
tests_require = install_requires

setup(
    name='etl-demo',
    version=__version__,
    url='',
    author='',
    author_email='',
    description='',
    long_description=__doc__,
    packages=['image'],
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={}
)

