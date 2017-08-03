new_df['grade_3q'] = new_df.groupby('grade').price.transform(
        lambda price: np.percentile(price, q=75))
above = new_df[new_df.price > new_df.grade_3q]
print(above.shape[0])
