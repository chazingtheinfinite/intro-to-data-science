# Project Ideas to Select from or to Inspire your Own

Course Co-Developer: Kevin Dick ([kevin.dick@carleton.ca](mailto:kevin.dick@carleton.ca))

*NOTE: This document will evolve during the course and students are advised to revisit it regularly for any useful changes.*

---

## Course Project Overview

Data Science is a field where practitioners tend to have "T-shaped knowledge"; all Data Scientists share a general foundation of statistics, probability, programming, and data manipulation skills and each Data Scientists then develops expertise in one or multiple specific domains. A Data Scientist specialized in text-processing and Natural Language Processing has a skillset and analytical pipeline that would be altogether different from a Data Scientist that creates Recommendation Systems for e-commerce products or a Data Scientist that works on image processing for Computer Vision applications.

That said, the technical material taught in the course functions to provide the Data Science foundations required to take on a Data Science project, however each of the projects you will work on within the course will _require autodidacticism on the behalf of all students and groups_. That said, the project topics listed below cover a broad range of topics, domains, and each require a specialized set of skills that you and your team will need to develop independently as you work through the project.

Your Intro. to Data Science course project must include *online data scraping to generate a new dataset* and/or *analyze the dataset in unique ways to produce new knoweldge*. Typically a scraping-based project will naturally include both of these criteria. We recommend that groups extensively research their proposed scraping target prior to committing to a given project topic. For groups that prefer to avoid a scraping component as part of their projects, please consider one of the topics listed below (and in each subdirectory here) for details on the proposed analysis method. If student groups are interested in defining their own project based on an existing dataset, it is imperative that you communicate with course developer (Kevin Dick; mailto:kevin.dick@carleton.ca) about your proposed project. 

When searching online for potential scraping-based data science projects, a number of recurrent themes are listed including: 
 - Financial Stock Value Scraping and Analysis
 - Social Media Scraping and NLP Analysis
 - eCommerce Product Price/Review Scraping and Comparison

While these types of projects are common, it is important that your project answers a number of new questions and does not repleat previous work. Listed below are a number of potential projects you and your group may select from for your course project. Certain projects already have existing datasets and therefore do not require a scraping component, however they each present an unique analysis that hadn't already been carried out on these data. These may also help inspire your own project ideas. The following projects are typically organized such that only one group may complete the project and therefore they may be claimed on a first-come-first-served basis. As metioned, please be sure to fully research your selected project idea (as part of Project Phase 1) and  before choosing to settle on it.

Finally, all projects are required to be organized using the [Cookiecutter Data Science Project Structure](https://drivendata.github.io/cookiecutter-data-science/#cookiecutter-data-science). Please read all of the documentation and related links to ensure that your project follows the standards of typical Data Science projects.

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

The [MIMIC-IV dataset](https://physionet.org/content/mimiciv/0.4/) is a recently released update of the MIMIC-III dataset of patient admission and care at the Beth Israel Deaconess Medical Center in Boston Massachusetts. The Dataset contains a wealth of information about patients, hospital admissions, prescribed medications, lab test results, and unstructured clinical notes. The data are organized into several SQL tables and can be queried and combined to generate various insights. The data are available only to pre-authorized researchers (Course Developer, Kevin Dick, has access) and strictly requires that data cannot be leaked or republished. Students who choose to pursue this project will be asked to sign forms to affirm proper use of these data during the course project.

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

## Project 4: Hate Speech Detection

### Project 4a: Creating a Hate Speech Detection Model using Twitter Data 

The detection of hate speech online is critical in the fight against prejudice and the targetting of minority groups in the information age. The TweetEval dataset could be used to train a hate-detection model and improve upon the performance of the [MetaHate model](https://ieeexplore.ieee.org/abstract/document/9672023).

### Project 4b: Mapping the Twittersphere Hate Language Landscape

**TW: This project will contain stong, offensive language and may be triggering to certain individuals.**

Using a hate detection model, the Twitter API can be used to detect hate speech and then for positive detections, vectorize the tweet using Word2Vec and all hate-tweets can be clustered and visualized/analyzed.

This work is expected to be applied to tweets published over the course of the semester (at least a month's worth of sampled tweets). These tweets could be localized to Canada-only for a Canadian hate landscape analysis.
The findings of this work can be compared to a similar study on an [Italian Twitter Hate Map](https://www.tandfonline.com/doi/full/10.1080/0144929X.2019.1607903). 

### Project 4c: Mapping the Twittershpere Incel Hate Speech Landscape

**TW: Incel-related language: this project will contain stong, offensive language and may be triggering to certain individuals.**

This project is a specific variant of the 4b project; essentially both could be completed in a single semester course-long project.

Using an existing Incel speech detector (see this [paper](https://dl.acm.org/doi/pdf/10.1145/3400806.3400808) as a reference), the Twitter API can be leveraged to source current posts and identify those that are etected as incel hate speech. This would enable the mapping of twitter-based incel hate speech for further analysis.

Recommended for:
 - Students interested in NLP machine learning model generation/application
 - Students interested in acquiring and analyzing Twitter data (millions of tweets)
 - Students interested in Social Good projects and the betterment of humanity

---

## Project 5: Analyses of Campus-Base IoT Sensor Data Streams

More details of this project are forthecoming.

Recommended for:
 - Students interested in time-series analyses and GIS-based applications
 - Students interested in working with sensor data streams

Research Questions:
 - Can we detect classroom occupancy from in-class CO2 detectors? (ground-truth obtained from campus in-person attendance)
 - Can we quantify the _number_ of individuals from in-class CO2 detectors? (ground-truth obtained from campus in-person attendance)
 - Can we determine the _biological gender composition_ from in-class CO2 detectors? (ground-truth obtained from campus in-person attendance)
 - Using a network of campus CO2 detectors, can we detect climate change? That is, can we detect a notable "drifting rise" in CO2 levels at a hyper-regional level through networked sensors to collectively denoise individual measurements? One opportunity would be to corroborate findings with a similar city-wide study in Munich using an alternative CO2 measurement method: [Article](https://www.tum.de/en/about-tum/news/press-releases/details/36482/); [Website](https://atmosphere.ei.tum.de/); [Data](https://retrieval.esm.ei.tum.de/); [Publication](https://amt.copernicus.org/articles/14/1111/2021/).


---

### Project 5: Statistics Canada Collaboration Projects 

#### Project 5a: Geospatial layer on active transportation (AT)

*Goal:* The goal is to prepare a geospatial dataset of active transportation (AT) network to be used in subsequent socio-economic analysis projects. Tasks will include building an inventory of available open datasets on AT, integration of the identified datasets and (or) a descriptive analysis of the datasets.

*Background*: The Public Health Agency of Canada (2014a) defines active transportation (AT) as “using your own power to get from one place to another” via “walking, biking, skateboarding, in-line skating/rollerblading, jogging and running, non-mechanized wheel chairing, snowshoeing and cross-country skiing”. [Public Health Agency of Canada (PHAC) (2014a). Active transportation.](https://www.canada.ca/en/public-health/services/being-active/active-transportation.html).

AT together with public transit constitute sustainable transportation for having minimal environmental impact. [Statistics Canada (2017). Commuters using sustainable transportation in census metropolitan areas. Census in Brief. November29, 2017. Catalogue no. 98-200-X2016029.](https://www12.statcan.gc.ca/census-recensement/2016/as-sa/98-200-x/2016029/98-200-x2016029-eng.cfm).

Infrastructure Canada defines AT infrastructure as “physical structures and the built environment that support active transportation, such as pathways, bike lanes, multi-use trails and widened sidewalks”, and considering that public transit is integral to any AT network, it is essentially  “a complete network that allows users to safely move through their communities and between destinations, from main streets to schools, parks, public transit hubs and residential neighbourhoods”.
[Infrastructure Canada (2021). Canada's First National Active Transportation Strategy.](https://www.infrastructure.gc.ca/trans/active-actif-eng.html)

*Data:* Authoritative (official) data on AT infrastructure (Walking and Biking) is available for many municipalities in Canada through open data portals. However, the scope, richness and structure of these data vary significantly between geographical units.

#### Project 5b: Sustainable development goal indicators for public transit

*Goal:* The goal is to prepare an inventory of available public transit data across municipality, to determine a process to compute indicator 11.2.1 of the [United Nations Sustainable Development Goals: Proportion of population that has convenient access to public transport, by sex, age and persons with disabilities](https://sdg.data.gov/11-2-1/) and (or) indicator 11.4.1 of the [Canadian Indicator Framework Sustainable Development Goals: Percentage of the population living within 500 meters of a public transport stop](https://sdgcif-data-canada-oddcic-donnee.github.io/11-4-1/).

*Background:* On June 22, 2021, Statistics Canada has launched the [Canadian Indicator Framework (CIF)](https://sdgcif-data-canada-oddcic-donnee.github.io/) for the Sustainable Development Goals (SDGs), a foundational component for Canada to track and report on progress on its priorities for achieving the 2030 Agenda for Sustainable Development. The agenda, adopted by all United Nations member states in 2015, is a 15-year global framework centred on the set of 17 SDGs.

Under the CIF, there is an indicator, CIF 11.4.1: “Percentage of the population living within 500 meters of a public transport stop”. The indicator is reflective of the UN Sustainable Development Goal 11, Indicator 11.2.1: “Proportion of population that has convenient access to public transport, by sex, age and persons with disabilities”. The UN defines “convenient access” as living/working/studying within a service area of 500 m, using the street network distance, from the nearest public transit stop.

*Data:* The data on public transit routes are commonly reported by public transit agencies in the General Transit Feed Specification (GTFS). GTFS data is made available by many municipalities as open data. They include routes and stops for public transit modes of transportation.

Depending on availability, other elements of public transit infrastructure could be considered: railroad stations, light rail lines, terminal ‘park-and-ride’ facilities and others.

#### Project 5c: Rural access index (RAI)

*Goal:* The goal is to calculate RAI for all of Canada at a high granularity level, for dissemination blocks (~500,000 polygons in Canada) and dissemination areas (~50,000 polygons in Canada), using the standard and then improved upon United Nations Methodology.

*Background:* Statistics Canada tracks and reports on progress towards achieving the United Nations 2030 Agenda for Sustainable Development. The agenda, adopted in 2015 by all United Nations member states, is a 15-year global framework centred on the [set of 17 sustainable development goals](https://www144.statcan.gc.ca/sdg-odd/index-eng.htm). 

RAI is defined through Indicator 9.1.1 of the [United Nations Sustainable Development Goals](https://sdg.data.gov/9-1-1/): Proportion of the rural population who live within 2 km of an all-season road.

A high level world map of RAI is available here: [https://rai.azavea.com/](ttps://rai.azavea.com/)

*Data:* Statistics Canada [Geographic Attribute File](https://open.canada.ca/data/en/dataset/32f1a777-9fcf-4e4a-8c66-82c66a2e76f1), [Census Boundary file](https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-2016-eng.cfm) for dissemination blocks (DBs), and the [National Road Network](https://open.canada.ca/data/en/dataset/3d282116-e556-400c-9306-ca1a3cada77f) data.

---

### Project 6: Scraping GoFundMe to Detect Forein Interference

Can we scrape the GoFundMe active fundraisers to ask a number of questions about the types of fundraisers ongoing during the pandemic? 

Can we scrape the history of donations for a given fundraiser to query where donations are coming from? 

For large-scale fundraisers (say >1M$), does the history of donations for certain fundraisers contain a significantly larger proportion of "Anonymous" donations (perhaps indicative of significant influence from foreign actors?) 

See [Tutorial 2](https://youtu.be/fZG4bWT8CSo) for an implementation of a fundraiser donation history scraper.

Individual GoFundMe pages can be scraped by adapting this [GitHub GoFundMe Page Scraper](https://github.com/lmeninato/GoFundMe). The [GoFundMe Wiki Page](https://en.wikipedia.org/wiki/GoFundMe) lists a number of the biggest fundraisser projects, many with 'Active' status that may serve the basis of this project. This is a [CBC News article with some preliminary findings on the Freedom Convoy 2022 Fundraiser](https://www.cbc.ca/news/politics/vaccine-protest-convoy-gofundme-donations-1.6330594#:~:text=GoFundMe%20only%20makes%20public%20a,as%20new%20donations%20come%20in.) and a potential contact at CBC news that may be willing to share the ~35K donations they have already scraped every half hour since the morning of Monday January 24th, 2022.

---

## Undefined Project Ideas

Students are welcome to consider these topic ideas and fully research them for project feasability before commiting to one of these ideas:
 - *Project "Political Climate"*: Scrape the data-rich [Climate Action Tracker](https://climateactiontracker.org) website for country-specific emmision/climate policy data and correlate with governmental  political leaning.
 - *Project Network Malware Detection*: The [Stratosphere Lab](https://www.stratosphereips.org/) has several [published datasets of malware attacks on IoT network traffic](https://www.stratosphereips.org/datasets-overview) for research applications. For research-oriented students, this could be an excellent project foundation for a subsequent Master's thesis on malware traffic captures; see this series of [previous Master's projects](https://www.stratosphereips.org/thesis-projects) using these data. For example, a course project might attempt to improve the [Random Forest-based Malware Detection Method from this thesis](https://dspace.cvut.cz/bitstream/handle/10467/69244/F3-BP-2017-Smolik-Daniel-Graph-Based-Analysis-of-Malware-Network-Behaviors.pdf) by using Graph Neural Networks (or another deep learning architecture); see [this GitHub repo](https://github.com/dansmoliik/Malware-graph-detection) to get started.
 - *Project COVID Policies & Perceptions*:  Track how regional policies around COVID have changed over the years and how people affected by these policy implementations react to the changes. This will require scraping social media and news websites and students will need to independently learn some basic NLP analytical techniques. 
 - *Project Alzheimer's Impacts*: Relationship between Alzheimer's cases, mental stress rates, unemployment, and demographics in different countries. This project would require scraping numerous resources and aggregating several datasets (could be very hard).
 - *Project Amazon Price Reaction*: Can we measure/quantify how much specific Amazon product prices deviate in relation to global events? This work would require scraping product price information before and after specific (and likely/necessarily related) events to quantify the deviation of prices as a reaction to external events (and ideally independently of other confounding factors). In lieu of price variation, sentiment analysis on certain product reviews could be useful too as in the example of [Negative Candle Reviews related to COVID loss of smell symptoms](https://www.washingtonpost.com/business/2020/12/01/covid-scented-candle-reviews/). Certain website have tracked historical data such as CamelCamelCamel (no API or data download, would need to extract from chart images [HARD]) and Keepa (has an API, but requires paid subscription and trial version is very limited).
 - *Project Scraping GoFundMe*: Can we scrape the GoFundMe active fundraisers to ask a number of questions about the types of fundraisers ongoing during the pandemic? Can we scrape the history of donations for a given fundraiser to query where donations are coming from? For large-scale fundraisers (say >1M$), does the history of donations for certain fundraisers contain a significantly larger proportion of "Anonymous" donations (perhaps indicative of significant influence from foreign actors?) Individual GoFundMe pages can be scraped by adapting this [GitHub GoFundMe Page Scraper](https://github.com/lmeninato/GoFundMe). The [GoFundMe Wiki Page](https://en.wikipedia.org/wiki/GoFundMe) lists a number of the biggest fundraisser projects, many with 'Active' status that may serve the basis of this project. This is a [CBC News article with some preliminary findings on the Freedom Convoy 2022 Fundraiser](https://www.cbc.ca/news/politics/vaccine-protest-convoy-gofundme-donations-1.6330594#:~:text=GoFundMe%20only%20makes%20public%20a,as%20new%20donations%20come%20in.) and a potential contact at CBC news that may be willing to share the ~35K donations they have already scraped every half hour since the morning of Monday January 24th, 2022. 

---

## Links to Resources on Useful Topics (and Unique Analysis Methods)

1. [Distance Measures between Vectors](https://towardsdatascience.com/distance-functions-in-machine-learning-a-primer-in-simple-language-with-few-action-points-f5e328759b24)
2. [Word Mover's Distance](https://medium.com/@nihitextra/word-movers-distance-for-text-similarity-7492aeca71b0)
