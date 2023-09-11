from environs import Env
env = Env()
env.read_env()  # read .env file, if it exists

API_KEY = env("API_KEY")
API_KEY_NAME = env("API_KEY_NAME")
SWARM_MONGO_URI = env("SWARM_MONGO_URI")