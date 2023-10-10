from Average import Average as av

class Average_of_two_list:   
    def average_two_lst(list_1: list[int | float], list_2: list[int | float]) -> str:
        res1 = av.average(list_1)
        res2 = av.average(list_2)
        if res1 == res2:
            return 'Средние значения равны'
        match res1 > res2:
            case True:
                return 'Первый список имеет большее среднее значение'
            case False:
                return 'Второй список имеет большее среднее значение'
   
            