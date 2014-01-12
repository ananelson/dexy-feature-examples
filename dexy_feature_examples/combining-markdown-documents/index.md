This is the main document. We want to automatically include component documents.

We iterate over input document keys given in `d.keys()`.

{% for doc_key in d.keys() %}
# {{ d[doc_key].title() }}

{{ d[doc_key] }}

{% endfor %}
