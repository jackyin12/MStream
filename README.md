# MStream

Here is the code of MStream and MStreamF.
The code is written by python3.6 with no dependence.

## Datasts

The datasets are in format of JSON like follows:

    {"tweetId": "006218", "clusterNo": 8, "textCleaned": "scottish independence alistair carmichael issue complacency warning"}
    {"tweetId": "000071", "clusterNo": 40, "textCleaned": "doggie scofflaw bagged dna testing"}
    {"tweetId": "000015", "clusterNo": 1, "textCleaned": "challenge china airspace"}
    {"tweetId": "008096", "clusterNo": 86, "textCleaned": "western michigan northern illinois key victory bronco"}


## Outputs

The outputs will be in the result folder and the result of each batch is saved separately in each folder.
You can check the clustering results of each folder which are in format like follows:

    006218 31
    000071 2
    000015 15
    008096 6

The former is ID of each document and the latter is predicted cluster of each document.

