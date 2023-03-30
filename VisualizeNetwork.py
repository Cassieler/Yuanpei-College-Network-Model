import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# 生成有30个节点的随机图，每条边上的权重为随机值
G = nx.gnm_random_graph(30, 50)
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = round(10 * np.random.uniform(0, 1), 1)

# 将图画在一张很大的画布上
plt.figure(figsize=(10, 10))

# 绘制图形，根据边的权重来确定线条颜色和粗细
pos = nx.spring_layout(G)
edges = G.edges()
weights = [G[u][v]['weight'] for u, v in edges]
nx.draw_networkx_nodes(G, pos, node_size=500, alpha=0.8)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=weights, edge_color=weights, edge_cmap=plt.cm.Blues, alpha=0.8)

# 添加节点标签
labels = {}
for i in range(30):
    labels[i] = i
nx.draw_networkx_labels(G, pos, labels=labels, font_size=12)

# 显示图形
plt.axis('off')
plt.show()

# 计算度分布
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_count = dict(zip(set(degree_sequence), [0]*len(set(degree_sequence))))
for degree in degree_sequence:
    degree_count[degree] += 1
print("度分布：", degree_count)

# 计算平均度
avg_degree = sum(dict(G.degree()).values()) / float(G.number_of_nodes())
print("平均度：", avg_degree)

# # 计算类似度
# similarity_coefficient = nx.algorithms.similarity.adamic_adar_index(G)
# print("类似度：", list(similarity_coefficient))

# 计算群集系数
clustering_coefficient = nx.clustering(G)
print("群集系数：", clustering_coefficient)

# 计算平均路径长度
avg_path_length = nx.average_shortest_path_length(G)
print("平均路径长度：", avg_path_length)

# 计算度中心性
degree_centrality = nx.degree_centrality(G)
print("度中心性：", degree_centrality)



import networkx as nx
import community
import matplotlib.pyplot as plt

# 创建一个带权图
G = nx.Graph()
G.add_edge('A', 'B', weight=0.6)
G.add_edge('A', 'C', weight=0.2)
G.add_edge('C', 'D', weight=0.1)
G.add_edge('C', 'E', weight=0.7)
G.add_edge('D', 'E', weight=0.9)

# 计算每个节点的集群系数
cluster_coeffs = nx.clustering(G, weight='weight')

# 打印每个节点的集群系数
for node, cluster_coeff in cluster_coeffs.items():
    print(f"Node {node}: Cluster Coefficient {cluster_coeff}")

# 计算最优的社区划分
partition = community.best_partition(G, weight='weight')

# 绘制社区划分图
pos = nx.spring_layout(G)
colors = list(partition.values())
nx.draw(G, pos, node_color=colors, with_labels=True)
plt.show()
