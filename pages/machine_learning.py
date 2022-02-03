'''
Description: 
Author: lunyang
Github: 
Date: 2022-02-02 16:00:26
LastEditors: lunyang
LastEditTime: 2022-02-02 17:34:55
'''
import streamlit as st 
import numpy as np 
from io import BytesIO

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score


def get_dataset(name):
    data = None
    if name == 'Iris':
        data = datasets.load_iris()
    elif name == 'Wine':
        data = datasets.load_wine()
    else:
        data = datasets.load_breast_cancer()
    X = data.data
    y = data.target
    return X, y


def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == 'SVM':
        C = st.sidebar.slider('C', 0.01, 10.0)
        params['C'] = C
    elif clf_name == 'KNN':
        K = st.sidebar.slider('K', 1, 15)
        params['K'] = K
    else:
        max_depth = st.sidebar.slider('max_depth', 2, 15)
        params['max_depth'] = max_depth
        n_estimators = st.sidebar.slider('n_estimators', 1, 100)
        params['n_estimators'] = n_estimators
    return params


def get_classifier(clf_name, params):
    clf = None
    if clf_name == 'SVM':
        clf = SVC(C=params['C'])
    elif clf_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['K'])
    else:
        clf = clf = RandomForestClassifier(n_estimators=params['n_estimators'], 
            max_depth=params['max_depth'], random_state=1234)
    return clf



def app():
    st.write("""
            # Classification
            """)

    dataset_name = st.sidebar.selectbox(
        'Select Dataset',
        ('Iris', 'Breast Cancer', 'Wine')
    )

    st.write(f"## {dataset_name} Dataset")

    classifier_name = st.sidebar.selectbox(
        'Select classifier',
        ('KNN', 'SVM', 'Random Forest')
    )

    # Get dataset
    X, y = get_dataset(dataset_name)
    st.write('Shape of dataset:', X.shape)
    st.write('number of classes:', len(np.unique(y)))

    # Hyper parameters
    params = add_parameter_ui(classifier_name)

    # Model
    clf = get_classifier(classifier_name, params)
    
    # Train model and plot results

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    st.write(f'Classifier = {classifier_name}')
    st.write(f'Accuracy =', acc)

    #### PLOT DATASET ####
    # Project the data onto the 2 primary principal components
    pca = PCA(2)
    X_projected = pca.fit_transform(X)

    x1 = X_projected[:, 0]
    x2 = X_projected[:, 1]

    fig, ax = plt.subplots(figsize=(8,6))
    ax.scatter(x1, x2,
            c=y, alpha=0.8,
            cmap='viridis')
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')

    # Resize image
    buf = BytesIO()
    fig.savefig(buf, format="png")
    st.image(buf)
