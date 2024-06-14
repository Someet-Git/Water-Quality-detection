from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
import pandas as pd
import json

def index(request):
    if request.method == 'POST':
        do=float(request.POST['do'])
        Ph=float(request.POST['Ph'])

        X_test=[[do, Ph]]
        df = pd.read_csv('predict\water_fin.csv')

        target=[]
        for i in range (0,1251):
            if df.iloc[i,6]<20:
                target.append(1)
            elif df.iloc[i,6]<40:
                target.append(2)
            elif df.iloc[i,6]<60:
                target.append(3)
            elif df.iloc[i,6]<80:
                target.append(4)
            else:
                target.append(5)

        X = df.iloc[:,0:2].values
        target = np.array(target)
        target = target[...,None]
        Xf = np.c_[X, target]
        dataset = pd.DataFrame(data =Xf, columns = ['do', 'ph', 'target'])

        X = dataset.iloc[:,0:2].values
        y = dataset[['target']].values

        from sklearn.ensemble import RandomForestClassifier
        rf = RandomForestClassifier(max_depth=3, random_state=15)
        rf.fit(X, y.ravel())
        y_pred = rf.predict(X_test)

        if(y_pred==1):
            result=str(y_pred)+' Very Good Quality'
        elif(y_pred==2):
            result=str(y_pred)+' Good Quality'
        elif(y_pred==3):
            result=str(y_pred)+' Moderate Quality'
        elif(y_pred==4):
            result=str(y_pred)+'  Bad Quality'
        else:
            result=str(y_pred)+' Very Bad Quality'

        return render(request, "index.html", {'do':do, 'Ph':Ph, 'result':result})
    else:
        return render(request, "index.html")

def about(request):
    return render(request, "about.html")
