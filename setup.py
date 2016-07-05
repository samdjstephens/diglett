from setuptools import setup, find_packages


setup(
    name='diglett',
    version='0.1',
    url='https://github.com/samdjstephens/diglett',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'docopt'
    ],
    scripts=['diglett/diglett']
)
