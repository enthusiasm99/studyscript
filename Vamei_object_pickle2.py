import pickle

class Bird(object):
    have_feather = True
    reproduction_method = "egg"

with open("summer.pkl", "rb") as g:
    summer = pickle.load(g)

print(summer.have_feather)