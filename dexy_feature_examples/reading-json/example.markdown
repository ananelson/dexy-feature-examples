The `from_json` method converts JSON output to python objects:

Foo is '{{ d['example.json'].from_json().foo }}'.

This is combined with jinja's helpers which let you access ex['foo'] as ex.foo.

To make this easier, use jinja template variables to create a shortcut:

{% set ex = d['example.json'].from_json() %}

Foo is '{{ ex.foo }}'.
