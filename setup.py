from setuptools import setup, find_packages

REQUIREMENTS = (
    'Django>=1.4',
    'django-image-helper>=0.1.1',
    'docutils==0.8.1',
)

from pseudo_cms import VERSION

setup(
    name="django-pseudo-cms",
    version=VERSION,
    author="Aaron Madison",
    description="A Simple application to help add dynamic content to pages.",
    long_description=open('README.rst', 'r').read(),
    url="https://github.com/madisona/django-pseudo-cms",
    packages=find_packages(exclude=["example"]),
    install_requires=REQUIREMENTS,
    zip_safe=False,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
