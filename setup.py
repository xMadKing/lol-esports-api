from setuptools import setup, find_packages

setup(
    name='lol-esp-api',
    version='0.3',
    license='MIT',
    author="xMadKing",
    author_email='ahmad.kh.se@outlook.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/xMadKing/lol-esports-api',
    keywords='League of legends, esports, lolesports, API',
    install_requires=[
          'requests',
      ],

)