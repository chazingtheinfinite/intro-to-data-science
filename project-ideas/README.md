# Project Ideas to Select from or to Inspire your Own

Course Developer: Kevin Dick ([kevin.dick@carleton.ca](mailto:kevin.dick@carleton.ca))

---

Your Intro. to Data Science course project must include *online data scraping to generate a new dataset* and/or *analyze the dataset in unique ways to produce new knoweldge*. Typically a scraping-based project will naturally include both of these criteria. We recommend that groups extensively research their proposed scraping target prior to committing to a given project topic. For groups that prefer to avoid a scraping component as part of their projects, please consider one of the topics listed below (and in each subdirectory here) for details on the proposed analysis method. If student groups are interested in defining their own project based on an existing dataset, it is imperative that you communicate with course developer (Kevin Dick; mailto:kevin.dick@carleton.ca) about your proposed project. 

When searching online for potential scraping-based data science projects, a number of recurrent themes are listed including: 
 - Financial Stock Value Scraping and Analysis
 - Social Media Scraping and NLP Analysis
 - eCommerce Product Price/Review Scraping and Comparison

While these types of projects are common, it is important that your project answers a number of new questions and does not repleat previous work. Listed below are a number of potential projects you and your group may select from for your course project. These may also help inspire your own project ideas. The following projects are typically organized such that only one group may complete the project and therefore they may be claimed on a first-come-first-served basis. As metioned, please be sure to fully research your selected project idea before settling on it.

## Structured Project Ideas 

The following subsections describe several structured projects that students are welcome to consider and fully research them for project feasability before commiting to one of these ideas.

---

## Project 1: Web Scraping Crypto Currency Prices to Explore what Makes certain Coins Appealing

Recommended for:
 - Students interested in acquiring and analyzing financial data
 - Students looking to scrape their own dataset
 - Students interested in Natural Language Processing

Cryptocurrencies have recently been growing in popularity given the metoeric rise and fall of certain coins over the last few years. With an increasingly digitized future, cryptocurrency may eventually become an effective means of payment.

For this project, we require a website that hosts all the relevant information for cryptocurrencies such as  NFTs, their last seven days’ trend, etc. One such website is [CoinMarketCap](https://coinmarketcap.com/). Over a period of time,  say one month, all data should be scraped from this website and tabulated. Other information related to each cryptocurrency should be acquired from auxillary websites (text-based information related to each coin that can be mined and/or compared). Based on coin-specific financial performance data as well as text-related to each coin, can we determine which coins are most/least similar to one another? Can we cluster coins based on these pairwise rankings?

Analytical methods to consider:
 - TF-IDF for word frequency based on each coin.
 - Word Mover's Distance (WMD) to determine which coins most resemble each other based on systematically obtained text describing each coin.
 - Clustering algorithms could be used (on trading information and/or descirptive information) to group similar coins. Perhaps a "diversified cypto portfolio" could be identifed from these clusters.

---

## Project 2:  The Modal Patient - Identifying the Characteristics of the Most Common Patient in a Hospital

When treating a patient in a hospital/clinical setting, numerous patient characteristics are taken into account. When we think of the "typical patient", we would likely consider the _average_ of each one-dimensional characteristic of interest and erroneously combine these to for a multi-dimensional view of the "average patient". This combination of one-dimensional means is unlikely to actually describe an actual patient; we should instead be identifying the "modal patient". That is, the most common characteristics (the mode) of the multi-dimensional distributionn of the patient characteristics considered. This analysis could have important bearings on specific patient treatments, physician training, and possibly on identifying potential biases of machine learning models deployed in clinical settings (due to intrinsic class imbalance).

This project idea was inspired by the Planet Money podcast edisode on finding The Modal American. Should a group pursue this project, please listen to the podcast to familiarize yourselves with the general concept and methodology: [The Modal American](https://www.npr.org/2019/08/28/755191639/episode-936-the-modal-american).

Recommended for:
 - Students interested in analyzing an existing (and real-world) clinical dataset
 - Students who prefer manipulating an existing dataset (PostgreSQL expertise required) and with an established code community
 - Students who will respect a strict "no data leakage" policy for this project (given that it deals with sensitive clinical data)

The [MIMIC-IV dataset](https://physionet.org/content/mimiciv/0.4/) is a recently released update of the MIMIC-III dataset of patient admission and care at the Beth Deconess 

Important links:
 - [The MIMIC Website](https://mimic.mit.edu/)
 - [The MIMIC Codebase](https://github.com/MIT-LCP/mimic-code/)

---

## Project 3: The Modal Canadian - Identifying the Socio-Demographic Characteristic of the Most Common Canadian

Understanding how the socio-demographic landscape of a country varies across time (over the years) and space (within specific regions/provinces/territories) is important to sociological research and to informing governmental policy.  When we think of identifying the "typical/average Canadian/household" we would likely aggregate the results of a number of one-dimensional averages and erroneously assume that the resulting aggregate likely represnents common Canadians/households. This combination of one-dimensional means is unlikely to actually describe an actual person/household; we should instead be identifying the "Modal Canadian". That is, the most common characteristics (the mode) of the multi-dimensional distributionn of the population characteristics considered. This analysis could have important bearings on studying how the frequency of certain demographics vary over time (by year) and space (by region). Implementation of this analysis in such a way that it could be reproduced for each release of the Canadian census promises to be a useful and unique demonstration of how Canadian demographics are shifting.

This project idea was inspired by the Planet Money podcast edisode on finding The Modal American. Should a group pursue this project, please listen to the podcast to familiarize yourselves with the general concept and methodology: [The Modal American](https://www.npr.org/2019/08/28/755191639/episode-936-the-modal-american).

Recommended for:
 - Students interested in analyzing Statistic Canada Census data
 - Students who prefer manipulating existing datasets and developing their own codebase

The 5-year Canadian Census data  provide statistical information about the population, age, sex at birth and gender, type of dwelling, families, households and marital status, Canadian military experience, income, language, Indigenous peoples, housing, immigration, place of birth and citizenship, ethnocultural and religious diversity, mobility and migration, education, labour, and commuting as measured in the Census Program. 

The Census data products are availabel every five years since 1996 and the latest 2021 Census data are scheduled to be released Feb. 9th 2022.

The Modal Canadian analysis requires parsing the census data to form "meta-categories" (e.g. separating age into generations, education-level into "earned bachelors" or not, income-level into fewer brackets) to redistribute each individual into these new catagories. These recategorized data are then binned using permutations to arrive at a multi-dimentional distribution from which we can determine the characteristics of the Modal Canadian.

The codebase for this project should developed in such a way that meta-catagories could easily be added, removed, or the boundaries modified. 

The analysis should be completed over both the dimension of time (repeated for each version of the census) as well as over the dimension of space (repeated for each province/territory). 

---

## Project 4: Analyses of Campus-Base IoT Sensor Data Streams

TODO

---

## Undefined Project Ideas

Students are welcome to consider these topic ideas and fully research them for project feasability before commiting to one of these ideas:
 - *Project "Political Climate"*: Scrape the data-rich [Climate Action Tracker](https://climateactiontracker.org) website for country-specific emmision/climate policy data and correlate with governmental  political leaning.
 - TODO

---

## Links to Resources on Useful Topics (and Unique Analysis Methods)

1. [Distance Measures between Vectors](https://towardsdatascience.com/distance-functions-in-machine-learning-a-primer-in-simple-language-with-few-action-points-f5e328759b24)
2. [Word Mover's Distance](https://medium.com/@nihitextra/word-movers-distance-for-text-similarity-7492aeca71b0)
