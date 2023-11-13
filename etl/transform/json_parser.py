# from page_rank import pagerank

import json

id_to_location = {}
url_to_id = {}
adjacency_list = {}  # id -> list of links (not ids)


def json_to_docs():
    with open("data/wikipedia_extraction.json", "r") as file:
        raw_data = json.load(file)

    for i, article in enumerate(raw_data):
        article["links"] = [
            "https://en.wikipedia.org" + link for link in article["links"]
        ]
        article_to_save = {}
        article_to_save["id"] = i
        article_to_save["title"] = article["title"]
        article_to_save["description"] = (
            article["content"][:200] + "..."
        )

        article_to_save["content"] = article["content"]
        article_to_save["link"] = article["current_link"]

        article_path = "documents/" + str(i) + ".json"

        id_to_location[i] = article_path
        url_to_id[article["current_link"]] = i
        adjacency_list[i] = article["links"]
        with open(article_path, "w") as file:
            json.dump(article_to_save, file)

    # print(id_to_location)
    # print()
    # print()
    # print(url_to_id)


def set_adjacency_list():
    for article_id in adjacency_list.keys():
        cur_id_links = []
        for link in adjacency_list[article_id]:
            if link not in url_to_id:
                continue
            if url_to_id[link] in cur_id_links:
                continue
            cur_id_links.append(url_to_id[link])
        adjacency_list[article_id] = cur_id_links
    # print()
    # print()
    # print(adjacency_list)


# run_wikipedia_spider()
# assign_id_to_url()
# set_adjacency_list()

# rank = pagerank(graph=adjacency_list, iters=100, d=0.85)
