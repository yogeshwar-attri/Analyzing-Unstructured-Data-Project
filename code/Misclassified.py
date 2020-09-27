import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.metrics import roc_auc_score

data = pd.read_csv("D:\Purdue Courses\Fall Mod 2\MGMT 590 Analysing Unstructured Data\Project\AUD Misclassified.csv",encoding = "ISO-8859-1")

titles = data.Title
y = data.is_phone

tokenized_titles = []
for title in titles:
    title = title.lower()
    token_dl = nltk.word_tokenize(title)
    #punct_words_removed = [token for token in token_dl if token.isalpha()]
    stop_words_removed = [token for token in token_dl if not token in stopwords.words('english')]
    tokenized_titles.append(token_dl)

train_X = tokenized_titles[:700]
test_X = tokenized_titles[701:len(tokenized_titles)-1]

train_y = y[:700]
test_y = y[701:len(y)-1]

def tk(doc):
    return doc

vec = TfidfVectorizer(analyzer='word',tokenizer=tk, preprocessor=tk,token_pattern=None, min_df=8, ngram_range=(1,3),lowercase=True)
#vec = CountVectorizer(min_df=8,lowercase=True)

training_x = vec.fit_transform(train_X)

#training_x = vec.transform(train_X)
testing_x = vec.transform(test_X)


Logitmodel = LogisticRegression()

# training
Logitmodel.fit(training_x, train_y)
y_pred_logit = Logitmodel.predict(testing_x)

# evaluation
acc_logit = accuracy_score(test_y, y_pred_logit)
print("Logit model Accuracy:: {:.2f}%".format(acc_logit*100))


# training
NBmodel = MultinomialNB()
NBmodel.fit(training_x, train_y)
y_pred_NB = NBmodel.predict(testing_x)

# evaluation
acc_NB = accuracy_score(test_y, y_pred_NB)
print("Naive Bayes model Accuracy:: {:.2f}%".format(acc_NB*100))


SVMmodel = LinearSVC()
# training
SVMmodel.fit(training_x, train_y)
y_pred_SVM = SVMmodel.predict(testing_x)
# evaluation
acc_SVM = accuracy_score(test_y, y_pred_SVM)
print("SVM model Accuracy:{:.2f}%".format(acc_SVM*100))


train_y = y[:700]
test_y = y[701:len(y)-1]

from sklearn.metrics import roc_auc_score
roc_auc_score(test_y, y_pred_SVM)
roc_auc_score(test_y,y_pred_logit)
roc_auc_score(test_y,y_pred_NB)

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
DTmodel = DecisionTreeClassifier()
RFmodel = RandomForestClassifier(n_estimators=50, max_depth=3,bootstrap=True, random_state=0) ## number of trees and number of layers/depth
# training

DTmodel.fit(training_x, train_y)
y_pred_DT = DTmodel.predict(testing_x)
RFmodel.fit(training_x, train_y)
y_pred_RF = RFmodel.predict(testing_x)
# evaluation
acc_DT = accuracy_score(test_y, y_pred_DT)
print("Decision Tree Model Accuracy: {:.2f}%".format(acc_DT*100))
acc_RF = accuracy_score(test_y, y_pred_RF)
print("Random Forest Model Accuracy: {:.2f}%".format(acc_RF*100))

from sklearn.neural_network import MLPClassifier
DLmodel = MLPClassifier(solver='adam', hidden_layer_sizes=(4), activation = 'tanh', random_state=1)
# training
DLmodel.fit(training_x, train_y)
y_pred_DL= DLmodel.predict(testing_x)
# evaluation
acc_DL = accuracy_score(test_y, y_pred_DL)
print("DL model Accuracy: {:.2f}%".format(acc_DL*100))
