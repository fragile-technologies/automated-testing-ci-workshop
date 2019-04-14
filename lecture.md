Automated tests
===

Why write automated tests?

* More confidence in your code
* Repeatible without human action (humans are silly & make mistakes)
* Test subsection (e.g. _units_) of your code

Different levels of testing:

Testing pyramid:

![Testing pyramid][testing_pyramid]

[testing_pyramid]: https://d2h1nbmw1jjnl.cloudfront.net/ckeditor/pictures/data/000/000/158/content/typical_pyramid-1024x938.jpg

Up: more coverage, e.g. E2E testing, slower, more expensive, _brittle_
Down: more granular (smaller scale), cheap, fast

In practice, applications have **many** unit tests but few E2E tests. Unit tests are geared towards a particular function, class or piece of code, whereas integration tests and E2E tests consider the system as a whole.

## Detour into Python dep management

### Dependencies in Python

Problem: use third-party code from a library - how do we use it in our program?
Solution: Pip

`pip install --user <package>` installs package.

The `--user` means it installs it for the user.

Problem: what if we have different projects requiring different versions of a dependency?

Solution: Use a virtual environment.

Problem: new versions of packages are released constantly. By default, `pip install` installs the latest. How do we ensure every developer has the same version running? 

Solution: `requirements.txt` or similar. I prefer Pipenv because it stores the entire dep chain in a "lockfile" and has a virtual environment built in.

### Pipenv install

`pip install --user pipenv`

### Pipenv usage

Install package: `pipenv install requests`
Run script with virtual env: `pipenv run <file>`
