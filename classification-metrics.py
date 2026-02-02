from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
y_true = [1,0,1,1,0,1,0]
y_pred = [1,0,1,0,0,1,1]
print("accuracy:",accuracy_score(y_true,y_pred))#how many % model guessed
print("precision:",precision_score(y_true,y_pred))#how many positive prediction were correct
print("recall:",recall_score(y_true,y_pred))#how many actual positive data i get
print("f1:",f1_score(y_true,y_pred))#recall+precision