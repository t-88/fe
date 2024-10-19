from setuptools import setup

setup(
    name='fe',
    version='0.1',
    py_modules=['main'],  
    entry_points={
        'console_scripts': [
            'fe=main:main',  # 'your-script' will be the command to run it
        ],
    },
)