echo "Starting task. First, we need to identify a public website with at least 100 pages."
echo "Let's choose a popular website for demonstration purposes: https://example.com"
echo "Next, we will check if the website has a sitemap.xml to help us find pages."
curl -s https://example.com/sitemap.xml | grep "<url>" | wc -l