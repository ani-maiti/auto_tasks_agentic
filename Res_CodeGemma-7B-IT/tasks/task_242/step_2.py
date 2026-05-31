from collections import Counter

# Remove invalid topic keyword
topic_keywords = [keyword for keyword in topic_keywords if keyword != ""]

# Print most common topic keyword
most_common_topic = Counter(topic_keywords).most_common(1)[0][0]
print("Most common topic keyword:", most_common_topic)