from bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1118936839  # my telegram ID
    OWNER_USERNAME = "Sur_vivor"  # my telegram username
    API_KEY = "your bot api key"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    USE_MESSAGE_DUMP = True
    SUDO_USERS = []  # List of id's for users which have sudo access to the bot.
