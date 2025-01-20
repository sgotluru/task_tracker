import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="taskmanager",                
    version="1.0.0",                   
    author="Sreekara Gotluru",
    description="A simple CLI Task Manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sgotluru/task_tracker.git",  
    # packages=["utlis"],       
    packages=setuptools.find_packages(),   
    python_requires=">=3.6",           
    entry_points={
        "console_scripts": [
            "tasktkr=utlis.cli:main", 
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "PyYAML>=6.0",
        "tabulate>=0.9.0",
        ],
    include_package_data=True,
    license="MIT",
)
