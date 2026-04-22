import environs

env = environs.Env()
env.read_env()


class Settings:
    bot_token = env.str("BOT_TOKEN", "8620751527:AAGolJy8SUxrBLNYyXHJZ-Mw5okvrWiA5I8")
    bot_user_redis = env.bool("BOT_USE_REDIS", default=False)
    tg_api_server_url = env.str("TG_API_SERVER_URL", default="https://api.telegram.org")
    admins_ids = env.list("ADMINS_IDS", default=[7892805795])

    database_url = env.str("DATABASE_URL")

    redis_host = env.str("REDIS_HOST", default="localhost")
    redis_db_name = env.str("REDIS_DB", default="0")

    selenium_url = env.str("SELENIUM_REMOTE_URL", default="http://localhost:4444/wd/hub")

    lastfm_api_key = env.str("LASTFM_API_KEY", default="f25528f2546d239c7922e8794225478b")
