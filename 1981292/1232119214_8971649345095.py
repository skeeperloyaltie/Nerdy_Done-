import pandas as pd
import numpy as np
import math

# This function should prepare the data by reading it from a file and converting it into a useful format for training and testing
# and implement 90-10 splitting as specified in the project description.
def preprocess(filename):
    
    # Reading csv file
    data = pd.read_csv(filename)
    
    # Splitting the data into 90-10 and returning the train and test data. 
    index = int(len(data) * 0.9)
    train = data.iloc[:index]
    test = data.iloc[index:]
    return train, test

# This function should calculate prior probabilities and likelihoods (conditional probabilities) from the training data and using
# to build a naive Bayes model

def train(instance, train_data, label, model, replace_missingValues):
    
    # Calculating prior probabilities
    conditional_prob = 1
    data = train_data.loc[train_data["label"] == label]
    total_instances = len(train_data)
    label_count = len(data)
    prior = label_count / total_instances
    
    # Replacing missing values by Laplace Smoothing to calculate conditional probabilities
    for col in ["work class", "education", "marital status", "occupation", "relationship", "race", "sex", "native country (region)"]:
        x = len(data.loc[data[col] == instance[col]])
        d = len(set(data[col]))
        if (instance[col]):
            if (replace_missingValues):
                conditional_prob *= (x + 1) / (d + label_count)
            else:
                conditional_prob *= x / label_count    
                
    # Calculating conditional probabilities
    if (model == "gausian"):
        conditional_prob *= gausian_model(instance, train_data, label)
    else:
        conditional_prob *= kde_model(instance, train_data, label)
        
    return prior * conditional_prob

# This function calculates and returns probability density function of a data with Gaussian model
def gausian_model(instance, train_data, label):
    prob = 1
    data = train_data.loc[train_data["label"] == label]
    
    # Calculating mean and standard deviation to find the probability of observing an instance. 
    for col in ["age", "education num", "hours per week"]:
        mean = np.nanmean(data[col])
        std = np.nanstd(data[col])
        prob *= (1 / std * np.sqrt(2 * math.pi)) * math.exp(-0.5 * ((instance[col] - mean) / std) ** 2)
        
    return prob

# This function should predict classes for new items in the testing data
def predict(train_data, test, model, replace_missingValues):
    
    # Assigning the labels to "positive" and "negative"
    for index, row in test.iterrows():
        positive = train(row, train_data, " <=50K", model, replace_missingValues)
        negative = train(row, train_data, " >50K", model, replace_missingValues)
        
    # Predicting labels
        if (positive > negative):
            test.loc[index,"Predicted_Label"] = " <=50K"
        else:
            test.loc[index,"Predicted_Label"] = " >50K"
    return

# This function should evaliate the prediction performance by comparing your model’s class outputs to ground
# truth labels, return and output accuracy, confusion matrix and F1 score.

def evaluate(test):
    
    # Finds the no of true positive, true negative, false positive and false negative predicted labels. 
    TP = len(test[(test['label'] == " <=50K") & (test['Predicted_Label'] == " <=50K")])
    TN = len(test[(test['label'] == " >50K") & (test['Predicted_Label'] == " >50K")])
    FP = len(test[(test['label'] == " >50K") & (test['Predicted_Label'] == " <=50K")])
    FN = len(test[(test['label'] == " <=50K") & (test['Predicted_Label'] == " >50K")])
    
    # Calculating accuracy of the predicted label. 
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    
    # Creating the confusion matrix
    confusion_matrix = pd.DataFrame([[TP, FN], [FP, TN]], columns=['Positive', 'Negative'], index = ['Positive', 'Negative'])
    F1 = TP / (TP + 0.5 * (FP + FN))
    
    return accuracy, confusion_matrix, F1

# This cell should act as your "main" function where you call the above functions 
# on the full ADULT data set, and print the evaluation results. [0.33 marks]

# First, read in the data and apply your NB model to the ADULT data
train_data, test = preprocess("dataset/adult.csv")
predict(train_data, test, "gausian", False)

# Second, print the full evaluation results from the evaluate() function
accuracy, confusion_matrix, F1 = evaluate(test)
print("Accuracy: ", accuracy)
print("\nConfusion Matrix:\n\n", confusion_matrix)
print("\nF1 score: ", F1)

# Third, print data statistics and model predictions, as instructed below 
# N is the total number of instances, F the total number of attributes, L the total number of labels
# The "class probabilities" may be unnormalized
# The "predicted class ID" must be in range (0, L)

print("\nAttribute vectors of instances [0, 1, 2]: \n", list(train_data.iloc[0, : -1]), list(train_data.iloc[1, : -1]), list(train_data.iloc[2, : -1])) # of the first three records in adult.csv

print("\nNumber of instances (N): ", len(train_data))
print("Number of attributes (F): ", len(train_data.iloc[0]) - 1)
print("Number of labels (L): ", len(set(train_data["label"])))


# print out the prediction results of the last three instances
print("\n\nPredicted class log-probabilities for instance N-3: ", [("<=50K", math.log(train(test.iloc[-3,], train_data, " <=50K", "gausian", False))), (">50K", math.log(train(test.iloc[-3,], train_data, " >50K", "gausian", False)))])
print("Predicted class ID for instance N-3: ", test.iloc[-3,-1])
print("\nPredicted class log-probabilities for instance N-2: ", [("<=50K", math.log(train(test.iloc[-2,], train_data, " <=50K", "gausian", False))), (">50K", math.log(train(test.iloc[-2,], train_data, " >50K", "gausian", False)))])
print("Predicted class ID for instance N-2: ", test.iloc[-2,-1])
print("\nPredicted class log-probabilities for instance N-1: ", [("<=50K", math.log(train(test.iloc[-1,], train_data, " <=50K", "gausian", False))), (">50K", math.log(train(test.iloc[-1,], train_data, " >50K", "gausian", False)))])
print("Predicted class ID for instance N-1: ", test.iloc[-2,-1])


### Q2 [4 marks]
# You can adopt different methods for training and/or testing, which will produce different results in model evaluation. 

# (a) Instead of Gaussian, implement KDE for  P(Xi|cj) for numeric attributes Xi. Compare the evaluation results with Gaussian. Which one do you think is more suitable to model P(Xi|cj), Gaussian or KDE? Observe all numeric attributes and justify your answer.

# You can choose an arbitrary value for kernel bandwidth $\sigma$ for KDE, but a value between 3 and 15 is recommended. You should write code to implement KDE, not call an existing function/method such as `KernelDensity` from `scikit-learn`.

# (b) Implement <10-fold and 2-fold cross-validations</u>.  
#	Observe the evaluation results in each fold and the average accuracy, recall and specificity over all folds. 
#	Comment on what is the effect by changing the values of m in m-fold cross validation. (You can choose either Gaussian or KDE Naive Bayes.)

# This function implements KDE model for P(Xi|cj) for numeric attributes Xi and returns the probability. 
def kde_model(instance, train_data, label):
    prob = 1
    data = train_data.loc[train_data["label"] == label]
    N = len(data)
    std = 3
    for col in ["age", "education num", "hours per week"]:
        prob *= (1 / N) * sum((1 / std * np.sqrt(2 * math.pi)) * np.exp(-0.5 * ((instance[col] - data[col]) / std) ** 2))
    return prob

# Predicts the train and test data after implementing KDE 
predict(train_data, test, "kde", False)
accuracy = evaluate(test)[0]
print("Accuracy after KDE implementation: ", accuracy)

import warnings
warnings.filterwarnings("ignore")

# This function takes in the dataset and a value m and implements m fold cross validation on the dataset
def cross_validation(dataset, m):
    size = int(len(dataset) / m)
    accuracy_sum = 0
    recall_sum = 0
    specificity = 0
    
    #Calculating and returning average accuracy, recall an specificity. 
    for i in range(m):
        train_data = dataset.loc[(dataset.index < i * size) | (dataset.index >= size * (i + 1))]
        test = dataset.iloc[i * size : size * (i + 1)]
        predict(train_data, test, "gausian", False)
        accuracy, confusion_matrix, F1 = evaluate(test)
        accuracy_sum += accuracy
        recall_sum += confusion_matrix.loc["Positive","Positive"] / (confusion_matrix.loc["Positive","Positive"] + confusion_matrix.loc["Positive","Negative"])
        specificity += confusion_matrix.loc["Negative","Negative"] / (confusion_matrix.loc["Negative","Negative"] + confusion_matrix.loc["Negative","Positive"])
        
    return accuracy_sum / m, recall_sum / m, specificity / m

dataset = pd.read_csv("dataset/adult.csv")
l = []
for m in range(2, 11):
    l.append(cross_validation(dataset, m))
d = pd.DataFrame(l, columns = ["Average Accuracy", "Average Recall", "Average specificity"], index = range(2, 11))
d

# In week 4, we have learned how to obtain information gain (IG) and gain ratio (GR) to choose an attribute to split a node in a decision tree. We will see how to apply them in the Naive Bayes classification.

# (a) Compute the GR of each attribute Xi, relative to the class distribution. In the Naive Bayes classifier, remove attributes in the ascending order of GR: first, remove P(Xi|cj) such that Xi has the least GR; second, remove P(Xi'|cj) such that Xi' has the second least GR,......, until there is only one Xi* with the largest GR remaining in the maximand P(cj) P(Xi*} | cj). Observe the change of the accuracy for both Gaussian and KDE (Choose bandwidth sigma=10 for KDE).

# (b) Compute the IG between each pair of attributes. Describe and explain your observations. Choose an attribute and implement an estimator to predict the value of `education num`. Explain why you choose this attribute. Enumerate two other examples that an attribute can be used to estimate the other and explain the reason.  