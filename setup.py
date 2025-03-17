from setuptools import setup, find_packages

setup(
    name="20thrice",
    version="1.0.0",
    author="khawaidev",
    author_email="khawaimedia@gmail.com",
    description="A 20-20-20 rule reminder app to reduce eye strain",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/khawaidev/20thrice",  # Replace with your repo link
    packages=find_packages(),
    install_requires=[
        "tkinter",
        "ttkbootstrap",
        "pynput",
        "playsound; platform_system!='Windows'",
        "winsound; platform_system=='Windows'",
    ],
    package_data={
        "": ["assets/*.wav", "assets/*.ico"]
    },
    entry_points={
        "gui_scripts": [
            "twenty_twenty_twenty = twenty_twenty_twenty_reminder.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
