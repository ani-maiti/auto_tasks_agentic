# Fix the code to handle the case where the repository name is not found
def extract_repo_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract repository name and owner
    try:
        repo_name = soup.find("h1", class_="h3 lh-condensed").text.split("/")[1]
        repo_owner = soup.find("h1", class_="h3 lh-condensed").text.split("/")[0]
    except AttributeError:
        return None, None, None, None, None, None

    # Extract stars, forks, and issues
    try:
        stars = int(soup.find("a", class_="social-count js-social-count").text.replace(",", ""))
        forks = int(soup.find("a", class_="social-count js-social-count").next_sibling.next_sibling.text.replace(",", ""))
        issues = int(soup.find("a", class_="social-count js-social-count").next_sibling.next_sibling.next_sibling.next_sibling.text.replace(",", ""))
    except AttributeError:
        return None, None, None, None, None, None

    # Extract language information
    try:
        language = soup.find("span", class_="repo-lang").text.strip()
    except AttributeError:
        return None, None, None, None, None, None

    return repo_name, repo_owner, stars, forks, issues, language