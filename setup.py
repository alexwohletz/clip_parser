from setuptools import setup,find_packages
setup(
    name='clip_parser',
    packages=find_packages(),
    install_requires= ['pyperclip','pandas','pynput','tabulate'],
    version='0.1.0',
    description='Simple clipboard utilities program',
    author='Alex Wohletz',
    license='MIT',
    author_email='alex.wohletz@phtech.com',

)
