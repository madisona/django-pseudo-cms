from setuptools import setup, find_packages


from pseudo_cms import VERSION

setup(
    name="django-pseudo-cms",
    version=VERSION,
    author="Aaron Madison",
    description="A Simple application to help add dynamic content to pages.",
    long_description=open('README.rst', 'r').read(),
    url="https://github.com/madisona/django-pseudo-cms",
    packages=find_packages(exclude=["example"]),
    install_requires=open('requirements/requirements.txt').read().split('\n'),
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
