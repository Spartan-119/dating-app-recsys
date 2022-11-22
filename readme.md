# Graph-based RecSys for Dating App

A graph-based recommendation system develops for dating app.

Documentation in Chinese -> https://hackmd.io/@kuouu/mlg_final

## Table of Contents

- [Introduction](#getting-started)
- [Related Work](#usage)
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
Average Chat Volume = \frac{\sum_{Chats}Words}{Num _of _Chats}
$$

## Evaluation

## Conclusion

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



在設計時，我預期了一些使用者可能遇到的問題，以及對於使用交友軟體的期望，得到的結論是：比起推薦所謂「匹配」的人，不如推薦「很會聊」的人給使用者，達到我們預期效果---聊天熱絡---的比例說不定會比較高。

那問題就會變成怎麼定義「很會聊」，我自己的解釋會是在一定時間下的聊天量，與開啟的聊天室數量的比例，也就是「平均聊天量」。一個人如果面對不同的人、不同的情況下都能侃侃而談，那他應該就會是我們大力推薦給其他使用者的人；相對來說如果那個人只有對幾個人比較聊得開，那可能就是碰巧遇到而已，分母很大的情況下會拉低分數，更不用說很少在回訊息的人了。

||會聊|不會聊|
|-|-|-|
|會聊|一定聊得來|有機會聊起來|
|不會聊|有機會聊起來|有點困難|

在這個情況下，「很會聊」的人會被一直配對到新的使用者，考量到一個人的時間有限，回訊息的量總有一個極限，到達極限之後再增加聊天室會讓分數降低，如此一來就能避免永遠只有一個人會被配對到的情況。

#### 平均聊天量

依據當下的**平均聊天量**由高至低做推薦

$$
平均聊天量 = \frac{\sum_{聊天室}聊天字數}{聊天室數量}
$$


#### 期望結果

- 會聊天的人優先，會“被”配對到很多人
- 不會聊天的人比較不會被主動配對到
- 在時間內配對到一定程度會讓聊天量下降，後面順位的人往上排名

#### 解決的問題

- 配對到的人最近一定有在玩，而且很活躍
- 雙方至少有一人有一定的社交程度，造成尷尬開場的機率較低（難聊的人不會互相遇到）
- 聊天室數量增加會降低平均聊天量，因此過度配對會降低排名，不會有某個人一直配對到超多人的情況
- 與比較會聊的人配對，增加社交能力較低的人的自信

#### pseudo code

1. get G
2. get user_list
3. remove random edge, get G’
4. get rec_list by G’
5. validation

### Graph Neural Network

![](https://i.imgur.com/InUM1lC.png)

使用 Graph Neural Network 的目的不外乎就是獲得圖上 local 或是 global 的資訊，能在目前搜集的資料之外獲得更多額外的資訊來做配對。因此我的想法是結合 GNN 跟目前交友軟體推薦系統研究的大宗 Collaborative Filtering 來做推薦。

#### GNN

用 GCN 得到 node embedding ，並使用 similarity 做 user user 的 Collaborative Filtering


1. GCN 學習 node embedding
2. 做 user user 的 CF

---

## 實作

### Evaluation

對於推薦系統的驗證方式其實有很多種，但考量到真實資料的狀況，其實有很多方式是不太合適的。最主要的問題是「單一聊天室聊天量太少」的資料佔整體的很大一部分，這使資料嚴重的不平衡，若是移除這些資料又會讓資料變得太少，不足以反映平均的狀況。

因此在這裡我是使用召回率（Recall）來做評價的方式，也就是「預測」出現在「實際」上的比例，其中也考慮到有問題時比較好 Debug（將兩邊的 list 印出）。

#### recall

$$
Recall(pred, label) = \frac{pred 出現在 label\_list 出現次數}{label\_list 的長度}
$$

### Data set

| 資料名稱 | 數量 | 
| -------- | -------- | 
| user | 5043 |
| chat | 290559 |
| friend | 22683 |

上面是目前資料庫中整體的資料狀況，但在訓練的過程中，會將資料以「一段時間」來做取用，因為這篇研究強調「當下狀況」，而不是整體的表現。實際是使用一個月來訓練，以抓取 2020 年 11 月來說，大約可以獲得 300 個左右的使用者，訊息總量大約是 20000 上下，但實際上經過篩選後的資料又更少了。

在取得使用者的 node feature 部分我是使用以下幾種資料：

- gid
- gender
- animal
- heart
- type
- personality
- bgm
- active_time

當然資料庫裡面並不只有這些，還有一些上線時間等等的資料，但考量到是以時間間隔來做訓練，再抓資料的時候如果不是抓最新資料，有些資料就沒有辦法使用，例如：最後上線時間。

如果有要發展下去之後可能要定期備份資料庫 snapshot。

#### 網路圖

##### 2020

![](https://i.imgur.com/RZDZmru.jpg =450x) 

##### 2019

![](https://i.imgur.com/GWaqJiI.jpg =450x)

上面分別為 2020, 2019 年 11/01～11/15 的資料，可以看到除了中間那一坨之外，外面還有一圈單個的點，那圈就是比較沒有在玩的使用者，放大看可以看到箭頭都是往內，也就是別人傳訊息給他，但他都沒有回，可能是下載之後馬上就刪掉了，又或者單純是沒有在聊天。

事前規劃的時候沒有想到這個情況會影響這麼嚴重，直接就下去測試，結果如下：

- rule base: < 0.1

但在移除不活躍的使用者之後，rule base 的 Recall 提升至約 0.1 ~ 0.2 雖然是有很明顯的提升，但還是不高。

其實很多點“沒有往外的邊”，也就是很多使用者沒有在使用，可能只是下載來看一看就再也沒有登入了，因此在加入 user feature 之後，我將不活躍的使用者移除，並按照性別改變顏色，圖形變成如下

![](https://i.imgur.com/y3oCvyg.jpg =600x)

按照性別配對之後就有顯著的提升了，我居然都忘記交友軟體的大宗還是男女配對啊！

- rule base 的 Recall 提升至約 0.1 ~ 0.5
- GNN 約為 0.4 ~ 0.5（較穩定

但其實也不算是太高，相比之前使用性格做深度學習的甚至沒有比較好，就算我現在的使用方法是比較有邏輯性的，我相信現在的方向是正確的，只是可能還有很多資料處理的地方沒有考慮到，我把目前想到的問題點列在下一點。

### 問題點

- 需要每個時間點資料庫的 snapshot，ex: 更新時間、今日登入、交友狀況
- 移除不活躍的使用者之後資料不足（需要一段時間內的資料
- 沒有標記的資料

---

## 結論

本篇研究圖（Graph）在交友軟體上的應用，包括：

- 利用圖形來視覺化呈現資料並分析使用者習性
    - 聊天狀況
    - 配對偏好
    - 平均聊天量
- 使用時間區段內的使用者資料來做配對
    - rule base
    - Graph Neural Network

### future work

- 利用網路圖來呈現目前使用者的狀況
    - 本篇當中的圖是使用 spring layout，應該有更好的呈現方式
- 定期備份資料庫狀態以拿來做訓練
- 改善軟體配對機制，取得標記資料
    - 右滑喜歡、左滑不喜歡
    - 配對評分機制

