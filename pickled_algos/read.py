#!c:/Python/python3_6.exe -u

import pickle
import nltk

'''
pk = ["BernoulliNB_classifier5k.pickle",
"LinearSVC_classifier5k.pickle",
"LogisticRegression_classifier5k.pickle",
"MNB_classifier5k.pickle",
"SGDC_classifier5k.pickle",
"documents.pickle",
"naivebayes.pickle",
"originalnaivebayes5k.pickle",
"sentiment_mod.pickle",
"voted_classifier.pickle",
"voted_classifier5k.pickle",
"word_features5k.pickle",
"word_features_3000.pickle" ]
'''

pk = ["word_features5k.pickle",
"word_features_3000.pickle" ]


for file in pk:
    #op_file = "new/"+file
    with open(file, 'rb') as pickle_file:
        #content = pickle.load(pickle_file)
        print (file)
        with open("new/"+file,'wb') as op_file:
            pickle.dump(pickle.load(pickle_file), op_file, 2)
