![GitHub](https://img.shields.io/github/license/MichaelSasser/ds2000?style=flat-square)
![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/MichaelSasser/ds2000/pythonpackage.yml/master?style=flat-square)
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes

ds2000 is a Python package for Rigol DS2000(A) Series Oscilloscopes.
Without touching any SCPI command, you will be able to use any function of
your oscilloscope with an python interface. It wraps every command and puts it
in an logical high level interface for you.

It uses the "[python-vxi11](https://github.com/python-ivi/python-vxi11)"
package to communicate with your Oscilloscope.

> Python VXI-11 provides a pure Python VXI-11 driver for controlling instruments
> over Ethernet.
> -- [python-ivi/python-vxi11](https://github.com/python-ivi/python-vxi11)

## Development

ds2000 is under development. You can try it out, but it might not be ready or
stable. Most features are not implemented yet and untested.

[Check out current development status](https://github.com/MichaelSasser/ds2000/projects/2)

## Semantic Versioning

This repository uses [SemVer](https://semver.org/) for its release
cycle.

## Branching Model

This repository uses the
[git-flow](https://danielkummer.github.io/git-flow-cheatsheet/index.html)
branching model by [Vincent Driessen](https://nvie.com/about/).
It has two branches with infinite lifetime:

* [master](https://github.com/MichaelSasser/ds2000/tree/master)
* [develop](https://github.com/MichaelSasser/ds2000/tree/develop)

The master branch gets updated on every release. The develop branch is the
merging branch.

## License
Copyright &copy; 2020-2021 Michael Sasser <Info@MichaelSasser.org>.
Released under the GPLv3 license.
