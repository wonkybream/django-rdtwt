import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="django-rdtwt",
    version="3.0.0",
    license="MIT",
    author="Sampo Lavinen",
    description="Run Django tests with testcontainers.",
    long_description=(here / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/wonkybream/django-rdtwt",
    packages=find_packages(exclude=["tests"]),
    keywords=[
        "django",
        "testing",
        "testcontainers",
        "docker",
        "test automation",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "testcontainers",
        "Django",
        "psycopg",
    ],
    python_requires=">=3.10",
)
