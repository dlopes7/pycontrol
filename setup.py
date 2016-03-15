from setuptools import setup

setup(
    name='pycontrol',
    description='Library for F5 iControl API',
    long_description="""pyControl is a Python-based library that integrates
                        with F5's BIG-IP iControl management API.""",
    version='3.0',
    license='GPL',
    author='David Lopes',
    author_email='davidribeirolopes@gmail.com',
    url='https://github.com/dlopes7/pycontrol',
    keywords='iControl F5 API',
    #py_modules=['pycontrol'],
    packages=['pycontrol',],
    install_requires=['distribute', 'suds-py3'],
    platforms='any',
    classifiers=[
        'Operating System :: OS Independent',
    ],
)
