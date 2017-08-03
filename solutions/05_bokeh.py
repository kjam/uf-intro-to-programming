countries = ['United Kingdom', 'Germany', 'Greece', 'United States', 'Czech Republic']
subset = unemployment.loc[countries]

chart = draw_line_chart(subset)

show(chart)
