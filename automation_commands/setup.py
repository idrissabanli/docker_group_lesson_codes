from setuptools import setup, find_packages

setup(
      # mandatory
      name='create_front_project',
      # mandatory
      version='1.0.0',
      # mandatory
      author_email='idris.sabanli@gmail.com',
      packages=['codes'],
    #   package_data={},
      install_requires=['click'],
      entry_points={
        'console_scripts': ['create_front_project = codes.create_front_project:create_project']
      }
)