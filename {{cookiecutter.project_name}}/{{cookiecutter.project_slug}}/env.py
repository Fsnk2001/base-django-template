import os

import environ

BASE_DIR = environ.Path(__file__) - 2

env = environ.Env()
env_path = os.path.join(BASE_DIR, '.env')
env.read_env(env_path)
