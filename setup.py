from setuptools import setup, find_packages

setup(
    name='jemma',
    version='0.1.4200',
    description='convert ideas into code',
    author='tolitius',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jemma = jemma.huddle:main',
        ],
    },
    install_requires=[
        'python-dotenv==1.0.1',
        'anthropic==0.21.3',
        'openai==1.14.3',
        'ollama==0.1.8',
        'replicate==0.25.1',
    ],
)
