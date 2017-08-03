dummy_races = pd.get_dummies(df.race, prefix='race')
df = df.drop('race', axis=1).join(dummy_races)

# now adding the education dummy dataframe
dummy_education = pd.get_dummies(df.education, prefix='education')
df = df.drop('education', axis=1).join(dummy_education)

df.head()
