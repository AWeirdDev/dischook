from distutils.core import setup

setup(
    name='dischook',
    version='2',
    packages=['dischook', 'dischook.components'],
    license='MIT',
    description="The best way to execute discord webhooks!",
    long_description=open('desc.md', 'r').read(),
    author='AWeirdScratcher',
    author_email = "aweirdscrather@gmail.com",
    install_requires=[
        'requests'
    ],
    keywords = ['discord', 'webhook', 'dischook', 'execute'],
    url="https://github.com/AWeirdScratcher/dischook"
)
