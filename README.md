# Quadratic Equations Solver

This repository except script for solving quadratic equations contains tests and pre commit hook which runs before commit and interrupt it if test failed.


# How to install

1. Create bash script **pre-commit** in the **.git/hooks** directory:
```bash
#!/bin/sh
path_to_python path_to_pre-commit.py

```

2. In the **pre-commit.py** define filenames:
```python
LOG_FILENAME = 'log_filename.log'
TESTS_FILENAME = 'file_with_tests.py'
```

3. Try to make commit. If tests failed, your attempt finishes with error and log string in the log file.


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
