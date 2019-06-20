import os
from urllib.parse import urljoin

import requests
from decouple import config


# https://docs.transifex.com/api/
TRANSIFEX_API_URL = "https://www.transifex.com/api/2/project/python-newest/"
# https://www.transifex.com/user/settings/api/
TRANSIFEX_API_TOKEN = config("TRANSIFEX_API_TOKEN")

PROJECT_NAME = "python-newest" # Lastest version of Python (Master branch on Github)
REQUIRED_RESOURCES = ["bugs", "howto", "library"]

GOLD = "#ffd700"
GOLDENROD = "#daa520"
DODGERBLUE = "#1e90ff"
ROYALBLUE = "#4169e1"


def colorize_resource(resource, color1, color2):
    if resource not in required_resources:
        return color1

    return color2


def palette(resources):
    fill_palette = [GOLD if resource in REQUIRED_RESOURCES else DODGERBLUE
                    for resource in resources]
    line_palette = [GOLDENROD if resource in REQUIRED_RESOURCES else ROYALBLUE
                    for resource in resources]

    return fill_palette, line_palette


def transifex_api(url):
    response = requests.get(urljoin(TRANSIFEX_API_URL, url), auth=("api", TRANSIFEX_API_TOKEN))

    if not response.ok:
        raise Exception(f"Error, status_code={response.status_code}, {url}")
    return response.json()


def kilo_format(value, tick_number):
    s = str(int(value))
    if s.endswith("000"):
        return s[:-3] + " k"
    return value


def setup_axes(ax):
    ax.tick_params(axis="x", pad=10)
    ax.tick_params(axis="y", pad=10)
    ax.spines["left"].set_color("0")
    ax.spines["bottom"].set_color("0")
