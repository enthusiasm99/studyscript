class num:
    def __init__(self, value):
        self.value = value

    def get_neg(self):
        return -self.value

    def set_neg(self, value):
        self.value = -value

    def del_neg(self):
        print("value also deleted")
        del self.value

    neg = property(get_neg, set_neg, del_neg, "I'm negative")

x = num(11)
print( x.neg )

x.neg = 22
print(x.value)

print(num.neg.__doc__)

del x.neg