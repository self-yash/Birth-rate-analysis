This is a project about Birth rate analysis on which we will be predicting the births in future years of Males and Females but firstly we are aiming to perform PCA and SVD on the dataset used for the project

Steps for Performing PCA and SVD:

Preprocessing Data-
1. Standardize the dataset 'births.csv' to make the mean equal to 0 and standard deviation 1 (approx) so that our dataset comes into a sequence
2. Now that our dataset is standardized with 'standardized_births.csv'.Now, we need to get rid of the missing values.
3. For getting rid of missing values we have two options 1. Delete the missing value rows 2. replace the missing values rows with mean,median etc
4. and obviously i have chosen the easier one so I'll go with the first option and deleting the rows with missing values
5. Fortunately in our dataset around 400 rows are there with missing values. Since our dataset is huge containing 15K rows removing 400 rows doesn't cause much loss of information and hence giving rise to 'standardized_births without missing values.csv'. (I just manually deleted them >.< )

Performing SVD and PCA-
6. SVD and PCA can only be performed on numerical values so we will be completely ignoring the categorical columns 'gender' for this project which comes with the cost of losing information.
7. Now just perform PCA and SVD with codes 'svd code.py' and 'pca code.py' 
