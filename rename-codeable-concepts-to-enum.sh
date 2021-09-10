#!/bin/sh

sed -i 's/value_codeable_concept/value_enum/g' model/schema/crdch_model.yaml > temp.yaml
