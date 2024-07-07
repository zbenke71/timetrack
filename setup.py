from setuptools import setup, find_namespace_packages

setup(
    name='bennet-timetrack',
    version='0.1',
    packages=find_namespace_packages(include=['bennet.timetrack', 'bennet.timetrack.*']),
    namespace_packages=['bennet'],
    description='A simple stopwatch for measuring elapsed time, recording laps, and splits (timetrack)',
    long_description=open('bennet/timetrack/README.md').read(),
    long_description_content_type='text/markdown',
    author='Zoltán Benke',
    author_email='benke.zoltan.71@gmail.com',
    url='https://bennet.hu',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
