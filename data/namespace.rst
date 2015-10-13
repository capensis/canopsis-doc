{{namespace|title|replace("-", " ")}}
==========================================


.. toctree::
   :maxdepth: 1
   :titlesonly:

{% for repo in repositories %}
   {{repo.repo}}/index
{% endfor %}