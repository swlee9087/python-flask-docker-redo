from book_modu.population.models import Population

if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    # name = input('조사 대상 지역 (읍면동) 입력: ')
    # pop.pop_per_dong()
    # pop.find_by_dong(input(f'알고 싶은 지역 (읍면동) 입력: '))
    # pop.show_plot(pop.pop_per_dong('역삼1동'))
    # pop.show_plot(pop.find_by_dong(input(f'알고 싶은 지역 (읍면동) 입력: ')))
    # pop.find_dong_pd()
    # pop.show_plot(pop.find_dong_pd())
    # pop.find_similar_dong_pd(pop.find_dong_pd())
    pop.find_home('구래동')
    pop.home = pop.list_to_array(pop.home)
    # pop.home = arr_home
    # print(f' pop.home : \n{pop.home}')
    #    pop.show_plot_home(arr_home, '보광동')
    pop.find_similar_area('구래동')
    pop.show_plot_similar_two_cities('구래동', pop.home, pop.away)
