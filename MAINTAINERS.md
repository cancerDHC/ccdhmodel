# This repo was recently updated to follow the https://github.com/linkml/linkml-model-template

Much of the instructions below are probably obsolescent. Not 100% sure about using mike to make the docs, although mike is specified as a plugin in the mkdocs setup file. I’m not sure where tagging fits into this. A gh-pages branch may not be necessary for publishing the docs to https://cancerdhc.github.io/ccdhmodel

The environments for using and building this package are managed with pipenv now. The Makefile recipes install and enter into the environments as necessary. Manually installing the environment shouldn’t be necessary but couldn’t hurt.

`make` all by itself regenerates the schema artifacts including the documentation.

I have git added the docs folder, so maybe that should be rolled back?
![image](https://user-images.githubusercontent.com/25185273/128519081-6f0ee1fa-d300-4686-b7b2-480d18a559c5.png)


# ~~How to make a release~~

See the instructions at the top of [Makefile](Makefile)

First install the linkml python package and mkdocs:

```bash
. environment.sh
pip install -r requirements.txt
```

Then every time you change the source schema, run:

```bash
make all
```

This will generate files in:

 * [docs]
 * [jsonschema]
 * [shex]
 * [owl]
 * [rdf]

Do **not** git add the files in docs

## Using mike to maintain multiple versions

We use [mike](https://github.com/jimporter/mike) to maintain multiple
versions of our documentation on the website. We currently refer to
each version as e.g. `v0.2`. Please create Git tags to keep track of
which version of the source code the documentation was generated from.

To deploy a new version, you have to prepare the `docs/` directory
with the new documentation in Markdown. Usually, the steps described
above can be used to do this. However, if the `docs/` directory was not
created and populated correctly, you can run:

```
$ make clean      # This will delete the `docs/` directory. 
$ make gen-docs	  # This will generate the docs in `target/docs`.
$ make stage-docs # This will copy `target/docs` into `docs/`.
```

Once the documentation has been generated in `docs/`, use mike to 
publish a new version:

```
$ pip install mike # Only needed the first time.
$ mike deploy v0.2 latest -p
```

Note that the `-p` option causes mike to push the documentation to
the `gh-pages` branch immediately. `latest` is the alias we use to
indicate that a particular version should be considered the latest
(and therefore the default).
