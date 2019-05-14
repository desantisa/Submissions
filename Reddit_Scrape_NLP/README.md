***He Said She Said: Discussions among Men and Women on Reddit***

**Problem Statement**

Are men from Mars and Women from Venus? Do Reddit subthreads purported to be of greater interest to men and women distinguishable from each other? The objective of this analysis is to use natural language processing (NLP) to predict whether an article posted on Reddit is from the subthread r/men or from r/women based soley on the post title.

 
**Notebooks**

00. Scrape Methods: Documentation of different scraping methods attempted.
01. Reddit Scraper: Scraper used to data from Reddit using Pushshift.io API.
02. NLP & Classification Modeling: Includes EDA, natural language processing, classification modeling, and evaluation of selected model.
3. Data

Final dataset: reddit___gender___all.csv

Reddit_men.csv - Posts scraped from Reddit r/men

Reddit_women.csv: Posts scraped from Reddit r/women

**Presentation**

Data Collection & Processing
The data for this project were collected in December, 2018 and January 2019 using the pushshift.io API. It contains the entire set of submissions (at time of collection) to each subreddit, r/men and r/women

There were substantially more submissions to the women's subreddit, as compared to the men's.  This is reflected in the dataset.  As such, analyses were stratified so that each training and test dataset had equal proportions of submissions to the male thread.  Note that although the threads are presumed to address topics believed to be of interest to one specific gender, there are no requirements or presumptions made regarding the gender of the individuals posting submissions to each subthread.

After collection, the titles of each submission were processed according to the following steps:

Punctuation was removed.
Capitalization was removed so that only lowercase words would be returned.
Words were lemmatized.
Stop words were removed.

The data were split into training and testing data, then vectorized using CountVectorizer and TF-IDF methods, (and results were compared).

 
**Model Evaluation**

Accuracy scores generally ranged from .83 to .98.
Random Forest frequently misclassified posts in the men's subthread, but more accurately predicted posts in the women's thread. Models were slightly overfit, as training scores were 0.05 to 0.10 higher than testing dataset scores.

The words that were more likely to be from titles in r/women were abortion, pregnancy, breast, female, girl/girls, and world. 
The words that were more likely to be from titles in r/men were erection, cenforce, male, online, and treatment. The only overlapping words among men and women were best, like, and sex.
 

**Conclusions**

The various classification models could predict whether an article was from r/men or r/women by title alone with substantial accuracy.  Count vectorizers were more accurate than TF-IDF vectorizers. 

 
