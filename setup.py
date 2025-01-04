from setuptools import setup, find_packages

try:
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    name='sshcopyid',
    version='0.0.6',
    description='A Windows-friendly replacement for the Linux ssh-copy-id tool.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Meena (Menas) Erian',
    author_email='menas@portacode.com',
    url='https://github.com/meena-erian/ssh-copy-id',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'ssh-copy-id=sshcopyid.cli:main',  
        ],
    },
    classifiers=[
        'Environment :: Win32 (MS Windows)',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Networking',
    ],
    include_package_data=True,
    install_requires=[],
)
