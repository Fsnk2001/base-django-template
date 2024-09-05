import os
import shutil


def delete_resource(resource):
    if os.path.isfile(resource):
        print(f"removing file: {resource}")
        os.remove(resource)
    elif os.path.isdir(resource):
        print(f"removing directory: {resource}")
        shutil.rmtree(resource)


if __name__ == "__main__":
    project_slug = "{{cookiecutter.project_slug}}"
    license = "{{cookiecutter.open_source_license}}"
    use_celery = "{{cookiecutter.use_celery}}"
    use_docker = "{{cookiecutter.use_docker}}"

    if license == "Not open source":
        delete_resource("LICENSE")
    if use_celery == "n":
        delete_resource(f"{project_slug}/celery.py")
    if use_docker == "n":
        delete_resource(f"docker/")
        delete_resource(f"docker-compose.yml")
        delete_resource(f"docker-compose-production.yml")

    print("Project initialized.")
