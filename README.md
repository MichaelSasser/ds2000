![GitHub](https://img.shields.io/github/license/MichaelSasser/ds2000?style=flat-square)
![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/MichaelSasser/ds2000/pythonpackage.yml/master?style=flat-square)
![Matrix](https://img.shields.io/matrix/projects:michaelsasser.org?server_fqdn=matrix.michaelsasser.org&style=flat-square)
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes

ds2000 is a Python package for Rigol DS2000(A) Series Oscilloscopes.
With this package you are able to navigate through the functions of your
Oscilloscope with the Python autocomplete feature of your editor.
You will never need to touch any SCPI command. This package parses every
return value and gives you a complete python interface for your scope.
It is an abstraction layer between the real world hardware and the programming.

It uses the "[python-vxi11](https://github.com/python-ivi/python-vxi11)"
package to communicate with your Oscilloscope.

> Python VXI-11 provides a pure Python VXI-11 driver for controlling instruments
> over Ethernet.
> -- [python-ivi/python-vxi11](https://github.com/python-ivi/python-vxi11)

## Development

ds2000 is under development. You can try it out, but it might not be ready or
stable. Most features are not implemented yet and untested.

[Check out current development status](https://github.com/MichaelSasser/ds2000/projects/2)

#### A "NotImplementedError"-Error is not a bug
Mostly I create the structure first and fill it with the Rigol programming
documentation. This takes the most time. These methods and functions don't
contain any code, except the NotImplementedError raise.
These methods and functions are getting implemented later.

## License
Copyright &copy; 2020 Michael Sasser <Info@MichaelSasser.org>. 
Released under the GPLv3 license. 


