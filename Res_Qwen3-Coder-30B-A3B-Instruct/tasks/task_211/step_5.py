print("Task completed successfully!")
print(f"Pages crawled: {len(page_titles)}")
print(f"Unique titles: {len(set([title for _, title in page_titles]))}")
print(f"Duplicate titles found: {len([title for title, count in Counter([title for _, title in page_titles]).items() if count > 1])}")