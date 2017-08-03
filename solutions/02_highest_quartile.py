highest_quartile = df[df['LiteracyRate'] >= 97.85]
highest_quartile = highest_quartile.set_index('Country')
highest_quartile.sort_values('LiteracyRate')['LiteracyRate'].plot(kind='bar')
