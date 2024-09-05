import sys

project_name = "{{ cookiecutter.project_name }}"
project_slug = "{{ cookiecutter.project_slug }}"

assert " " not in project_name, f"'{project_slug}' project name should not contain spaces."

if hasattr(project_slug, "isidentifier"):
    assert project_slug.isidentifier(), f"'{project_slug}' project slug is not a valid Python identifier."

assert project_slug == project_slug.lower(), f"'{project_slug}' project slug should be all lowercase."

assert " " not in project_slug and "-" not in project_slug, f"'{project_slug}' project slug should not contain spaces or hyphens."
