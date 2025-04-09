import logging

import feedparser
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

log = logging.getLogger(__name__)


def test_view(request):
    return render(request, "html/test_view.html")


class Spotlight(View):
    def __init__(self):
        self.latest_feed_link = "https://www.livechart.me/feeds/episodes"

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            response = self.loading_page(request)
        elif request.method == "OPTIONS":
            self.http_method_names = ["get", "options"]
            response = self.options()
        return response

    def get_latest_anime_list(self):
        rss_feed_list = feedparser.parse(self.latest_feed_link)
        latest_anime_episodes = []
        for entry in rss_feed_list.get("entries"):
            datashard = {
                "title": entry.get("title"),
                "image": entry.get("links")[1]["href"],
            }
            latest_anime_episodes.append(datashard)
        return latest_anime_episodes

    def loading_page(self, request):
        schedule_anime = self.get_latest_anime_list()
        return render(
            request, "html/test_view.html", {"schedule_anime": schedule_anime}
        )


class episode_page(View):
    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            response = self.episode_page(request)
        elif request.method == "OPTIONS":
            self.http_method_names = ["get", "options"]
            response = self.options()
        return response

    def episode_page(self, request):
        return render(request, "html/episode_page.html")


class searchPage(View):
    def __init__(self, **kwargs):
        self.anilist_graphql_url = "https://graphql.anilist.co"

    def dispatch(self, request, search_term=None):
        if request.method == "GET":
            return render(request, "html/search_page.html")
        elif request.method == "POST":
            response = self.search(request, search_term)
            return JsonResponse(response)

    def search(self, request, search_term):
        query = """query searchquery($PageNo:Int,$PerPageNo:Int,$SearchKey:String)
                {Page(page:$PageNo,perPage:$PerPageNo){pageInfo{total currentPage hasNextPage}
                media(search:$SearchKey,sort:[SEARCH_MATCH],type: ANIME)
                {id idMal episodes bannerImage title{english romaji}genres coverImage{extraLarge}airingSchedule{edges{node{episode airingAt}}}}}}"""
        variables = {"PageNo": 1, "PerPageNo": 20, "SearchKey": search_term}
        search_response = requests.post(
            self.anilist_graphql_url, json={"query": query, "variables": variables}
        )
        return search_response.json()
