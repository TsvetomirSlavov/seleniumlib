try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name = 'seleniumlib',
    version = '0.3',
    description = 'Selenium extra helper library',
    author='Eleven Paths',
    author_email='ivanmar_91@hotmail.com',
    url='https://github.com/ivanprjcts/seleniumlib',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    packages=['seleniumlib', 'seleniumlib.page', 'seleniumlib.util'],
)
