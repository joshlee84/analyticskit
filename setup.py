from setuptools import setup

setup(
    name='analyticskit',
    version='0.1.0',
    description='Package for use in data analytics tasks',
    url='https://github.com/joshlee84/analyticskit',
    author='Josh Lee',
    author_email='joshlee84@byu.edu',
    license='MIT',
    packages=['analyticskit'],
    install_requires=[
        'requests',
        'pypdf',
        'pandas',
        'selenium',
        'tk',
        'numpy',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
)