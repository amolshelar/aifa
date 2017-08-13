from __future__ import print_function
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.


# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
import pandas as pd
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import csv
import math

def index(request): 
    return render(request, 'personal/main.html')

def Tab1(request): 
    return render(request, 'personal/Tab1.html')

def Tab2(request): 
    return render(request, 'personal/Tab2.html')

def register(request): 
    if request.method=='POST':
        global name,age,uid,nationality,marital,gender
        name=request.POST['name2']
        age=request.POST['age']
        uid=request.POST['uid']
        nationality=request.POST['nationality']
        marital=request.POST['marritalstatus']
        gender=request.POST['genderradio']
        print(name)
        print(age)
        print(uid)
        print(nationality)
        print(marital)
        print(gender)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def register1(request): 
    if request.method=='POST':
	global occupation,jobtype,income,expenditure,currentsavings,dependent,pension,surplus
        occupation=request.POST['occupation']
	jobtype=request.POST['jobtype']
  	income=float(request.POST['income'])
	expenditure=float(request.POST['expenditure'])
	surplus=income-expenditure
	currentsavings=float(request.POST['currentsavings'])
	dependent=request.POST['dependentperson']
	pension=request.POST['pension']
        print(occupation)
        print(jobtype)
	print(income)
	print(expenditure)
        print(currentsavings)
	print(dependent)
	print(pension)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def register2(request): 
    if request.method=='POST':
	global name,age,uid,nationality,marital,gender
        name=request.POST['name2']
        age=request.POST['age']
        uid=request.POST['uid']
        nationality=request.POST['nationality']
        marital=request.POST['marritalstatus']
	gender=request.POST['genderradio']
        print(name)
        print(age)
        print(uid)
        print(nationality)
        print(marital)
        print(gender)
	global occupation,jobtype,income,expenditure,currentsavings,dependent,pension,surplus,goalname,shortfall
        occupation=request.POST['occupation']
	jobtype=request.POST['jobtype']
  	income=float(request.POST['income'])
	expenditure=float(request.POST['expenditure'])
	surplus=income-expenditure
	currentsavings=float(request.POST['currentsavings'])
	dependent=request.POST['dependentperson']
	pension=request.POST['pension']
        print(occupation)
        print(jobtype)
	print(income)
	print(expenditure)
        print(currentsavings)
	print(dependent)
	print(pension)
        goalname=request.POST['goalname']	
	print(goalname)
	goalvalue=float(request.POST['goalvalue'])
	print(goalvalue)
	timetogoal=float(request.POST['timetogoal'])
        print(timetogoal)
	investamount=float(request.POST['investamount'])
	print(investamount)
	expectreturns=float(request.POST['expectreturns'])
	print(expectreturns)

	#Future value of goal

 	rate=float(1+((7.9/100)/12))
	fvg=float(math.pow(rate,timetogoal))
	fvg1=float(fvg*goalvalue)
	fvg_final=int(fvg1)
	print(fvg_final)

	#Future value of Existing savings

	rate1=float(1+((8.0/100)/12))
	fvs=float(math.pow(rate1,timetogoal))
	fvs1=float(fvs*currentsavings)
	fvs_final=int(fvs1)
	print(fvs_final)

	#Future value of Investment
	
	rate2=float(expectreturns/1200)
	if rate2==0.0:
		rate2=1.0
	rate3=float(math.pow((1+rate2),timetogoal)-1)
	rate4=float(rate3/rate2)
	rate5=float(rate4*investamount)
	fvi_final=int(rate5)
	print(fvi_final)

   	#calculating shortfall
	shortfall=fvg_final-fvs_final-fvi_final
	print(shortfall)

	#calculating surplus
	

	#converting to int
	currentsavings1=int(currentsavings)
	goalvalue1=int(goalvalue)
	timetogoal1=int(timetogoal)
	investamount1=int(investamount)
	expectreturns1=int(expectreturns)
	income1=int(income)
	expenditure1=int(expenditure)
	surplus1=int(surplus)

	with open('output.csv', 'wb') as csvfile:
	    writer=csv.writer(csvfile)
	    writer.writerow(['Name','UID','Age','Nationality','Gender','Maritial_Status','Occupation','Job_type','Total Income per month','Total Expenses per month','Surplus per month','How much savings you have now? (Rs)','Dependent person','Age_pension','Goal Name','Goal Value in today value terms','Time to Goal (in months)','Amount you intend to invest per month for this goal','Expected rate of return you expect from your investment','Future Value of Goal','Future Value of Existing savings','Value of future investment','Shortfall in goal'])
  	    writer.writerow([name,uid,age,nationality,gender,marital,occupation,jobtype,income1,expenditure1,surplus1,currentsavings1,dependent,pension,goalname,goalvalue1,timetogoal1,investamount1,expectreturns1,fvg_final,fvs_final,fvi_final,shortfall])
 
	with open('historyDB.csv', 'a') as csvfile1:
	    if shortfall<0:
		str_res="Yes"
	    else:
		str_res="No"
	    writer=csv.writer(csvfile1)
	    writer.writerow([name,uid,age,nationality,gender,marital,occupation,jobtype,income1,expenditure1,surplus1,currentsavings1,dependent,pension,goalname,goalvalue1,timetogoal1,investamount1,expectreturns1,fvg_final,fvs_final,fvi_final,shortfall,str_res])
	

    def get_data():
        df = pd.read_csv("train.csv")
        return df
    
    df = get_data()

    class MultiColumnLabelEncoder:
        def __init__(self,columns = None):
            self.columns = columns # array of column names to encode

        def fit(self,X,y=None):
            return self # not relevant here

        def transform(self,X):	#Transforms columns of X specified in self.columns using LabelEncoder(). 
        
            output = X.copy()
            if self.columns is not None:
                for col in self.columns:
                    output[col] = LabelEncoder().fit_transform(output[col])
            else:
                for colname,col in output.iteritems():
                    output[colname] = LabelEncoder().fit_transform(col)
            return output

        def fit_transform(self,X,y=None):
            return self.fit(X,y).transform(X)
    output1=MultiColumnLabelEncoder(columns = ['Name','Goal Name']).fit_transform(df)

    df=output1
  
    def encode_target(df, target_column):
        df_mod = df.copy()
        targets = df_mod[target_column].unique()
        map_to_int = {name: n for n, name in enumerate(targets)}
        df_mod["Target"] = df_mod[target_column].replace(map_to_int)
        return (df_mod, targets)

    df2, targets = encode_target(df, "Will the goal be achieved")

    features = ['Total Income per month','Total Expenses per month','Surplus per month','Time to Goal (in months)','Goal Name','Goal Value in today value terms','Amount you intend to invest per month for this goal','How much savings you have now? (Rs)','Future Value of Existing savings','Value of future investment','Future Value of Goal']


    y = df2["Target"]
    X = df2[features]

    f1 = pd.read_csv("output.csv")

    output2=MultiColumnLabelEncoder(columns = ['Name','Goal Name']).fit_transform(f1)
    f1=output2
    X_test=pd.DataFrame(f1, columns = ['Total Income per month','Total Expenses per month','Surplus per month','Time to Goal (in months)','Goal Name','Goal Value in today value terms','Amount you intend to invest per month for this goal','How much savings you have now? (Rs)','Future Value of Existing savings','Value of future investment','Future Value of Goal'])
  
    svc = LinearSVC(C=1.0)
    svc.fit(X,y)

    global y_pred
    y_pred=svc.predict(X_test) 
    
    y_test=[1]
    def measure_performance(X,y,clf, show_accuracy=True, show_classification_report=True, show_confusion_matrix=True):

        if y_pred==1:
            print("Predicted class is : ",y_pred)
        else:
            print("Predicted class is : ",y_pred)
        if show_accuracy:
            print ("Accuracy:{0:.3f}".format(metrics.accuracy_score(y,y_pred)),"\n")

        if show_classification_report:
            print ("Classification report")
            print (metrics.classification_report(y,y_pred),"\n")
        
        if show_confusion_matrix:
            print ("Confusion matrix")
            print (metrics.confusion_matrix(y,y_pred),"\n")
          
    measure_performance(X_test,y_test,svc,show_classification_report=True, show_confusion_matrix=True)     

    if y_pred==1:
	if(goalname=='Buying a House'):
	    return HttpResponse("<center><body><b><br><br><br><font size='5'> <p style='color:#9932cc';>Yes you can buy the home....!!!</p></font></color><b></body></center>")
	if(goalname=='Education of Child'):
	    return HttpResponse("<center><body><b><br><br><br><font size='5'> <p style='color:#9932cc';>Yes you will have enough money to educate your child....!!!</p></font></color><b></body></center>")
	if(goalname=='Domestic Vacation'):
	    return HttpResponse("<center><body><b><br><br><br><font size='5'> <p style='color:#9932cc';>Yes Domestic vacation will possible within given time.. Enjoy!!!</p></font></color><b></body></center>")
	if(goalname=='Buying a Car'):
	    return HttpResponse("<center><body><b><br><br><br><font size='5'> <p style='color:#9932cc';>Yes you can buy the car....!!!!</p></font></color><b></body></center>")
	if(goalname=='Child Marriage'):
	    return HttpResponse("<center><body><b><br><br><br><font size='5'> <p style='color:#9932cc';>Yes you will have enough savings so you can think of childs marriage...!!!</p></font></color><b></body></center>")
    else:
	shortfall1=int(shortfall/timetogoal1)
	if(goalname=='Buying a House'):
	    return HttpResponse({"<center><body><b><br><br><br><p style='color:#9932cc';>NO.. you can't buy the home..<br><br>You need to invest additional amount Rs per month: ",shortfall1,"</body>"})
	if(goalname=='Education of Child'):
	    return HttpResponse({"<center><body><b><br><br><br><p style='color:#9932cc';> No..you won't be having enough money to educate your child.!!!<br><br> You need to invest additional amount Rs per month :",shortfall1,"</body>"})
	if(goalname=='Domestic Vacation'):
	    return HttpResponse({"<center><body><b><br><br><br> <p style='color:#9932cc';>NO... Domestic vacation won't be possible with  this savings..!!! <br><br>You need to invest additional amount Rs per month : ",shortfall1,"</center></body>"})
	if(goalname=='Buying a Car'):
	    return HttpResponse({"<center><body><b><br><br><br><p style='color:#9932cc';>NO... You can't buy the car....  <br><br>You need to invest additional amount Rs per month : ",shortfall1,"</body>"})
	if(goalname=='Child Marriage'):
	    return HttpResponse({"<center><body><b><br><br><br> <p style='color:#9932cc';>No.. You won't be having enough savings for childs marriage!!.<br><br>You need to invest additional amount Rs per month : ",shortfall1,"</body>"})
	


	

 

def register3(request): 
    if request.method=='POST':
	global name,age,uid,nationality,marital,gender
        name=request.POST['name2']
        age=request.POST['age']
        uid=request.POST['uid']
        nationality=request.POST['nationality']
        marital=request.POST['marritalstatus']
        gender=request.POST['genderradio']
        print(name)
        print(age)
        print(uid)
        print(nationality)
        print(marital)
        print(gender)
	global occupation,jobtype,income,expenditure,currentsavings,dependent,pension,surplus,goalname,shortfall
        occupation=request.POST['occupation']
	jobtype=request.POST['jobtype']
  	income=float(request.POST['income'])
	expenditure=float(request.POST['expenditure'])
	surplus=income-expenditure
	currentsavings=float(request.POST['currentsavings'])
	dependent=request.POST['dependentperson']
	pension=request.POST['pension']
        print(occupation)
        print(jobtype)
	print(income)
	print(expenditure)
        print(currentsavings)
	print(dependent)
	print(pension)
        goalname=request.POST['goalname']	
	print(goalname)
	goalvalue=float(request.POST['goalvalue'])
	print(goalvalue)
	timetogoal=float(request.POST['timetogoal'])
        print(timetogoal)
	investamount=float(request.POST['investamount'])
	print(investamount)
	expectreturns=float(request.POST['expectreturns'])
	print(expectreturns)
	path=request.POST['FileUpload']
	print(path)

	#Future value of goal

 	rate=float(1+((7.9/100)/12))
	fvg=float(math.pow(rate,timetogoal))
	fvg1=float(fvg*goalvalue)
	fvg_final=int(fvg1)
	print(fvg_final)

	#Future value of Existing savings

	rate1=float(1+((8.0/100)/12))
	fvs=float(math.pow(rate1,timetogoal))
	fvs1=float(fvs*currentsavings)
	fvs_final=int(fvs1)
	print(fvs_final)

	#Future value of Investment
	
	rate2=float(expectreturns/1200)
	if rate2==0.0:
		rate2=1.0
	rate3=float(math.pow((1+rate2),timetogoal)-1)
	rate4=float(rate3/rate2)
	rate5=float(rate4*investamount)
	fvi_final=int(rate5)
	print(fvi_final)

   	#calculating shortfall
	shortfall=fvg_final-fvs_final-fvi_final
	print(shortfall)

	#calculating surplus
	

	#converting to int
	currentsavings1=int(currentsavings)
	goalvalue1=int(goalvalue)
	timetogoal1=int(timetogoal)
	investamount1=int(investamount)
	expectreturns1=int(expectreturns)
	income1=int(income)
	expenditure1=int(expenditure)
	surplus1=int(surplus)

	with open('output.csv', 'wb') as csvfile:
	    writer=csv.writer(csvfile)
	    writer.writerow(['Name','UID','Age','Nationality','Gender','Maritial_Status','Occupation','Job_type','Total Income per month','Total Expenses per month','Surplus per month','How much savings you have now? (Rs)','Dependent person','Age_pension','Goal Name','Goal Value in today value terms','Time to Goal (in months)','Amount you intend to invest per month for this goal','Expected rate of return you expect from your investment','Future Value of Goal','Future Value of Existing savings','Value of future investment','Shortfall in goal'])
  	    writer.writerow([name,uid,age,nationality,gender,marital,occupation,jobtype,income1,expenditure1,surplus1,currentsavings1,dependent,pension,goalname,goalvalue1,timetogoal1,investamount1,expectreturns1,fvg_final,fvs_final,fvi_final,shortfall])
 


	with open('historyDB.csv', 'a') as csvfile1:
	    if shortfall<0:
		str_res="Yes"
	    else:
		str_res="No"
	    writer=csv.writer(csvfile1)
	    writer.writerow([name,uid,age,nationality,gender,marital,occupation,jobtype,income1,expenditure1,surplus1,currentsavings1,dependent,pension,goalname,goalvalue1,timetogoal1,investamount1,expectreturns1,fvg_final,fvs_final,fvi_final,shortfall,str_res])
	


    def get_data():
        df = pd.read_csv(path)
        return df
    
    df = get_data()

    class MultiColumnLabelEncoder:
        def __init__(self,columns = None):
            self.columns = columns # array of column names to encode

        def fit(self,X,y=None):
            return self # not relevant here

        def transform(self,X):	#Transforms columns of X specified in self.columns using LabelEncoder(). 
        
            output = X.copy()
            if self.columns is not None:
                for col in self.columns:
                    output[col] = LabelEncoder().fit_transform(output[col])
            else:
                for colname,col in output.iteritems():
                    output[colname] = LabelEncoder().fit_transform(col)
            return output

        def fit_transform(self,X,y=None):
            return self.fit(X,y).transform(X)
    output1=MultiColumnLabelEncoder(columns = ['Name','Goal Name']).fit_transform(df)

    df=output1
  
    def encode_target(df, target_column):
        df_mod = df.copy()
        targets = df_mod[target_column].unique()
        map_to_int = {name: n for n, name in enumerate(targets)}
        df_mod["Target"] = df_mod[target_column].replace(map_to_int)
        return (df_mod, targets)

    df2, targets = encode_target(df, "Will the goal be achieved")

    features = ['Total Income per month','Total Expenses per month','Surplus per month','Time to Goal (in months)','Goal Name','Goal Value in today value terms','Amount you intend to invest per month for this goal','How much savings you have now? (Rs)','Future Value of Existing savings','Value of future investment','Future Value of Goal']


    y = df2["Target"]
    X = df2[features]

    f1 = pd.read_csv("output.csv")

    output2=MultiColumnLabelEncoder(columns = ['Name','Goal Name']).fit_transform(f1)
    f1=output2
    X_test=pd.DataFrame(f1, columns = ['Total Income per month','Total Expenses per month','Surplus per month','Time to Goal (in months)','Goal Name','Goal Value in today value terms','Amount you intend to invest per month for this goal','How much savings you have now? (Rs)','Future Value of Existing savings','Value of future investment','Future Value of Goal'])
  
    svc = LinearSVC(C=1.0)
    svc.fit(X,y)

    global y_pred
    y_pred=svc.predict(X_test) 
    
    y_test=[1]
    def measure_performance(X,y,clf, show_accuracy=True, show_classification_report=True, show_confusion_matrix=True):

        if y_pred==1:
            print("Predicted class is : ",y_pred)
        else:
            print("Predicted class is : ",y_pred)
        if show_accuracy:
            print ("Accuracy:{0:.3f}".format(metrics.accuracy_score(y,y_pred)),"\n")

        if show_classification_report:
            print ("Classification report")
            print (metrics.classification_report(y,y_pred),"\n")
        
        if show_confusion_matrix:
            print ("Confusion matrix")
            print (metrics.confusion_matrix(y,y_pred),"\n")
          
    measure_performance(X_test,y_test,svc,show_classification_report=True, show_confusion_matrix=True)     

    if y_pred==1:
	if(goalname=='Buying a House'):
	    return HttpResponse("<center><body><b><br><br><br><font size='5'> <p style='color:#9932cc';>Yes you can buy the home....!!!</p></font></color><b></body></center>")
	if(goalname=='Education of Child'):
	    return HttpResponse("<center><body><b><br><br><br><font size='5'> <p style='color:#9932cc';>Yes you will have enough money to educate your child....!!!</p></font></color><b></body></center>")
	if(goalname=='Domestic Vacation'):
	    return HttpResponse("<center><body><b><br><br><br><font size='5'> <p style='color:#9932cc';>Yes Domestic vacation will possible within given time.. Enjoy!!!</p></font></color><b></body></center>")
	if(goalname=='Buying a Car'):
	    return HttpResponse("<center><body><b><br><br><br><font size='5'> <p style='color:#9932cc';>Yes you can buy the car....!!!!</p></font></color><b></body></center>")
	if(goalname=='Child Marriage'):
	    return HttpResponse("<center><body><b><br><br><br><font size='5'> <p style='color:#9932cc';>Yes you will have enough savings so you can think of childs marriage...!!!</p></font></color><b></body></center>")
    else:
	shortfall1=int(shortfall/timetogoal1)
	if(goalname=='Buying a House'):
	    return HttpResponse({"<center><body><b><br><br><br><p style='color:#9932cc';>NO.. you can't buy the home..<br><br>You need to invest additional amount Rs per month: ",shortfall1,"</body>"})
	if(goalname=='Education of Child'):
	    return HttpResponse({"<center><body><b><br><br><br><p style='color:#9932cc';> No..you won't be having enough money to educate your child.!!!<br><br> You need to invest additional amount Rs per month :",shortfall1,"</body>"})
	if(goalname=='Domestic Vacation'):
	    return HttpResponse({"<center><body><b><br><br><br> <p style='color:#9932cc';>NO... Domestic vacation won't be possible with  this savings..!!! <br><br>You need to invest additional amount Rs per month : ",shortfall1,"</center></body>"})
	if(goalname=='Buying a Car'):
	    return HttpResponse({"<center><body><b><br><br><br><p style='color:#9932cc';>NO... You can't buy the car....  <br><br>You need to invest additional amount Rs per month : ",shortfall1,"</body>"})
	if(goalname=='Child Marriage'):
	    return HttpResponse({"<center><body><b><br><br><br> <p style='color:#9932cc';>No.. You won't be having enough savings for childs marriage!!.<br><br>You need to invest additional amount Rs per month : ",shortfall1,"</body>"})
	

