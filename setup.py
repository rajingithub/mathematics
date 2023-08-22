import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mathematics',
    version='0.0.1',
    author='Mahender',
    author_email='',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/rajingithub/mathematics',
    license='MIT',
    packages=['mathematics'],
    install_requires=['requests'],
)
