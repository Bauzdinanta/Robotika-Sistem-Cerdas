from setuptools import setup

package_name = 'prm_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=["prm"],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Probabilistic Roadmap simulation',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'prm = prm:main'
        ],
    },
    data_files=[
        ('share/' + package_name + '/launch', ['launch/prm_launch.py']),
    ],
)
