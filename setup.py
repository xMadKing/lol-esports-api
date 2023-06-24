from setuptools import setup, find_packages

setup(
    name='lol-esports-api',
    version='0.1',
    license='MIT',
    author="xMadKing",
    author_email='ahmad.kh.se@outlook.com',
    packages=find_packages('lol_esports_api'),
    package_dir={'': 'lol_esports_api'},
    url='https://github.com/xMadKing/lol-esports-api',
    keywords='League of legends, esports, lolesports, API',
    install_requires=[
          'requests',
      ],

)