from django.shortcuts import render
import random


def index(request):

    menus = ['삼겹살','피자','치킨','중국집','다이어트']

    menu = random.choice(menus)

    if menu == '삼겹살':
        imgs = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ9h_G7aLr2jOBL7toFnkD-K5uelSyJ38W0w&usqp=CAU'
    elif menu == '피자':
        imgs = 'https://img.hankyung.com/photo/202108/99.26501439.1-1200x.jpg'
    elif menu == '치킨':
        imgs = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwre5xcz-pTDOg88sdDHo9wIvrwRlaLTpuUA&usqp=CAU'
    elif menu == '중국집':
        imgs = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvwQOrMlNs7ThYlo9-sCqR-RFI0uBTdDpKlw&usqp=CAU'
    elif menu == '다이어트':
        imgs = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRSAnk3CuNSFLvFH7TyL8FmCUrzBVO3xLhUuXNjUdLnelBZQXcFlhqgduXw1_cW9V8BmA&usqp=CAU'
    context = {
        'menu' : menu,
        'img' : imgs
    }

    return render(request,'dinner.html', context)