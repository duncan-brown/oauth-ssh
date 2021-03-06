import sys
from setuptools import setup

setup(
    name='oauth_ssh',
    version=0.9,
    description='SSH with OAuth Tokens',
    long_description=open("README.rst").read(),
    url='https://github.com/xsede/oauth-ssh',
    author="Jason Alt",
    author_email='jasonalt@gmail.com',
    packages=['oauth_ssh'],

    # Only enforced with setuptools 24.2.0+ and pip 9.0.0+
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',

    install_requires=[
        'requests>=2.21.0,<3.0',
        'click>=6.7,<7.0',
        # paramiko 2.4.2 plus newer cryptography results in unnecessary
        # deprecation warnings. paramiko recommends downgrading cryptography
        # until the new verison of paramiko (>2.4.2) is available.
        'cryptography==2.4.2',
        'paramiko>=2.4.2',
    ],

    entry_points='''
        [console_scripts]
        oauth-ssh=oauth_ssh.oauth_ssh:oauth_ssh
        oauth-ssh-token=oauth_ssh.oauth_ssh_token:oauth_ssh_token
    ''',

    keywords=["oauth", "ssh"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: POSIX",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
    ],
)
