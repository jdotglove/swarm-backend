from environs import Env
env = Env()
env.read_env()  # read .env file, if it exists

SWARM_MONGO_URI = env("SWARM_MONGO_URI")