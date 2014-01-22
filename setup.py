import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
INSTALL_REQUIREMENTS = ["pydenticon", "django"]
TEST_REQUIREMENTS = []

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-pydenticon',
    version='0.1',
    packages=find_packages(exclude=["testproject", "testproject.*"]),
    include_package_data=True,
    license='BSD',
    description='Django application providing generated identicons to the web.',
    long_description=README,
    url='https://github.com/azaghal/django-pydenticon',
    author='Branko Majic',
    author_email='branko@majic.rs',
    install_requires=INSTALL_REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries',
    ],
)
