import pickle
import networkx as nx
import numpy as np
from utils.data_processing import get_user_graph
from random import choice, sample
from utils.evaluation import Recall

PRED_NUM=20

# return highest avg number of msg user list
def get_global_list(G):
  avg_weight = []
  for u in G.nodes:
    # weight sum, avg weight, avg weight with maximum
    avg = np.array([G[u][v]['weight'] for v in G[u]]).sum() / G.degree[u]
    avg_weight.append(avg)

  avg_weight = np.array(avg_weight)
  idx = np.argsort(-avg_weight)
  nodes = np.array(G.nodes)

  print([(node, weight) for node, weight in zip(nodes[idx], avg_weight[idx])])
  ranking_list = [node for node in nodes[idx]]
  return np.array(ranking_list[:PRED_NUM])

# return user's list of highest messaging user
def get_user_list(G, u):
  weights = []
  for v in G[u]:
    weights.append(G[u][v]['weight'])
  weights = np.array(weights)
  idx = np.argsort(-weights)
  friends = np.array(G[u])
  ranking_list = [(node, weight) for node, weight in zip(friends[idx], weights[idx])]
  return np.array(ranking_list)

if __name__ == '__main__':
  np.set_printoptions(suppress=True)
  try:
    G = pickle.load(open('./data/graph.pickle', 'rb'))
  except:
    G = get_user_graph(start='2021-05-01')

  pred = get_global_list(G)

  random_users = sample(list(G.nodes()), 30)
  ans = []
  for user in random_users:
    ans.append(get_user_list(G, user))
  ans = np.array(ans)

  print(Recall(predict=pred, answer=ans))
