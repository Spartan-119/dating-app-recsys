import pickle
import networkx as nx
import numpy as np
from data_processing import get_user_graph

if __name__ == '__main__':
  np.set_printoptions(suppress=True)
  try:
    G = pickle.load(open('./data/graph.pickle', 'rb'))
  except:
    G = get_user_graph(start='2021-05-01')
  
  weight_sum = []
  for u in G.nodes:
    summ = np.array([G[u][v]['weight'] for v in G[u]]).sum()
    weight_sum.append(summ)

  weight_sum = np.array(weight_sum)
  idx = np.argsort(-weight_sum)
  nodes = np.array(G.nodes)

  ranking_list = [(node, weight) for node, weight in zip(nodes[idx], weight_sum[idx])]
  print(ranking_list)
