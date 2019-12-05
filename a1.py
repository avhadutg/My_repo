import pickle
import os

f = open("mainprogramfor3.py", "r")
val=f.read()
f.close()
pickle_out=open('main.pkl','wb')
pickle.dump(val, pickle_out)
pickle_out.close()

pickle_in=open('main.pkl','rb')
val2=pickle.load(pickle_in)

f1=open('main.py','w')
f1.write(val2)
f1.close()
pickle_in.close()

os.system('python main.py ')
