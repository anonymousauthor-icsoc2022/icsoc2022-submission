from setuptools import setup, find_packages

setup(name='icsoc-2022',
      version='0.1.0',
      description='Implementation of stochastic service composition.',
      url='',
      author='Anonymous Author',
      author_email='anonymousauthor@email.com',
      license='MIT',
      packages=find_packages(include='icsoc_2022*'),
      zip_safe=False,
      install_requires=[
            "numpy",
            "graphviz",
            "websockets",
            "paho-mqtt",
            "requests",
            "logaut",
      ]
)
