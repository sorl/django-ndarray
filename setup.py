from setuptools import setup


setup(
    name='django-ndarray',
    version='0.0.2',
    url='http://github.com/sorl/django-ndarray',
    description='Numpy n-dimensional field for Django.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mikko Hellsing',
    author_email='mikko@sumsum.se',
    packages=['ndarray'],
    include_package_data=True,
    license='ICS',
    test_suite='tests.test_all',
    install_requires=[
        'numpy>=1',
        'Django>=2',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
    ]
)
