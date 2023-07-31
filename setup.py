from setuptools import setup, find_packages

setup(
    name='gmass-campaign-stats',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests==2.28.2',
        'numpy==1.24.2',
        'matplotlib==3.7.1',
        'streamlit==1.22.0',
    ],

    author='Shubhkarman Pruthi',
    author_email='shubhpruthi2004@gmail.com',
    description='This program is a simple Streamlit app that allows users to track and visualize the email open rates for campaigns using the GMass API.',
    url='https://github.com/p116/gmass-campaign-stats',
)