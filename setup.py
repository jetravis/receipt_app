from setuptools import setup

setup(name='receipt_app',
      version='0.1',
      description='Store receipt information',
      long_description='Handles import and storage of info from retail receipt, the receipt data is stored in json format within tinydb',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business :: Financial :: Accounting',
      ],
      keywords='receipt accounting budget',
      url='http://github.com/jetravis/receipt_app',
      author='Larry',
      author_email='lwgray@gmail.com',
      license='MIT',
      packages=['receipt_input'],
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=[
          'appdirs>=1.4.0',
          'packaging>=16.8',
          'pyparsing>=2.1.10',
          'six>=1.10.0',
          'tinydb>=3.2.2',
      ],
      include_package_data=True,
      entry_points = {
          'console_scripts': ['cart=receipt_input.cart:run'],
      },
      zip_safe=False)
