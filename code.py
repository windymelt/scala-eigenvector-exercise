import networkx as nx
import sys
import time
import matplotlib.pyplot as plt

def calculate_eigenvector_centrality(node_count):
    """
    ランダムなグラフを生成し、固有ベクトル中心性を計算する関数。

    :param node_count: グラフのノード数
    :return: ノードごとの固有ベクトル中心性
    """
    output_filename = "graph_eigenvector_centrality.png"
    print(f"Calculating eigenvector centrality for a random graph with {node_count} nodes...")
    # 1. ランダムなグラフを生成
    G = nx.powerlaw_cluster_graph(node_count, 2, 0.02)  # pはエッジが作られる確率
    print(f"Number of nodes: {G.number_of_nodes()}")

    # 2. 固有ベクトル中心性を計算
    try:
        eigenvector_centrality = nx.eigenvector_centrality_numpy(G, max_iter=100, tol=1e-6)
        # node_sizes = [3000 * centrality for centrality in eigenvector_centrality.values()]
        # labels = {node: f"{centrality:.2f}" for node, centrality in eigenvector_centrality.items()}

        # # 4. グラフを描画
        # plt.figure(figsize=(40, 32))
        # pos = nx.spring_layout(G)  # レイアウトを決定
        # nx.draw(
        #     G,
        #     pos,
        #     with_labels=True,
        #     labels=labels,
        #     node_size=node_sizes,
        #     node_color="lightblue",
        #     font_size=10,
        #     font_color="darkred",
        #     edge_color="gray",
        # )
        # plt.title("Graph with Eigenvector Centrality", fontsize=16)

        # # 5. PNG画像として保存
        # plt.savefig(output_filename, format="png", dpi=300)
        # plt.close()

        # print(f"Graph saved as {output_filename}")
    except nx.NetworkXException as e:
        print(f"Error in eigenvector centrality computation: {e}")
        return {}

    return eigenvector_centrality


if __name__ == "__main__":
    # コマンドライン引数からノード数を取得
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <number_of_nodes>")
        sys.exit(1)

    try:
        node_count = int(sys.argv[1])
    except ValueError:
        print("Error: <number_of_nodes> must be an integer.")
        sys.exit(1)

    if node_count <= 0:
        print("Error: <number_of_nodes> must be a positive integer.")
        sys.exit(1)

    # 実行時間の測定開始
    start_time = time.time()

    # 固有ベクトル中心性を計算
    centrality = calculate_eigenvector_centrality(node_count)

    # 実行時間の測定終了
    end_time = time.time()

    # 結果を表示
    if centrality:
        print("\nEigenvector Centrality for each node:")
        for node, value in centrality.items():
            if node < 100:
                print(f"Node {node}: {value:.6f}")

    # 実行時間を表示
    print(f"\nExecution Time: {end_time - start_time:.6f} seconds")
