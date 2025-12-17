from setuptools import setup

package_name = 'amr_nav'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch',
         ['launch/sim_headless.launch.py',
          'launch/runtime.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robot-dev',
    maintainer_email='dev@company.com',
    description='AMR navigation package for CI/CD demo',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'simple_controller = amr_nav.simple_controller:main',
            'node_health = amr_nav.node_health:main',
        ],
    },
)
