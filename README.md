# Coronavirus twitter analysis

## Project Summary

In this project, I analyzed the geotagged tweets sent in 2020.
I particularly focused on a set of hashtags related to coronavirus to see the number of times they were used.
Using the data from the tweets, I was able to compare which countries and languages used the hashtags the most and produce graphs to visualize this data.
I also used an alternative reduce function to analyze the frequency of the hashtags throughout the year of 2020, which yielded interesting results based on the hashtags.

## Background

Approximately 500 million tweets are sent everyday with about 2% being geotagged. 
In this project, I will be analyzing the 1.1 billion geotagged tweets sent in 2020.
To do this, I followed the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) procedure to analyze these tweets.
My map.py file parsed through the tweets and kept track of the country code and language correspondig to each tweet using a particular hashtag.
Then, I reduced the data using my reduce.py file to merge all the outputs.
In order to visualize the data, I created code using the matplotlib library.

## Results

**Bar Graphs Analyzing Country and Language for Hashtags**

<img src=coronavirus_country.png width=100%/>

This graph shows the number of tweets in the top 10 countries that posted a tweet containing #coronavirus in 2020. 
The hashtag was most popoular in the US and 10th most popular in Turkey.

<img src=coronavirus_lang.png width=100%/>

This graph shows the number of tweets using #coronavirus written in the top 10 languages.


<img src=korean_coronavirus_country.png width=100%/>

This graph shows the number of tweets in the top 10 countries that posted a tweet containing #coronavirus in Korean in 2020. 
The hashtag was unsurprisingly most popoular in the Korea and 10th most popular in Australia.

<img src=korean_coronavirus_lang.png width=100%/>

This graph shows the number of tweets using #coronavirus in Korean written in the top 10 languages.

**Line Graphs Comparing Hashtag Usage Over Time**

These graphs compare how often a hashtag was used on a given date in 2020. I picked hashtags that had similar meanings to analyze which was most common.

<img src=hashtag_comparison_coronavirus.png width=100%/>

<img src=hashtag_comparison_coronavirus_corona.png width=100%/>

<img src=hashtag_comparison_cough_sneeze.png width=100%/>

<img src=hashtag_comparison_covid2019_covid-2019_covid19_covid-19.png width=100%/>

## Conclusion

In conclusion, I learned how to use MapReduce to parse through data and analyze specific traits.
I have used matplotlib before but enjoyed the flexibility of formatting the graphs.
My biggest challenge was creating my Alternative Reduce program as I had issues visualizing the dates in accordance with each tweet.
I enjoyed this project because it allowed me to use the knowledge from this course and apply it to a real-life issue.
