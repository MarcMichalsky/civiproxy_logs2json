import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="civiproxy_logs2json",
    version="1.0.0",
    author="Marc Michalsky",
    author_email="michalsky@forumZFD.de",
    packages=["civiproxy_logs2json"],
    description="Translate a CiviProxy logfile into JSON format.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarcMichalsky/civiproxy_logs2json",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'cpl2j = civiproxy_logs2json.__main__:main',
        ],
    },
)
