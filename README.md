# README

## Setup PowerShell for venv

Set-ExecutionPolicy Unrestricted -Scope Process

.\venv\Scripts\activate

## Create PS Terminal with Admin Access

Start-Process powershell.exe -Verb runAs

## Dev Tool Tips

https://medium.com/analytics-vidhya/essential-developer-tools-for-improving-your-python-code-71616254134b

## pytest

```$pytest -ra .\path\to\file.py::TestClass::TestMethod```

## coverage

```$coverage run```
```$coverage report -m```

## Useful links

https://jellis18.github.io/post/2022-01-11-abc-vs-protocol/