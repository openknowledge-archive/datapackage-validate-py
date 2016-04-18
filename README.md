**This project is DEPRECATED. You should use
<https://github.com/datapackages/datapackage-py> instead. This repository is
just for historical purposes.**

# datapackage-validate-py

Validate [Data Package][] datapackage.json files against a jsonschema.

[Data Package]: http://data.okfn.org/doc/data-package

## Usage

```python
import datapackage_validate

try:
  datapackage_validate.validate(datapackage, schema)
except datapackage_validate.exceptions.DataPackageValidateException as e:
  e.errors  # List with validation errors
```

The `datapackage` can be a json string or python dict.

The `schema` can be a json string, python dict, or a schema id corresponding with a schema from the registry of [Data Package Profiles][]. `schema` is optional, and will default to the `base` schema id if not provided.

`validate()` returns None. If there were errors during validation, it raises a
`datapackage_validate.exceptions.DataPackageValidateException` with a list of
the validation errors in its `.errors` property.

[Data Package Profiles]: https://github.com/dataprotocols/registry
