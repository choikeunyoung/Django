from django.shortcuts import render
import random

def index(request):
    # num_dict = []
    # while len(num_dict) == 6:
    #     nums = random.randrange(1,45)
    #     if nums not in num_dict:
    #         num_dict.append(nums)
    # context = {
    #     'num' : num_dict
    # }
    lotto_list = []
    result_list = []
    bonus, *lotto_winner = random.sample(range(1,46),7)

    for _ in range(5):
        lotto = random.sample(range(1,46),6)
        count = 0
        result = 0
        for num in lotto:
            if num in lotto_winner:
                count += 1
        if count == 3:
            result = 5
        elif count == 4:
            result = 4
        elif count == 5:
            if bonus not in lotto:
                result = 3
            else:
                result = 2
        elif count == 6:
            result = 1
        lotto_list.append((lotto, result))
        # result_list.append(result)

    context = {
        "lotto_winner" : lotto_winner,
        "bonus" : bonus,
        "lotto_list" : lotto_list,
        # "result" : result_list,
    }

    return render(request,'lotto.html', context)