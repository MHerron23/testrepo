from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Michael Herron",
      author_email="michael.herron@hotmail.com",
      license="GPL3",
      packages=["systeminfo"],
      entry_points={
          "console_scripts":["comp30670_syteminfo=systeminfo.main:main"]
          }
      )