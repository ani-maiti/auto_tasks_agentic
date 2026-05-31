import json

with open('language_stats.txt', 'r') as f:
    lines = f.readlines()

stats = {}
for line in lines:
    count, lang = line.split()
    stats[lang] = int(count)

most_common_language = max(stats, key=stats.get)
most_common_count = stats[most_common_language]

result = {
    "total_files": len(lines),
    "most_common_language": most_common_language,
    "most_common_count": most_common_count,
    "other_languages": {k: v for k, v in stats.items() if k != most_common_language}
}

with open('language_stats.json', 'w') as f:
    json.dump(result, f, indent=4)