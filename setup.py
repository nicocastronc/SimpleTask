from setuptools import setup, find_packages

setup(
    name="simpletask",
    version="0.1",
    packages=find_packages(),
    description="Library for scheduled tasks in Python (like Celery but simpler). Ideal for scripts, Django, and small projects.",
    author="Nicolás Castro (nicocastronc)",
    install_requires=[],  # Zero dependencies.
    python_requires=">=3.6",
)
