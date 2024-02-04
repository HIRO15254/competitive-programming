import math


class Dijkstra():

    def __init__(self, n):
        self.route_list = [[math.inf] * n for _ in range(n)]
        self.node_num = n  # ノードの数

        self.now_a = -1

    def append_edge(self, a, b, dist):

        self.route_list[a][b] = min(dist, self.route_list[a][b])
        self.route_list[b][a] = min(dist, self.route_list[a][b])
        self.now_a = -1

    def append_edge_atob(self, a, b, dist):
        self.route_list[a][b] = dist
        self.now_a = -1

    def get_dist(self, a, b):
        return self.route_list[a][b]


    def search(self, a, b):
        unsearched_nodes = list(range(self.node_num))  # 未探索ノード
        self.distance = [math.inf] * self.node_num  # ノードごとの距離のリスト
        self.distance[a] = 0  # 初期のノードの距離は0とする
        # 最短経路でそのノードのひとつ前に到達するノードのリスト
        self.previous_nodes = [-1] * self.node_num

        while(len(unsearched_nodes) != 0):  # 未探索ノードがなくなるまで繰り返す
            # まず未探索ノードのうちdistanceが最小のものを選択する
            posible_min_distance = math.inf  # 最小のdistanceを見つけるための一時的なdistance。初期値は inf に設定。
            for node_index in unsearched_nodes:  # 未探索のノードのループ
                if posible_min_distance > self.distance[node_index]:
                    # より小さい値が見つかれば更新
                    posible_min_distance = self.distance[node_index]
            target_min_index = self.get_target_min_index(
                posible_min_distance, self.distance, unsearched_nodes)  # 未探索ノードのうちで最小のindex番号を取得
            unsearched_nodes.remove(target_min_index)  # ここで探索するので未探索リストから除去

            # ターゲットになるノードからのびるエッジのリスト
            target_edge = self.route_list[target_min_index]
            for index, route_dis in enumerate(target_edge):
                if self.distance[index] > (self.distance[target_min_index] + route_dis):
                    # 過去に設定されたdistanceよりも小さい場合はdistanceを更新
                    self.distance[index] = self.distance[target_min_index] + route_dis
                    # 　ひとつ前に到達するノードのリストも更新
                    self.previous_nodes[index] = target_min_index

    # 道順を探索
    def search_root(self, a, b):

        if a != self.now_a:
            self.search(a, b)
        previous_node = b
        root = []
        while previous_node != -1:
            root.append(previous_node)
            previous_node = self.previous_nodes[previous_node]
        root.reverse()
        return root

    def search_dist(self, a, b):
        if a != self.now_a:
            self.search(a, b)
        return self.distance[b]

    def get_target_min_index(self, min_index, distance, unsearched_nodes):
        start = 0
        while True:
            index = distance.index(min_index, start)
            found = index in unsearched_nodes
            if found:
                return index
            else:
                start = index + 1



N, A, B, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(N)]
dij = Dijkstra(N * 2)
for i in range(N):
    for j in range(N):
        dij.append_edge(i, j, D[i][j] * A)
        dij.append_edge_atob(i, j + N, D[i][j] * B + C)
        dij.append_edge(i + N, j + N, D[i][j] * B + C)
print(min(dij.search_dist(0, N - 1), dij.search_dist(0, 2 * N - 1)))