import joblib

class Model:
  model = None
  
  def __init__(self, path:str):
   self.model= self.load_model(path)

  def load_model(self, path:str):
    try:
      return joblib.load(path)
    except Exception as ee:
      return None, "Model not loaded"
  
  def tokenize(self, text):
    if(self.model):
      return self.model.tokenize(text)
    else:
      return "Model not loaded"
  
model1 = Model("/Users/japeto/t1-pln-2024/models/model2.pkl")
model2 = Model("/Users/japeto/t1-pln-2024/models/model2.pkl")
model3 = Model("/Users/japeto/t1-pln-2024/models/model3.pkl")


