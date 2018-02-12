import pickle

class Bird:
    have_feather = True
    reproduction_method = "egg"

summer = Bird()
with open("summer.pkl", "wb") as f:
    pickle.dump(summer, f)


