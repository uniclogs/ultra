import setuptools
import ultra as u

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name=u.APP_NAME,
    version=u.APP_VERSION,
    author=u.APP_AUTHOR,
    license=u.APP_LICENSE,
    description=u.APP_DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=u.APP_URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Internet :: WWW/HTTP",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis"
    ],
    install_requires=[
        "loguru",
        "Flask",
        "Flask-RESTful",
        "Flask-SQLAlchemy",
        "psycopg2",
        "python-dateutil",
        "ballcosmos",
        "pass-calculator"
    ],
    extras_require={
        "dev": [
            "setuptools",
            "wheel",
            "pytest",
            "flake8",
            "twine",
            "sphinx",
            "sphinx_rtd_theme",
        ]
    },
    python_requires='>=3.8.5',
    entry_points={
        "console_scripts": [
            f'{u.APP_NAME} = ultra.__main__:main'
        ]
    }
)
