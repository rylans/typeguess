typeguess
=========

[![Build Status](https://travis-ci.org/rylans/typeguess.svg?branch=master)](https://travis-ci.org/rylans/typeguess)

Automatically guess data types


### Examples

```python
>>> from typeguess import guess
>>> guess(['hanson@mail.org'])
'string.email'
```

```python
>>> from typeguess import guess
>>> guess(['m', 'f'])
'string.vcard.gender'
```

### Planned Features

* vCard types
* XML Schema types

## License

Apache 2.0
