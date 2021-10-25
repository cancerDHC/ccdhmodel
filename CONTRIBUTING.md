# How to contribute

The following is a set of guidelines for contributing to this repository.

## Create a new issue

If you spot a problem with the code or documents; want to report bugs; or want to suggest enhancements, [search if an issue already exsits](https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-issues-and-pull-requests#search-by-the-title-body-or-comments). If a related issue doesn't exist, you can open a new issue using an [issue form](https://github.com/cancerDHC/ccdhmodel/issues/new/choose). You can choose "Bug report", "Feature request", or "Open an blank issue." 

* How to use labels?

## Solve an issue

Scan through our [existing issues](https://github.com/cancerDHC/ccdhmodel/issues) to find one that interests you.

* The issues can be self-assigned and/or assigned by any members of the team.
* The issues we should tackle first are listed on Standing reference section of the Tools team meeting notes.
* The issues we priotize each quarter can be found at [Milestones](https://github.com/cancerDHC/ccdhmodel/milestones) page. category (e.g., model, model generation, model testing, etc.)

### Create a branch
* Using naming convention of branches described in [gitflow](https://nvie.com/posts/a-successful-git-branching-model/) workflow (discussions are ongoing.)

### Pull Request

When you're finished with the changes, create a [pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests), also known as a  PR.
* Fill the "Ready for review" template so that we can review your PR. This template helps reviewers understand your changes as well as the purpose of your pull request. (Are we adding "ready for review" template?)
* Don't forget to [link PR to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) if you are solving one.

#### Code Review

A pull request must be reviewed by **at least one other project member** to get merged quickly.
* Assign reviewer(s). Who do I assign?

> A CCDH engineer must review and accept your pull request. A code review (which happens with both the contributor and the reviewer present) is required for contributing.

* **Which branch should I select on PR? base:?; compare:(the branch you made changes); Any rule on this?**; Follow [gitflow](https://nvie.com/posts/a-successful-git-branching-model/) workflow?
* **What about testing?**

* We may ask for changes to be made before a PR can be merged, either using suggested changes or pull request comments. You can make any other changes and commit them in your branch.
* As you update your PR and apply changes, mark each conversation as resolved.
* If you run into any merge issues, checkout this [git tutorial](https://lab.github.com/githubtraining/managing-merge-conflicts) to help you resolve merge conflicts and other issues.

## Development environment setup

1. Install package dependencies. **Where can we find pacakge dependencies?**
2. Clone the ccdhmodel package repository.
```shell
git clone https://github.com/cancerDHC/ccdhmodel.git
```
3. Create and activate the virtual environment.
* If you want to generate LinkML artifacts, follow the instruction on [Generation of LinkML artifacts](https://github.com/cancerDHC/ccdhmodel#generation-of-linkml-artifacts).

## Styleguides

The project follows the [Black code style](https://black.readthedocs.io/en/stable/the_black_code_style/index.html).
