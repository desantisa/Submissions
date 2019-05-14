# #Preventing Diabetes
#Can a Tweet per Day Keep the Doctor Away?: Using Natural Language Processing of Tweets to Assess Diabetes Risk


The current study analyzes text from social media data, and Twitter data in particular, to assess whether users might be at risk for type 2 diabetes, based on their tweets.  The search terms included were determined after first scraping 10 Reddit subthreads and analyzing those data with NLP to determine which words are unique to diabetes postings (e.g., diabetes and type2diabetes subthreads), as compared to general health (e.g., ask_docs, ask_health).



	1. Scrape Reddit subthreads for diabetes specific and for general health topics

        [Reddit Health Scraper](Submissions/DSI/Submissions/Reddit_health_scraper.ipynb)

	2. Count vectorize words from the subthreads and select words that are common in general health thread but not diabetes thread and vice versa

	3. Search for words unique to diabetes and not in Twitter

	4. Scrape the data and save in csv for NLP

	5. Conduct analyses - classification models (K-Means)

**List of Documents in Repository:**


| Reddit Scraper  | Reddit NLP|Reddit List of Top Terms| Twitter Scraper    | Twitter NLP | 
|---------|------------|------------|------------|---------|
|[Reddit Scraper](https://github.com/desantisa/Submissions/blob/master/Diabetes_Classify_Tweets/Reddit_health_scraper.ipynb)|[Reddit NLP](https://github.com/desantisa/Submissions/blob/master/Diabetes_Classify_Tweets/Reddit_NLP.ipynb)|[Reddit list of top terms](https://github.com/desantisa/Submissions/blob/master/Diabetes_Classify_Tweets/Reddit%20top%20terms.xlsx)|[Twitter Scraper](https://github.com/desantisa/Submissions/blob/master/Diabetes_Classify_Tweets/Twitter_scraper.ipynb)|[Twitter NLP](https://github.com/desantisa/Submissions/blob/master/Diabetes_Classify_Tweets/Twitter_NLP_clusters.ipynb)|

