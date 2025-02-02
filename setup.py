from setuptools import setup, find_packages

setup(
    name='rice-disease-classification',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'plotly',
        'statsmodels',
        'pmdarima',
        'gunicorn',
        'flask',
        'xgboost',
        'Flask-SQLAlchemy',
        'streamlit',
        'click',
        'Sphinx',
        'coverage',
        'awscli',
        'flake8',
        'python-dotenv>=0.5.1',
        'torch',
        'torchvision',
        'pillow'
    ],
)
