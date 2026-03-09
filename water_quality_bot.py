"""Water Quality Science Olympiad ID bot setup.

Run:
    source setup.sh
    python water_quality_bot.py
"""
import sciolyid

# ALIASES EDITx 
COMMAND_STYLE = {
    "prefixes": ["w.", "w!", "wq!", "W.", "W"],
    "pic_short_alias": "w",
    "hint_short_alias": "h",
    "check_short_alias": "c",
    "skip_short_alias": "s"
}

BOT_CONFIG = {
    "bot_description": "Science Olympiad Water Quality ID practice bot.",
    "bot_signature": "Water Quality ID Bot",
    "prefixes": COMMAND_STYLE["prefixes"],
    "id_type": "macroinvertebrates",
    "short_id_type": COMMAND_STYLE["pic_short_alias"],
    "support_server": "https://discord.gg/2HbshwGjnm",
    "source_link": "https://github.com/zainmarshall/waterboiiii",
    "name": "waterquality",
    "github_image_repo_url": "https://github.com/zainmarshall/waterboiiii-images.git",
    "invite": "https://discord.com/oauth2/authorize?client_id=1478213003886461048&permissions=116736&integration_type=0&scope=bot+applications.commands",
    "category_name": "grouping",
    "category_aliases": {
        "macroinvertebrates": ["macroinvertebrates", "macro", "macroinvert", "mi"],
        "invasive_animals": ["invasive_animals", "invanimals", "animals", "ia"],
        "invasive_plants": ["invasive_plants", "invplants", "plants", "ip"],
    },
    "data_dir": "water_quality_data",
    "default_state_list": "NATS",
    "local_redis": False,
    "redis_env": "REDIS_URL",
}

sciolyid.setup(BOT_CONFIG)

sciolyid.start()
