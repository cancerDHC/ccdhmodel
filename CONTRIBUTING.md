# How to contribute

The following is a guideline for contributing to this repository.

## Create a new issue

If you spot a problem with the code or documents; want to report bugs; or want to suggest enhancements, [search if an issue already exists](https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-issues-and-pull-requests#search-by-the-title-body-or-comments). If a related issue doesn't exist, you can open a new issue using an [issue form](https://github.com/cancerDHC/ccdhmodel/issues/new/choose). You can choose either "Bug report" or "Feature request." If your issue doesn't fall under either categories, please use "Open an blank issue" to report your problem.

### How to use labels?

If you report an issue using predefined issue forms, each form automatically tags a label for you. You can also add tags manually. You can find the list of labels currently being used in this repository at [labels](https://github.com/cancerDHC/ccdhmodel/labels) page.

## Solve an issue

Scan through our [existing issues](https://github.com/cancerDHC/ccdhmodel/issues) to find one that interests you.

* The issues can be self-assigned and/or assigned by any members of the team.
* The issues we should tackle first are listed on 'standing reference' section of the Tools team meeting notes.
* The issues we priotize each quarter can be found at [Milestones](https://github.com/cancerDHC/ccdhmodel/milestones) page. The issues are categorized in next release of the CRDCH model, improvement of model generation, model testing, and model documentation, and future goals.

### Create a branch

We follow the [gitflow](https://nvie.com/posts/a-successful-git-branching-model/) workflow for branching practice and naming convention.
(Discussions on branching model/practice are ongoing.)

* The repo holds two main branches with an infinite lifetime: `master` and `develop`
* The supporting branches we only use are feature and bugfix branches. You can name your branch anything except `master` and `develop`. You can add a short descriptor of the task, and/or an issue ID to the name of the branch.

### Pull Request

When you're finished with the changes on your code, create a [pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests), also known as a PR.

* You need to make a PR into the same branch that you created a sub branch from. Typically `main` or `develop`, unless you are proposing a modification to a feature branch or a bugfix branch.
* Don't forget to [link PR to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) if you are solving one.

### Code Review

A pull request must be reviewed by **at least one other project member** to get merged quickly.

> A CCDH engineer must review and accept your pull request. A code review (which happens with both the contributor and the reviewer present) is required for contributing.

* You can add `unittest` tests to the repo as well.
* We may ask for changes to be made before a PR can be merged, either using suggested changes or pull request comments. You can make any other changes and commit them in your branch.
* As you update your PR and apply changes, mark each conversation as resolved.
* If you run into any merge issues, checkout this [git tutorial](https://lab.github.com/githubtraining/managing-merge-conflicts) to help you resolve merge conflicts and other issues.

## Development environment setup

1. Install package dependencies.
   1. Install poetry if necessary. One-time installation commands are available for [osx/linux/bash on windows](https://github.com/python-poetry/poetry#osx--linux--bashonwindows-install-instructions) and for [windows powershell](https://github.com/python-poetry/poetry#windows-powershell-install-instructions).
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

5. To test new changes made to any of the modules within sheet2linkml, do the following:

    ```shell
    # make changes to any files or modules
    pip uninstall ccdhmodel  # uninstall package
    poetry build
    pip install dist/crdchmodel-x.y.z-py3-none-any.whl  # install wheel file
    ```

* If you want to generate LinkML artifacts, follow the instruction on [Generation of LinkML artifacts](https://github.com/cancerDHC/ccdhmodel#generation-of-linkml-artifacts).

## Format code with `black`

The code which you intend to commit and merge into this repository should be conformant with the standards adopted by the [black](https://black.readthedocs.io/en/stable/index.html) code formatter. In order to format your code with `black`, run the following command:

    ```shell
    poetry run black ~/path/to/directory
    ```
