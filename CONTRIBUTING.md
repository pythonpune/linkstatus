
# Introduction

 First off, thank you for considering contributing to linkstatus project. It's people like you that make linkstatus such a great tool. Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes, and helping you finalize your pull requests.

### What we are looking for?

linkstatus is an open source project and we love to receive contributions from our community — you! There are many ways to contribute, from writing tutorials or blog posts, improving the documentation, submitting bug reports and feature requests or writing code which can be incorporated into linkstatus itself.

### About to create a new Github Issue?

We appreciate that. But before you do, please learn our basic rules:

- Before posting a support issue please help to check the Readme & also the command help if it answers your question
- If you idea for a new feature, please consider if it fits into the project goals and it enhances the current features and also see if you can send a  [pull request](https://help.github.com/articles/using-pull-requests).  

### Suggested Labels For Issues

-   **Issue Types**
    -   **Bug**  - Anything that is broken
    -   **Regression**  - A bug that did not exist in previous versions and isn't a new feature (applied in tandem with Bug)
    -   **Feature**  - Anything that involves API changes, should generally only be for PRs or bug reports on in-progress features.
    -   **Performance**  - A performance related issue. We could track this as a bug, but usually these would have slightly lower priority than standard bugs.
    -   **Cleanup**  - Not a bug, not a feature, just code cleanup.
    -   **Documentation**  - Self-explanatory.
-   **Blockers**
    -   **Needs Bug Verification**  - A bug report, needs verification that it's actually a bug.
    -   **Needs Reproduction**  - Needs a test case or other reproduction of the issue.
    -   **Has Reproduction**  - Indicates a test case exists and is up-to-date.
    -   **Ready for PR**  - A well defined bug, needs someone to PR a fix.
    -   **PR Pending**  - A well defined bug, with a PR pending to fix.
    -   **Needs Code Review**  - A PR that needs the code to be verified by someone.
    -   **Needs Submitter Response**  - Anything that is blocking on the submitter.
    -   **Needs Team Discussion**  - Cannot progress until the core team has discussed further.
-   **Categories**  - These change per-project, may want to prefix, e.g. "C: HTMLBars". The big thing here is to keep proliferation low. If it gets too high, we might just want to change the issue title instead, e.g. prefix with "[HTMLBars]".
    -   **HTMLBars**
    -   **Router**
    -   ...
-   **Miscellaneous**  - These are per project and might be useful for further organization but should be kept to a minimum as well.
    -   **good first issue**  - What it says on the tin. This helps new people find stuff to work on, because  [GitHub actively promotes it](https://help.github.com/articles/helping-new-contributors-find-your-project-with-labels/)  and  [initializes new repositories with that label](https://help.github.com/articles/about-labels/#using-default-labels).
    
# Ground Rules

When contributing to linkstatus, we ask that you:

- let us know what you plan in the GitHub Issue tracker so we can provide feedback.
- provide tests and documentation whenever possible. When fixing a bug, please provide a failing test case that your patch solves.
- Ensure cross-platform compatibility for every change that's accepted. Windows, Mac, Debian & Ubuntu Linux.
- open a GitHub Pull Request with your patches and we will review your contribution and respond as quickly as possible. Keep in mind that this is an open source project, and it may take us some time to get back to you. Your patience is very much appreciated.  

# Setting up the environment

Below is the steps for setting up a development environment
```
git clone https://github.com/pythonpune/linkstatus
cd linkstatus
virtualenv .venv
source .venv/bin/activate
pip install .
linkstatus --help
```

# Your First Contribution

- Unsure where to begin contributing? You can start by looking through these beginner and help-wanted issues:
- Beginner issues - issues which should only require a few lines of code, and a test or two.
- Help wanted issues - issues which should be a bit more involved than beginner issues.
-  Both issue lists are sorted by total number of comments. While not perfect, number of comments is a reasonable proxy for impact a given change will have.

>*Working on your first Pull Request? You can learn how from this *free* series, [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first :smile_cat:
If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

# While Contributing

For something that is bigger than a one or two line fix:
 - Create your own fork of the code
 - Do the changes in your fork
 - If you like the change and think the project could use it
 - Be sure you have followed the code style for the project.

### Things that will be considered as fixes

As a rule of thumb, changes are obvious fixes if they do not introduce any new functionality or creative thinking. As long as the change does not affect functionality, some likely examples include the following:
- Spelling / grammar fixes
- Typo correction, white space and formatting changes
- Comment clean up
- Bug fixes that change default return values or error codes stored in constants
- Adding logging messages or debugging output
- Changes to ‘metadata’ files like .gitignore, build scripts, etc.
- Moving source files from one directory or package to another

