Automated testing
===

## Background

Why write automated tests?

* More confidence in your code
* Repeatible without human action (humans are silly & make mistakes)
* Test subsection (e.g. _units_) of your code
* Replicate real-world behaviour (_regression testing_)

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

Run shell in the virtual env: `pipenv shell`

Now we're able to install and use our dependencies in an isolated, virtual environment.

## Testing frameworks

Multiple testing frameworks, for example:

- pytest (which we will use)
- nose
- unittest

All have different ways of writing assertions and so-called doubles (or mocks).

### Assertions

The basic ability of any testing framework is an assertion, a comparison of the _desired state_ as to the _actual state_.

In pytest this is represented by the `assert` function.

Example assertion program:

```python
# greeting.py
def greet(name):
    if name:
        return "Hello, %s" % name
    else:
        return "Hello, Anon!"

# test_greeting.py
def test_without_name():
    actual = greet(None)
    assert actual == "Hello, Anon!"

def test_with_name():
    actual = greet("Michiel")
    assert actual == "Hello, Michiel!"
```

Assertions don't have to use `==`. 

Example: `strcmp` is a function that compares two strings, `a` and `b`. Outputs:

- If the strings are equal, it returns 0;
- If `a` is lexically _less_, the function returns a value below 0;
- If `b` is lexically _less_, the function returns a value above 0.

Tests:

```python
# test_strcmp.py
def test_equal():
    assert strcmp("foo", "foo") == 0

def test_b_higher():
    assert strcmp("bcd", "abc") < 0

def test_a_higher():
    assert strcmp("abc", "bcd") > 0
```


### Mocks / spies / stubs

Why?

- Test units, not entire systems, see earlier test pyramid.
- Isolate logic, focus on interface.
- Easier & cheaper to test
- **Avoiding side effects**

What do we test when using a mock?

- Interactions with component
- Arguments passed to component

Differences:

- Mocks allow you to define the return value **and** assert against the parameters, and do not call the real object
- Spies call the real object, but allow you to assert against the parameters
- Stubs is a special type of mock that accepts any arguments

### Running tests

Run `pipenv shell` and in your newly opened virtual environment, run `pytest`. 

Test files have to match `test_*.py` to be eligible for auto-discovery.

## TDD

How did it come about?

- Bugs in production
- Long turnaround on manual testing
- No "missed" code

It's a process. Write your test first. Write the minimal amount of code required to make the test pass. Refactor judiciously while running the tests.
AKA the red-green-refactor cycle.

More difficult to add tests afterwards.

Many developers don't practice TDD as closely as prescribed. Find a personal balance. Use metrics (e.g. code coverage) to confirm you are still testing _sufficiently_. 

TDD is considered an **essential** skill for many companies as it tends to decrease the amount of bugs, increases code quality and leads to decoupled systems.

## Continuous integration

Anecdote:

Imagine a big software organisation where developers work on their features. Every six months, according to the release schedule, developers all merge their work into the main branch and deploy said code. Integrating (resolving all conflicts!) and deployment take many days, weeks perhaps. Countless manhours are lost. Production issues occur because the merged code was incorrect.

What went wrong? Modern software practice is to merge your branches often - as often as you can. And when merging, running your tests. This is yet another point where tests help. If your tests fail after the merge, then something is wrong and this needs to be addressed as soon as possible. If the tests fail before the merge, the merge is declined or halted to fix the tests.

The process of merging your branches often, perhaps even multiple times a day, and running tests every time, before and after the merge, is called continuous integration.

Benefits

- Catch failing tests before merge
- Merging often leads to fewer merge conflicts
- Less time for requirements to change!
- Leads to small, iterative changes rather than big, risky changesets.

Many tools:

- Jenkins (probably most popular)
- TravisCI
- CircleCI
- GoCD
- Many, many more

### Pipelines

One way to do CI. Built from stages. Can be declaratively built. Each stage operates on output of previous. Allow complex build processes to be split up and even run concurrently (at the same time). You can have pipelines that fan out and have conditional stages. Often uses a YAML file or, uniquely, a Jenkinsfile.

## Task

https://docdro.id/ESOa6lQ

`MovieService` is an external component, implemented in a separate library.
Code against the interface.

`MovieService` will have an interface that is identical:

- a method `getParentalControlLevel` which accepts a parameter `movieId` and returns a string
- upon failure, it will return `None` (unless they have learned about exceptions)