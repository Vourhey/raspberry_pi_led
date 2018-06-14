# DO NOT USE
# python setup.py install

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['raspberry_pi_led'],
    package_dir={'': 'src'})
setup(**setup_args)

