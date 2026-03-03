"""Water Quality Science Olympiad ID bot setup.

Run:
    source setup.sh
    python water_quality_bot.py
"""

import sciolyid

# ALIASES EDIT
COMMAND_STYLE = {
    "prefixes": ["w.", "w!", "wq!"],
    "pic_short_alias": "e",
    "hint_short_alias": "h",
    "check_short_alias": "c",
    "skip_short_alias": "l"
}

BOT_CONFIG = {
    "bot_description": "Science Olympiad Water Quality ID practice bot.",
    "bot_signature": "Water Quality ID Bot",
    "prefixes": COMMAND_STYLE["prefixes"],
    "id_type": "organisms",
    "short_id_type": COMMAND_STYLE["pic_short_alias"],
    "support_server": "https://discord.gg/2HbshwGjnm",
    "source_link": "https://github.com/tctree333/SciOly-ID",
    "name": "waterquality",
    "github_image_repo_url": "https://github.com/zainmarshall/waterboiiii-images.git",
    "invite": "Replace this text with your bot invite URL.",
    "category_name": "grouping",
    "category_aliases": {
        "macroinvertebrates": ["macroinvertebrates", "macro", "macroinvert", "mi"],
        "invasive_animals": ["invasive_animals", "invanimals", "animals", "ia"],
        "invasive_plants": ["invasive_plants", "invplants", "plants", "ip"],
    },
    "data_dir": "water_quality_data",
    "default_state_list": "NATS",
}

sciolyid.setup(BOT_CONFIG)

sciolyid.start()
