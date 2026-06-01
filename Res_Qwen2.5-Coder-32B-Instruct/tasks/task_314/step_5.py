import os
import sqlite3
import csv

databases = [
    "fox/fnthq021.default-release/storage/default/https+++www.speedtest.net/idb/340685107feisraebbaatsaed--isn.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++www.speedtest.net/idb/1233580710fgiirfenboacs_ee_troe.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++code.claude.com/ls/data.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++claude.ai/idb/2728594770keeryovtasl-.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++claude.ai/idb/2091240663xb-da-rdki-ra.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++claude.ai/ls/data.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++claude.ai/fs/metadata.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++gemini.google.com/ls/data.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++view.qiime2.org/cache/caches.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++www.reddit.com/cache/caches.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++www.reddit.com/idb/2728594770keeryovtasl-.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++www.reddit.com/ls/data.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++www.reddit.com/fs/metadata.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++www.youtube.com^partitionKey=%28https%2Cgoogle.com%29/cache/caches.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++www.youtube.com^partitionKey=%28https%2Cgoogle.com%29/idb/2232182701SeesravbiacteaWDosrgk.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++www.youtube.com^partitionKey=%28https%2Cgoogle.com%29/idb/3504742604LCo7g%sCD7a%t9a5b0a6s.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++www.youtube.com^partitionKey=%28https%2Cgoogle.com%29/idb/2171031483YattIedMb.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++www.youtube.com^partitionKey=%28https%2Cgoogle.com%29/ls/data.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/http+++localhost+8888/ls/data.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++ai.google.dev/cache/caches.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++ai.google.dev/idb/1120474735dbedv-sxietden-i.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/default/https+++docs.google.com/ls/data.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/cookies.sqlite",
    "/home/ai_admin/.config/mozilla/firefox