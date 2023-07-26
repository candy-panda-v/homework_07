from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Sorting files by category',
    url='https://github.com/candy-panda-v/homework_07.git',
    author='Volodymyr Likhachiov',
    author_email='likhachiovvl@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.sort:main']}
)
