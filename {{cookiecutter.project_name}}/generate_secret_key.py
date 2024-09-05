import os
import shutil

from django.core.management.utils import get_random_secret_key


from {{cookiecutter.project_slug}}.env import env, BASE_DIR, env_path


def setup_secret_key():
    def copy_example_env():
        example_env_path = os.path.join(BASE_DIR, '.env.example')
        if os.path.exists(example_env_path):
            shutil.copy(example_env_path, env_path)
        else:
            raise FileNotFoundError("Both .env and .env.example are missing.")

    if not os.path.exists(env_path) or os.path.getsize(env_path) == 0:
        copy_example_env()

    secret_key = get_random_secret_key()
    new_env_content = []
    secret_key_replaced = False

    with open(env_path, 'r') as env_file:
        env_content = env_file.readlines()
    for line in env_content:
        if line.startswith("SECRET_KEY="):
            new_env_content.append(f"SECRET_KEY={secret_key}\n")
            secret_key_replaced = True
        else:
            new_env_content.append(line)

    if not secret_key_replaced:
        new_env_content.append(f"SECRET_KEY={secret_key}\n")

    with open(env_path, 'w') as env_file:
        env_file.writelines(new_env_content)

    print(f"New SECRET_KEY generated and added to {env_path}")


if __name__ == '__main__':
    if not env('SECRET_KEY', default=None):
        setup_secret_key()
