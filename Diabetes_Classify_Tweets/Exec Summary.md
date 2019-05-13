# #Preventing Diabetes
# Can a Tweet per Day Keep the Doctor Away?: Using Natural Language Processing of Tweets to Assess Diabetes Risk

**Problem Statement:**

* Is it possible to assess a person's risk for diabetes mellitus from a person's Twitter feed?


# Background

A number of recent studies have utilized Natural Language Processing (NLP) to analyze Twitter and other social media data to aid in public health research via a number of different mechanisms.   

Social media data have been used to recruit participants for health research, to promote health awareness and health-related campaigns, and to analyze real-time data about a number of subjects (e.g., physical activity and sleep).

Recently, it has become increasingly common to use social mediat data to assess the risk and spread of diseases.  To date, social media data have been most commonly been used to track infections disease, such as H1N1, seasonal influenza, and dengue (cites).  On occasion, researchers have also analyzed social media data to explore the transmission of sexually transmitted infections (STIs) and the prevalence of depression and/or suicidal ideation.

On the other hand, it has been much less common to investigate the use of social media to investigate non-communicable diseases (NCDs), particularly with respect to cardio-metabolic health.

The current study analyzes text from social media data, and Twitter data in particular, to assess whether users might be at risk for type 2 diabetes, based on their tweets.  The search terms included were determined after first scraping 10 Reddit subthreads and analyzing those data with NLP to determine which words are unique to diabetes postings (diabetes and type2diabetes subthreads), as compared to general health (ask_docs, ask_health).

NLP analyses of Reddit threads were used to inform the second round of webscraping - of Twitter.


# Analytical plan

	1. Scrape Reddit subthreads - for diabetes specific and for general health topics
	2. Count vectorize words from the subthreads and select words that are common in general health thread but not diabetes thread and vice versa
	3. Search for words unique to diabetes and not in Twitter
	4. Scrape the data and save in csv for NLP
	5. Conduct analyses - classification models (K-Means)
	6. Review the data within each cluster and determine common themes / why they are grouped together
	7. Iterate, try different numbers of clusters.  Remove irrelevant data systematically whenever possible
	8. Next steps: Described below
	

# Scraping Reddit 

	•	Reddit subthreads scraped

	1.	Type2diabetes
	2.	Diabetes 
	3.	Ask_docs  
	4.	Ask_health  
	5.	Diagnose me  
	6.	Diet 
	7.	Food   - Deleted
	8.	Medical 
	9.	Med_help 
	10.	Nutrition  
	

	I analyzed titles from these subthreads with count vectorizors to determine the most frequently mentioned words relevant to diabetes and general health to inform my subsequent Twitter search.
	
	http://localhost:8888/notebooks/DSI/Submissions/Reddit_health_scrape_final.ipynb


 
 
#Reddit NLP	 	



* Words that appear more in diabetes-specific and general health sub-threads 

•	Reddit top words that are common to both diabetes AND ask docs
		o	Blood sugar
	

•	Reddit top words in general health subthreads that are not among most frequent words in diabetes threads

	o	Chest (2018)
	o	Doctor (2018)
	o	Heart (2018)
	o	Symptoms (2018)
	o	Pain (2018)
	o	Skin (2018) 
	

•	Reddit top words that are in diabetes not ask docs
 
	o	A1c
	o	Insulin (pump)
	o	Blood sugar 
	o	Fasting 
	o	Fat 
	o	Carbs
	o	Glucose 
	o	Diet  
	
Next, the top words from the Reddit count vector analyses were used in Twitter searches and were scraped.


NLP 
     
   	Reddit 
Find top words and frequencies for each individual subthread 

Categorize Diabetes vs other categs combined
	Diabetes vs health / nutrition

              precision    recall  f1-score   support

           0       0.99      0.99      0.99    554020
           1       0.86      0.79      0.82     36466

	   micro avg       0.98      0.98      0.98    590486
	   macro avg       0.92      0.89      0.91    590486
	weighted avg       0.98      0.98      0.98    590486
	

 

 
# Scraping Twitter  
The list of terms searched are noted below.  Although terms appear to be redundant, each query returns approximately 400 tweets per month.  There is virtually no overlap.  Moreover, the more specific terms "I have diabetes" are more likely to be posted by individuals, rather than public service announcements from organizations.  It also appears upon glancing that specifying type 2 diabetes, rather than simply diabetes, removes some of irrelevant spam.
	Words and Time periods searched 
	 
	 	Diabetes / diabetic
	 	Diagnosis / diagnosed
	 	
		I was diagnosed with t2 / type 2 diabetes
		I was diagnosed with diabetes  
		I have diabetes
		I have type 2 / t2 diabetes
		I am /I'm diabetic
		I am a diabetic

Additional words searched (determined from Reddit NLP):
			
		o	Chest (2018)
		o	Doctor (2018)
		o	Heart (2018)
		o	Symptoms (2018)
		o	Pain (2018)
		o	Skin (2018) 

	
These terms were searched and scraped due to being frequently mentioned in general health threads but not diabetes specific threads.  After retrieving all the tweets from the API for these phrases (Jan 2012-Feb 2019, approximately 400 tweets per month), additional general health terms were searched.

The general health terms included the most common words from the Reddit Ask_Docs and /or Ask_Health subthreads that were distinct from the Reddit Diabetes and Type 2 Diabetes subthreads.

The data were analyzed using both Count vectorizer, and TF-IDF vectorizors.  Texts were lemmatized and stopwords removed, etc. in accordance with standard NLP practice.

Graphs of top terms, Reddit classification models 
	http://localhost:8888/notebooks/DSI/Submissions/Reddit_NLP_final.ipynb 

* Additional code for possible next steps (geolocation, user information, etc.)
	http://localhost:8888/notebooks/DSI/Submissions/Twitter_scraper_final.ipynb  


All files from Twitter searches were merged into one dataframe
http://localhost:8888/notebooks/DSI/Projects/Capstone/Merge_Twitter_all_files_final.ipynb 

* Twitter NLP 
	– 	Preprocessing (Regex, lemmatizing, stop words, etc.)
		Count vectorizer, TF-IDF

* Analyze clean corpus using K-means clustering 
DBSCAN??
http://localhost:8888/notebooks/DSI/Projects/Capstone/Twitter_NLP_final.ipynb 

#Summary:
Ultimately, two k-means models were investigated, grouping the corpus into 5 and 10 clusters.  Although the differences between clusters were not immediately evident, there were a few clusters that could easily be identified. Specifically, one cluster focused on singer Nick Jonas (revealed to be diabetic) and his wife Priyanka Chopra.  Second cluster was primarily in Spanish.  It would be ideal to have researchers who are fluent in Spanish examine the relevance of the tweets, as well as how tightly the topics "hang together" other than simply being in Spanish.  Finally, there was one cluster in which most people report being "diagnosed" with something, most often cancer, although the range of diagnoses is quite diverse.  

Although the clusters could not immediately be used to directly identify Twitter users who have or at risk of diabetes, the initial models do allow for simple elimination of a substantial number of tweets on the basis of being irrelevant.  This is an important first step toward the ultimate goal of being to accurately identify Twitter users at high risk of diabetes.  

The next goal is to continue to eliminate clusters believed to be irrelevant and iterate using different numbers of clusters.  Also,  additional data / tweets on words identified as frequently used on Reddit diabetes and generic health subthreads will be collected and analyzed. Additional steps may include identifying the specific users who explicitly self-identify as type 2 diabetics and track their Twitter handles.  These texts would eventually be analyzed as a corpus along with tweets by other users whose diabetes status is unknown. That could prove to be a highly effective method of identifying and reaching out to users at risk of diabetes nationwide, and could prove especially useful for targeting users in rural areas farther from traditional health services and /or those with less access to high quality preventive health services.


#Challenges:

One of the most common challenges is that family / friends often post on behalf of others.  Often family members or friends are looking for advice or suggestions about how to support diabetic family members. These findings are not irrelevant information but not ideal for directly targeting individuals in need.

It is similarly not uncommon to discuss dogs/pets who have diabetes, although substiantially less common than family members and friends.  These people would obviously not be the target of potential awareness and outreach efforts, but researchers could attempt to filter out animal words, although some diabetics post about their pets supporting them.

One of the most difficult issues to deal with is people making jokes.
For example, one person tweeted, “I had to turn cookies off in my browser because my laptop was recently diagnosed with type 2 diabetes.’  On numerous occasions, people have tweeted "he/she/it is so sweet, I might get diabetes."

Most of the searches have not distinguished betwee Type 1 and type 2 diabetes.  There were searches that specifically referenced type 2, but general searches did not exclude either type or try to distinguish between them.  Many promotional campaigns would likely focus on type 2, which is more strongly linked to lifestyle and much more amenable to lifestyle changes.

There are small clusters of tweets during specific periods when celebrities announce they have diabetes (e.g., Nick Jonas, Tom Hanks, Jay Cutler).  This tends to create a spike in discussions, not exclusively among diabetics, although many who post do identify as diabetics. 



#Possible next steps:

1. Redo the some of the word processing to avoid breaking up some obvious words - and deleting useless words (e.g., does) 
2. Analyze words from those who self-describe diabetics. Count vectorize their texts and compare results to words from Reddit diabetes subthreads to see whether / how things differ.
3. Try different numbers of clusters.  For the first 2 rounds, 5 and 10 clusters were selected.  The ideal number of clusters could potentially be more or fewer than that.
4. Re-analyze data after removing clusters that are clearly irrelevant(?)
5. Examine geocodes for all relevant tweets and compare to percentage of expected Twitter users in relation to known prevalence of diabetes in an area.

 

#Reddit Results 
	
	
	Top 20 Words for diabetes thread   
 
		a1c            1041
		advice         1044
		blood          2886
		blood sugar    1828
		cgm            1023
		dexcom         2110
		diabetics      1121
		diagnosed      1259
		does           1301
		glucose        1250
		help           2229
		high           1095
		insulin        3475
		just           1770
		low            1457
		need           1507
		new            1747
		pump           2133
		question       1494
		sugar          2598
		t1             1869
 

	Top Words for Type 2 diabetes thread 
	
		a1c            18
		advice         13
		bg             11
		blood          44
		blood sugar    30
		carb           12
		cure           11
		diabetics      12
		diagnosed      32
		diet           17
		eat            12
		fasting        12
		fat            11
		free           26
		glucose        18
		got            12
		health         11
		help           38
		high           16
		insulin        22
		just           20
		keto           31
		low            17
		metformin      17
		need           24
		new            28
		people         14
		research       16
		study          15
		sugar          47
		survey         23
		t2             17
		weight         13
 
 
	Top Words for the Ask Docs thread
 
	blood        8941
	chest        5747
	days         5065
	doctor       7475
	does         6526
	ear          5298
	heart        5085
	help        15807
	just         6421
	left         7806
	like         8632
	need         7286
	pain        29392
	possible     5843
	question     7725
	rash         5563
	red          6041
	right        7736
	skin         7665
	symptoms     5764
	throat       5758
	weird        6384
 
 

	Top Words for the Diagnose Me thread 
		bad          55
		blood        69
		day          54
		does         86
		health       53
		help        155
		just         66
		like         71
		pain        154
		question     54 
		ago         142
		blood       104
		bump        117
		bumps       168
		chest       142
		days        154
		doctor      121
		does        112
		don         122
		eye         118
		feel        101
		feeling     107
		foot        104
		got         106
		help        361
		hurts       106
		itchy       188
		just        229
		know        158
		left        168
		leg         136
		like        353
		months      150
		neck        115
		pain        649
		painful     114
		rash        196
		red         257
		right       189
		skin        238
		small       116
		sore        125
		spot        105
		spots       117
		sure        105
		swollen     122
		symptoms    167
		throat      217
		ve          175
		weeks       110
		weird       200
		white       128
		wrong       115
		years       150 
 
  
	Top Words for the Medical Help thread 
		ago           33
		blood         24
		days          29
		doctor        24
		don           30
		eye           23
		foot          24
		got           26
		graphic       26
		head          22
		help         193
		hurt          27
		hurts         26
		just          44
		know          49
		left          26
		leg           23
		like          60
		little        22
		medical       44
		need          58
		need help     31
		pain         101
		really        26
		red           29
		right         28
		skin          25
		stomach       22
		sure          21
		throat        25
		toe           24
		ve            26
		weird         35
		worried       24
		wrong         22
		
	 
	Top Words for the Medical thread  
		advice       1183
		ago          1040
		best         1125
		blood        1743
		days         1191
		doctor       1745
		does         1700
		ear          1043
		global       1111
		help         4393
		just         1857
		know         1675
		left         1425
		like         2301
		market       2048
		medical      5632
		need         1911
		pain         5201
		question     1371
		rash         1124
		red          1277
		right        1527
		skin         1502
		surgery      1327
		throat       1035
		treatment    1144
		ve           1145
		weird        1363
		years        1019
	 

 
	Top Words for the Food / Nutrition thread 
		ate          73154
		bacon        11294
		blood        11584
		cake         14359
		cheese       19524
		chicken      29050
		chocolate    13080
		does         11035
		food         19135
		fried        11649
		help         24424
		just         11808
		like         14961
		need         12001
		pain         35709
		pizza        13927
		pork         11333
		red          13024
		sauce        11896

