# Analyzing-Unstructured-Data-Project

>Developed analytical solutions to improve Craigslist’s online platform using the techniques of text mining, classification, and NLP

## Data Analysis

>Our raw data came from proprietary scrappers that we developed for the inactive listings identifier, expired events identifier, misclassified ads, and the lean search system. The scrappers yielded CSV files that contain raw text, including symbols, numeric, and other characters.

### Identifying Old, Inactive Listings, and Expired Events

> For expired events listings and inactive listings identifier, we extracted the information listing’s title and posted date with predefined categories and region. The solution is based on a flagging algorithm where takes in a specified parameter in the form of date and creates flags based on that parameter. Since there is no modelling involved, there was negligible data pre-processing required. Based on a trial run, we came up with the following results for car deals listed in Philadelphia for 7-day filter criteria:

>

#### Expired Listings Scrapper 

![]1.jpg
