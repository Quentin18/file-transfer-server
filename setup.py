"""
Install using pip: pip3 install .
"""
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='file-transfer-server',
    version='0.0.1',
    description='Simple file transfer server in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Quentin Deschamps',
    author_email='quentindeschamps18@gmail.com',
    url='https://github.com/Quentin18/file-transfer-server',
    packages=['filetransfer'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    license='MIT',
    keywords='file transfer server',
    project_urls={
        'Source Code': 'https://github.com/Quentin18/file-transfer-server',
    },
    platforms=['any'],
    include_package_data=True,
    zip_safe=True,
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        filetransfer=filetransfer.cli:cli
    ''',
    python_requires='>=3',
)
