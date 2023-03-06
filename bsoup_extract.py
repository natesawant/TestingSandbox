# Imports
from bs4 import BeautifulSoup
import re

# Pattern matching for getting the value in this format "property: value"
def use_regex(input_text):
    pattern = re.compile(r".+: (.+)", re.IGNORECASE)
    return pattern.match(input_text)

game_links = []

# Gets all possible games located on the website
with open("sitemap.xml", "r") as file:
    contents = file.read()
    # parsing
    soup = BeautifulSoup(contents, 'xml')
    for link in soup.find_all('loc'):
        if re.match(r"https://www.grosvenorcasinos.com/games/([A-Za-z]+(-[A-Za-z]+)+)", link.get_text()):
            game_links.append(link.get_text())

game_details = {}

# Iterate over all game links and get details
with open("Play Gold Blitz Online _ Grosvenor Casinos.html", encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, "html.parser")
    details = soup.find('div', class_='details-games')
    title = details.find('h1').text
    link = soup.find('link', rel='canonical')['href']
    tab_content = details.find('div', class_='tab-content')
    description = details.find('div', id='0')

    list_items = description.find_all('li')

    min_stake = use_regex(list_items[0].text).group(1)
    max_stake = use_regex(list_items[1].text).group(1)
    max_payout = use_regex(list_items[2].text).group(1)
    jackpot = use_regex(list_items[3].text).group(1)
    paylines = use_regex(list_items[4].text).group(1)
    special_features = use_regex(list_items[5].text).group(1)

    how_to_play = details.find('div', id='1')

    terms_and_conditions = details.find('div', id='2')

    game_details[title] = {
        'title' : title,
        'link' : link,
        'min_stake' : min_stake,
        'max_stake' : max_stake,
        'max_payout' : max_payout,
        'jackpot' : jackpot,
        'paylines' : paylines,
        'special_features' : special_features,
        'how_to_play' : how_to_play.text,
        'terms_and_conditions' : terms_and_conditions.text
    }

# From each category, get the order of the items in it
with open("view-source_https___www.grosvenorcasinos.com.html", encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, "html.parser")
    for game in soup.find_all("div", class_="game-tile-container"):
        title = game.find("img", class_="game-tile-background-container")["alt"]