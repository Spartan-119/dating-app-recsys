# Graph-based RecSys for Dating App

A graph-based recommendation system develops for dating app.

Documentation in Chinese -> https://hackmd.io/@kuouu/mlg_final

## Table of Contents

- [Introduction](#Introduction)
- [Related Work](#Related-Work)
- [Recommendation System](#Recommendation-System)
- [Evaluation](#Evaluation)
- [Conclusion](#Conclusion)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction

  With the Internet growing rapidly, people’s life is more rely on online services. Especially for the date during covid-19, everyone not only works from home but also makes new friends from home. I’m a marketing group member in a start-up called AInimal, a student group that is developing a dating app, I found that the number of chats is more than before the level 3 covid-19 alert. Furthermore, other dating apps even start advertising on social media. In conclusion, dating app may be an important part of future life, so how to give the user the best experience is a question that matter.

  However, one of the greatest problems is that users spent lots of time “swiping”, instead of building a strong and steady relationship with others. In other words, the recommender system is still not good enough. So, in this research, I want to propose an improved system for the dating app.

  Like social media, dating apps also hide a large network behind their system. I would like to use social network analysis to give visualize the picture of dating app users and apply graph neural network to build a recommender system. The former can give the marketing team a clearer reason to make decisions. The latter provides a more precise prediction that users may be interested in.

## Related Work

  Despite that the recommender system is a popular research topic in recent years, there are few focusing on dating apps. It can be the obstacle that finding an open dataset, or the relative research is owned by private usage. There are some papers or articles about recommender systems:
  
- [Recommender System for Online Dating Service](https://arxiv.org/pdf/cs/0703042.pdf) 2007 / 162 cites
- [RECON: A reciprocal recommender for online dating](https://www.researchgate.net/publication/221140972_RECON_A_reciprocal_recommender_for_online_dating) 2010 / 184 cites
- [Recommender Systems for Online Dating](https://core.ac.uk/download/pdf/33736431.pdf) 2015 / 6 cites
- [Design of Reciprocal Recommendation Systems for Online
Dating](http://web.cs.ucla.edu/~yzsun/papers/snam2016.pdf) 2016 / 24 cites
- [Shedding More Light on How Instagram Works](https://about.instagram.com/blog/announcements/shedding-more-light-on-how-instagram-works?fbclid=IwAR0L5kk9JEu3dEmz1VqIETTOevSWoc0IcZceaGTS9Vj_m0LccUGuJGsu_T0)

Shedding More Light on How Instagram Works
  In these studies, CF (Collaborative Filtering) is the state-of-art technique in this field. The recommender system using deep learning is not usual.

## Recommendation System

### Rule-Based Method

Before jumping into the Graph Neural Network, I want to use some rule-based methods to match people and make the comparison with GNN method. Considering my experience in dating apps, recommending people who are "talkative" is much more critical than the "matched" one. In addition, it also helps me to achieve the goal-make the chat hot.

||talkative|non-talkative|
|-|-|-|
|talkative|Good match|Maybe|
|non-talkative|Maybe|Difficult|

In this situation, talkative people may always be recommended to the new user. But if we consider the time limit to reply to the message, they may lower the score if they reach the maximum, avoiding matching the same people to everyone.

#### Average Chat Volume

According to **Average Chat Volume** to recommend.

$$
Average Chat Volume = \frac{\sum_{Chats}Words}{NumOfChats}
$$

#### pseudo code

1. get G
2. get user_list
3. remove random edge, get G’
4. get rec_list by G’
5. validation

### Graph Neural Network

![](https://i.imgur.com/InUM1lC.png)

The purpose of using Graph Neural Network is nothing more than to obtain local or global information on the graph and to obtain additional information for matching in addition to the currently collected data. Therefore, my idea is to combine GNN with the large Collaborative Filtering of the current dating software recommendation system research to make recommendations.

#### GNN

Use GCN to get node embedding, and use similarity to do user Collaborative Filtering


1. GCN learning node embedding
2. Be the CF of user user

## Evaluation

There are many ways to verify the recommendation system, but considering the situation of the actual data, there are many ways that are not suitable. The main problem is that "too little chat in a single chat room" data accounts for a large part of the whole, which makes the information seriously unbalanced. If these data are removed, the data will become too small to reflect the average situation.

So here I use the recall rate (Recall) as an evaluation method, that is, the ratio of "prediction" to "actual," and it is also considered that it is better to debug when there is a problem (print out the lists on both sides).

### recall

$$
Recall(pred, label) = \frac{OccurrencesOfPred}{LengthOfLabelList}
$$

### Network Diagram

#### 2020

![](https://i.imgur.com/RZDZmru.jpg)

#### 2019

![](https://i.imgur.com/GWaqJiI.jpg)

The above data are from 11/01 to 11/15 in 2020 and 2019, respectively. You can see that besides the lump in the middle, there is a circle of single dots outside. That circle is the users who are not playing. You can zoom in to see I saw that the arrows were all pointing inwards; someone sent him a message, but he didn't reply. Maybe it was deleted immediately after downloading, or it was not chatting.

When planning, I didn't expect that this situation would have such a severe impact, so I went to test directly, and the results are as follows:

- rule base: < 0.1

But after removing inactive users, the Recall of the rule base is increased to about 0.1 ~ 0.2. Although there is a significant improvement, it is still not high.

Many points have "no outward edge"; many users are not using it, and they may download it to take a look and never log in again. Therefore, I will remove the inactive users after adding the user feature. And change the color according to gender, the graph becomes as follows.

![](https://i.imgur.com/y3oCvyg.jpg)

After matching according to gender, there is a significant improvement. I forgot that the majority of dating software is male-female matching!

- The Recall of the rule base is increased to about 0.1 ~ 0.5
- GNN is about 0.4 ~ 0.5 (more stable

But it's not too high. It's not even better than using personality for deep learning before. Even if my current method of use is more logical, I believe the current direction is correct, but there may still be a lot of information. The place to deal with has not been considered. I will list the problem points I think of so far in the next.

### Problems

- A snapshot of the database at each point in time is required, ex: update time, today's login, friendship status
- Insufficient data after removing inactive users (requires data over time
- untagged material

## Conclusion

This project applied GNN on dating apps, including:

- Use graphs to visualize data and analyze user habits
     - chat status
     - pairing preference
     - Average chat volume
- Use user data in the time range for matching
     - rule base
     - Graph Neural Network

### future work

- Use network diagrams to present the current user status
     - The pictures in this article use a spring layout, and there should be a better way to present them
- Regularly back up the state of the database for training
- Improve the software pairing mechanism to obtain tagged data
     - Swipe right to like, swipe left to dislike
     - Pair scoring mechanism

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
<br />

## Contact

About me: [Yu-Tsung (Eric) Kuo](https://www.linkedin.com/in/kuouu/) - erickuo5124@gmail.com

Project Link: [https://github.com/kuouu/dating-app-recsys](https://github.com/kuouu/dating-app-recsys)


