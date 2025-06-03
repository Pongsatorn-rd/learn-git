from setuptools import setup

setup(
    name="taskly",
    version="1.0.0",
    description="A CLI application to manage tasks.",
    author="Nine",
    author_email="pongsatornrd@gmail.com",
    url="https://github.com/Pongsatorn-rd/learn-git",
    py_modules=["taskly"],
    entry_points={
        "console_scrips": [
            "taskly = taskly:main",
        ],
    },
    install_requires=[
        "tabulate",
    ],
    tests_requires=[
        "pytest",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT Liecense",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6",
)
