from setuptools import setup

setup(name='django-email-kit',
      version='0.1',
      description='A toolkit for common e-mail tasks like processing a "contact us" form.',
      long_description=file('README.txt').read(),
      author='Michaux Kelley',
      author_email='michauxkelley@gmail.com',
      package_dir={'emailkit': 'emailkit'},
      data_files=[('', ['README.txt'])],
      license='MIT',
      url='https://github.com/mkelley33/django-email-kit',
      keywords='django email contact forms',
      classifiers=["Development Status :: 1 - Planning",
                   "Operating System :: OS Independent",
                   "Framework :: Django",
                   "Programming Language :: Python",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Topic :: Software Development :: E-mail",
                   ],
     )
