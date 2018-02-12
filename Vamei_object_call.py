class SampleMore:
    def __call__(self, a):
        return a + 5

sample = SampleMore()
print(sample(2))