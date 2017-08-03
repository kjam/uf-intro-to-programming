for num in random_nums:
    if is_outlier(num, first_quartile, third_quartile):
        print(num)
