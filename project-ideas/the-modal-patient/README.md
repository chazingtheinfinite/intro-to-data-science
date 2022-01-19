# The Modal Patient

Inspired from a Planet Money podcast "The Modal American", identifying the "Modal Person" in a given dataset based on multiple characteristics is a conceptually simple, yet non-trivial task. Moreover, in various contexts, such as identifying the "Modal Patient" in a clinical context can have very important bearing on both clinician training and clinic-based machine learning models that may be sensitive to class-imbalance.
  
Looking for the average hospital patiuent profile is akin to putting a number of patients with different demographics, characteristics, and  qualities into a blender and hoping that an existing human comes out. But there is a different way to find the most "typical" patient: the mode.

The mode is the most common element in a dataset. It's not the average/mean and so when we wish to look for the "average patient" we really mean the most common/typical patient, aka the "modal Patient". That's a statistic that, to the best of our knowledge, hasn't been reported upon before of the recently released MIMIC-IV dataset and its consideration for both clinical training (treatment recommendations made on the mode rather than the mean) and machine learning applications (where class imbalance may bias a model.

This project will leverage the largest publicly available real-world clinical dataset and aim to extract relevant patient information, define reasonable/informed boundaries, and provide a framework/codebase for which other clinical researchers could replicate, modify, and extend this analysis. 

## The MIMIC-IV Dataset



## Project Steps:

1. Obtain the MIMIC-IV dataset from Kevin Dick (Course Developer)
2. Setup the Database and programming environment ([MIMIC-IV Instructions Here](https://github.com/MIT-LCP/mimic-code/tree/main/mimic-iv/buildmimic))
3. Extract relevant information about each patient in a CSV format
4. Determine subset of characteristics to focus study upon (these could be organized under certain types of catagories). Does it make sens to include medications (they are both common and rare)?
5. Generate final refined dataset of relevant information
6. Produce codebase analyzing the modal patient and assigning a "modal rank" to each type of individual (long-tailed distribution in rank-order). Perform similar experiments for other subsets of characteristics. The codebase should be organized in such a way that any subset of variables can be selected and a series of analyses/visualizations performed.
7. Generate a pairwise "distance measure" between each modal rank using a one-hot encoding of categorical features and the multi-dimensional cosine distance
8. Explore the rank-based modalities and the pairwise distances between each modal patient
9. Write up results based on these explorations. What is interesting about this modal patient? Is it what we might have expected?

#### Suggested Visualizations:
 - A Decision-Tree-like breakdown of the selected boundaries. Only one branch of the tree needs to be visualized since all cascaded decisions for a given leaf are the same for the sister leaf. This should be auto generated based on the chosen bounds for a given analysis.
 - A [Sunburst Chart](https://plotly.com/python/sunburst-charts/) could also be used to interactively "zoom" into each level applying the chosen characteristics. This will provide a better intuition to how each characteristic contributes to the final Modal Patient.


Bonus work:
 - Robustness Analysis 1: Perform an "ablation study" where the elminiation of various characteristics changes the outcome of the ranking (measured by how much the rankings change from one to the next)
 - Robustness Analysis 2: Quantify the impact of varying the chosen bounds for each "meta-characteristic" by measuring how much the modal ranking deviates. Hopefully we can show that within reasonable tolerance, the rankings are consistent.
 - Time-Based Study: Vary the "modal patient" by reducing analysis to a single year (must consider that this limits the size of the sample under study; perhaps only years with a minimum sample number should be considered)
 - 


