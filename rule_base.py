import pickle

from pymysql import NULL
import networkx as nx
import numpy as np
from data_processing import get_user_graph
from random import choice, sample
from evaluation import Recall

PRED_NUM=10

# return highest avg number of msg user list
def get_global_list(G):
  male_list = [n for n in G.nodes if G.nodes[n]['gender'] == 'male']
  female_list = [n for n in G.nodes if G.nodes[n]['gender'] == 'female']
  avg_weight = []
  male_weight = []
  female_weight = []
  for u in G.nodes:
    # weight sum, avg weight, avg weight with maximum
    avg = np.array([G[u][v]['weight'] for v in G[u]]).sum() / G.degree[u]
    avg_weight.append(avg)
    if G.nodes[u]['gender'] == 'male':
      male_weight.append(avg)
    else:
      female_weight.append(avg)

  avg_weight = np.array(avg_weight)
  idx = np.argsort(-avg_weight)
  nodes = np.array(G.nodes)
  ranking_list = [node for node in nodes[idx]]
  # print([(node, weight) for node, weight in zip(nodes[idx], avg_weight[idx])])

  male_weight = np.array(male_weight)
  male_idx = np.argsort(-male_weight)
  male_nodes = np.array(male_list)
  male_ranking = [male_nodes for male_nodes in male_nodes[male_idx]]

  female_weight = np.array(female_weight)
  female_idx = np.argsort(-female_weight)
  female_nodes = np.array(female_list)
  female_ranking = [female_nodes for female_nodes in female_nodes[female_idx]]

  return np.array(male_ranking), np.array(female_ranking)

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
    G = get_user_graph(start='2021-04-01')

  pred_male, pred_female = get_global_list(G)

  sample_num = int(len(G.nodes()) / 10)
  random_users = sample(list(G.nodes()), sample_num)
  ans = []
  ans_male = []
  ans_female = []
  for user in random_users:
    ans_list = get_user_list(G, user)
    ans.append(ans_list)
    if G.nodes[user]['gender'] == 'male':
      ans_male.append(ans_list)
    else:
      ans_female.append(ans_list)
  ans = np.array(ans, dtype=object)
  ans_male = np.array(ans_male, dtype=object)
  ans_female = np.array(ans_female, dtype=object)

  # print(Recall(predict=pred, answer=ans))
  print(Recall(predict=pred_male, answer=ans_female))
  print(Recall(predict=pred_female, answer=ans_male))
