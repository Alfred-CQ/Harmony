import json

def pagerank(graph, iters=100, d=0.85):
    N = len(graph)
    rank = [1.0 / N] * N

    for _ in range(iters):
        new_rank = [0] * N
        for i in range(N):
            for j in graph[i]:
                num_links = len(graph[j])
                if num_links == 0:
                    continue
                new_rank[j] += rank[i] / num_links
        rank = [(1 - d) / N + d * new_rank[i] for i in range(N)]
    print()
    print(rank)
    print(len(rank))

    dict_rank = {}

    for i, ranking in enumerate(rank):
        dict_rank[i] = ranking

    with open("dict_rank.json", 'w') as file:
            json.dump(dict_rank, file)

    return rank