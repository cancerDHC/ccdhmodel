# How to contribute

The following is a set of guidelines for contributing to the CRDCH model repository.

## Development Environment Setup

This section describes how to set up the development environment needed to make the CRDCH artifacts from the CRDCH schema in YAML that is included with this repository.

You will need to install `Python 3.7+`, `Make` and `Poetry` in order to build the artifacts in this repository. One-time installation commands for Poetry are available for [macOS/Linux/Bash on Windows](https://github.com/python-poetry/poetry#osx--linux--bashonwindows-install-instructions) and for [Windows PowerShell](https://github.com/python-poetry/poetry#windows-powershell-install-instructions).

For most development tasks, you should be able to clone this repository using:

```shell
git clone https://github.com/cancerDHC/ccdhmodel.git
```

And then building all artifacts by using the included Makefile:

```shell
make
```

You can run the included unit tests by running:

```shell
make test
```

You can regenerate the model by using:

```shell
make generate-model
```

You can publish the code to PyPI by running:

```shell
poetry publish
```

Detailed instructions on setting up the development environment without using the `Makefile` are provided below.

1. Install package dependencies.
   1. Install poetry if necessary. One-time installation commands are available for [macOS/Linux/Bash on Windows](https://github.com/python-poetry/poetry#osx--linux--bashonwindows-install-instructions) and for [Windows Powershell](https://github.com/python-poetry/poetry#windows-powershell-install-instructions).
2. Clone the ccdhmodel package repository.

    ```shell
    git clone https://github.com/cancerDHC/ccdhmodel.git
    ```

3. Create and activate the virtual environment.
4. Run the following commands to build ccdhmodel and install the package along with all of its dependencies:

    ```shell
    cd ccdhmodel  # change directory to ccdhmodel
    git checkout main  # switch to main branch of ccdhmodel
    poetry build # build source and wheel archives
    pip install dist/crdchmodel-x.y.z-py3-none-any.whl  # install wheel file
    ```

    **note**: x.y.z is the version number listed on pyproject.toml.

5. To test new changes made to any of the modules within ccdhmodel, do the following:

    ```shell
    # make changes to any files or modules
    pip uninstall ccdhmodel  # uninstall package
    poetry build
    pip install dist/crdchmodel-x.y.z-py3-none-any.whl  # install wheel file
    ```

* If you want to generate LinkML artifacts, follow the instruction on [Generation of LinkML artifacts](https://github.com/cancerDHC/ccdhmodel#generation-of-linkml-artifacts).

### Format Code with `black`

The code which you intend to commit and merge into this repository should be conformant with the standards adopted by the [black](https://black.readthedocs.io/en/stable/index.html) code formatter. In order to format your code with `black`, run the following command:

```shell
poetry run black ~/path/to/directory
```

## Create a New Issue

If you spot a problem with the code or documents; want to report bugs; or want to suggest enhancements, [search if an issue already exists](https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-issues-and-pull-requests#search-by-the-title-body-or-comments). If a related issue doesn't exist, you can open a new issue using an [issue form](https://github.com/cancerDHC/ccdhmodel/issues/new/choose). You can choose either "Bug report" or "Feature request." If your issue doesn't fall under either categories, please use "Open an blank issue" to report your problem.

### How to Use Labels?

If you report an issue using predefined issue forms, each form automatically tags a label for you. You can also add tags manually. You can find the list of labels currently being used in this repository at [labels](https://github.com/cancerDHC/ccdhmodel/labels) page.

## Solve an Issue

Scan through our [existing issues](https://github.com/cancerDHC/ccdhmodel/issues) to find one that interests you.

* The issues can be self-assigned and/or assigned by any members of the team. Please do not start work on an assigned issue without checking with the assignee, who might be already working on the issue, and please unassign yourself if you can no longer work on that issue.
* The issues we should tackle first are listed on 'standing reference' section of the Tools team meeting notes.
* Issues we are currently working on are grouped using [Milestones](https://github.com/cancerDHC/ccdhmodel/milestones). Milestones group thematically related issues that are due to be completed by a particular date.

### Create a Branch

We follow the [gitflow](https://nvie.com/posts/a-successful-git-branching-model/) workflow for branching practice and naming convention.
(Discussions on branching model and branching practice are ongoing.)

* The repo holds two main branches with an infinite lifetime: `main` and `develop`
* The supporting branches we may use are:
  * Feature branches
  * Release branches
  * Hotfix branches
* Naming convention of the branches
  * Feature branches: You can name your branch anything except `main` and `develop`. You can add a short descriptor of the task, and/or an issue ID to the name of the branch.
  * Release branches: release-*
  * Hotfix branches: hotfix-*
* It is recommended to use the [GitFlow Git extension](https://github.com/nvie/gitflow) to implement the gitflow branching model locally.

### Pull Request

When you're finished with the changes on your code, create a [pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests), also known as a PR.

* PRs for feature branches should always merge into `develop`, while PRs for release and hotfix branches should always merge into `main`, unless there are good reasons to merge them into another branch.
* Don't forget to [link PR to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) if you are solving one. A good way to do this is by writing `closes #[issue number]` somewhere in the PR description.
* Major changes, especially new features, should be documented in the CHANGELOG file in the PR so we can keep track of which version each change was incorporated into.

### Code Review

A pull request must be reviewed by **at least one other project member** before it is merged.

> A CCDH engineer must review and accept your pull request. A code review (which happens with both the contributor and the reviewer present) is required for contributing.

* You can add `unittest` tests to the repo as well.
* We may ask for changes to be made before a PR can be merged, either using suggested changes or pull request comments. You can make any other changes and commit them in your branch.
* As you update your PR and apply changes, mark each conversation as resolved.
* If you run into any merge issues, checkout this [git tutorial](https://lab.github.com/githubtraining/managing-merge-conflicts) to help you resolve merge conflicts and other issues. Please also don't hesitate to ask other project members for help!
