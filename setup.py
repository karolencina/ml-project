from setuptools import setup, find_packages

setup (
    name='ml-project',
    version='0.0.1',  
    description='ML project created for learning.',
    author='Karo Lencina',
    author_email='karolencina@icloud.com',
    url='https://github.com/karolencina/ml-project.git',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'requests',
    ],
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    long_description=open('README.md').read(),
)