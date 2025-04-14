from setuptools import find_packages, setup
import glob
import os

package_name = 'opencv_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch',
              glob.glob(os.path.join('launch', '*.launch.py'))),
        ('share/' + package_name + '/params',
              glob.glob(os.path.join('params', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dori',
    maintainer_email='dori@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'img_publish = opencv_pkg.img_publish:main'
        ],
    },
)