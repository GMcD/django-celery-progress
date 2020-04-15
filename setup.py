from setuptools import setup, find_packages

version = '0.3.0'

setup(
    name='django-celery-progress',
    version=version,
    description='',
    #long_description=open('README.md').read(),
    author='Rob Golding',
    author_email='rob@robgolding.com',
    license='BSD',
    url='https://github.com/gmcd/django-celery-progress',
    download_url=(
        'https://github.com/gmcd/django-celery-progress/downloads'),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'celery',
    ],
    classifiers=[
        'Development Status :: 3 - Beta',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ],
)
