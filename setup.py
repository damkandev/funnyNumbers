from setuptools import setup, find_packages

setup(
    name='FunnyNumbers',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/damkandev/damkandev',
    license='MIT',
    author='Damkan',
    author_email='damkancontacto@gmail.com',
    description='Evita los numeros chistosos y con rimas.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
