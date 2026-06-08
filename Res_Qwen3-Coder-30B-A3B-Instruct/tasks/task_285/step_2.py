import requests
import json
from collections import defaultdict
import re
from datetime import datetime

# Step 1: Retrieve the latest 200 Hacker News stories
def get_top_stories(n=200):
    try:
        # Get the top story IDs
        response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
        story_ids = response.json()[:n]
        
        # Fetch details for each story
        stories = []
        for story_id in story_ids:
            story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
            story_data = story_response.json()
            if story_data and 'url' in story_data:
                stories.append(story_data)
        
        return stories
    except Exception as e:
        print(f"Error fetching stories: {e}")
        return []

# Step 2: Extract domain, keywords, and score information
def extract_info(stories):
    processed_stories = []
    
    for story in stories:
        url = story.get('url', '')
        title = story.get('title', '')
        score = story.get('score', 0)
        
        # Extract domain
        domain = ''
        if url:
            match = re.search(r'https?://(?:www\.)?([^/]+)', url)
            if match:
                domain = match.group(1)
        
        # Extract keywords from title (simple approach)
        keywords = [word.lower() for word in re.findall(r'\b\w+\b', title) if len(word) > 3]
        
        processed_stories.append({
            'id': story.get('id'),
            'title': title,
            'url': url,
            'domain': domain,
            'keywords': keywords,
            'score': score,
            'time': story.get('time')
        })
    
    return processed_stories

# Step 3: Classify stories into categories
def classify_story(story):
    keywords = story['keywords']
    domain = story['domain'].lower()
    
    # Define category mappings
    tech_keywords = ['tech', 'software', 'programming', 'development', 'code', 'app', 'mobile', 'web', 'ai', 'machine', 'learning', 'data', 'algorithm', 'database', 'server', 'cloud', 'api', 'framework', 'library', 'open source', 'github', 'docker', 'kubernetes', 'aws', 'azure', 'gcp', 'react', 'vue', 'angular', 'node', 'python', 'java', 'javascript', 'typescript', 'go', 'rust', 'c++', 'cpp', 'sql', 'nosql', 'graphql', 'tensorflow', 'pytorch', 'deep learning']
    science_keywords = ['science', 'research', 'study', 'paper', 'academic', 'university', 'physics', 'chemistry', 'biology', 'math', 'mathematics', 'astronomy', 'space', 'climate', 'environment', 'ecology', 'genetics', 'medicine', 'health', 'biotech', 'nanotech', 'robotics', 'quantum', 'neuroscience']
    business_keywords = ['business', 'startup', 'venture', 'funding', 'investment', 'market', 'economy', 'finance', 'stock', 'company', 'corporate', 'entrepreneur', 'product', 'launch', 'acquisition', 'ipo', 'revenue', 'profit', 'growth', 'strategy', 'marketing', 'sales']
    design_keywords = ['design', 'ui', 'ux', 'user experience', 'user interface', 'creative', 'art', 'graphic', 'visual', 'branding', 'logo', 'typography', 'color', 'layout', 'prototyping', 'mockup', 'wireframe']
    security_keywords = ['security', 'hack', 'cyber', 'privacy', 'encryption', 'authentication', 'authorization', 'vulnerability', 'exploit', 'malware', 'ransomware', 'phishing', 'ddos', 'firewall', 'vpn', 'ssl', 'tls', 'certificate', 'penetration', 'ethical hacking']
    gaming_keywords = ['game', 'gaming', 'play', 'video game', 'esports', 'console', 'pc', 'mobile game', 'indie', 'roguelike', 'fps', 'rpg', 'mmo', 'multiplayer', 'vr', 'ar', 'metaverse', 'gamification']
    
    # Categorize based on keywords
    category = 'other'
    
    # Check for tech
    if any(keyword in keywords for keyword in tech_keywords):
        category = 'technology'
    # Check for science
    elif any(keyword in keywords for keyword in science_keywords):
        category = 'science'
    # Check for business
    elif