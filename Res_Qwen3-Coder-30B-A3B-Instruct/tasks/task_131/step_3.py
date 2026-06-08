from xml.etree import ElementTree as ET
import re

# Parse the RSS feed
feed_content = '''<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:atom="http://www.w3.org/2005/Atom"
	xmlns:syndication="http://purl.org/rss/1.0/modules/syndication/"
	xmlns:slash="http://purl.org/rss/1.0/modules/slash/"
	>

<channel>
	<title>The Mozilla Blog</title>
	<atom:link href="https://blog.mozilla.org/feed/" rel="self" type="application/rss+xml" />
	<link>https://blog.mozilla.org/en/</link>
	<description>Mozilla Blog</description>
	<lastBuildDate>Wed, 20 Mar 2024 15:00:00 +0000</lastBuildDate>
	<language>en-US</language>
	<syndication:window>60</syndication:window>
	<syndication:frequency>1</syndication:frequency>
	
	<item>
		<title>Ajit Varma on Firefox’s new AI controls: &#8216;We believe in user choice&#8217;</title>
		<link>https://blog.mozilla.org/en/firefox/outside-the-fox-ai-controls/</link>
		<comments>https://blog.mozilla.org/en/firefox/outside-the-fox-ai-controls/#respond</comments>
		<pubDate>Wed, 20 Mar 2024 15:00:00 +0000</pubDate>
		<dc:creator><![CDATA[Firefox Team]]></dc:creator>
		
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>
		<category><![CDATA[AI]]></category>
		<category><![CDATA[Firefox]]></category>