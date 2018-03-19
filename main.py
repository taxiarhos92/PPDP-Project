from functions import *
import copy

print('Privacy preserving data publishing project')

hospital_data = QID_maker('hospital_data.csv', 'hospital_data_new.csv')

k_list, group_count, k_anonymity = k_anonymity_func(hospital_data)
l_diversity = l_diversity_func(k_list, hospital_data, group_count)
entropy_l_diversity = entropy_l_diversity_func(k_list, hospital_data, group_count)
print('These are the results.\n++++++++++++++++++++++++++++++++++')
print('The value of k-anonymity is: ', k_anonymity)
print('The value of l-diversity is: ', l_diversity)
print('The value of entropy l-diversity is: %.3f' %entropy_l_diversity)
print('++++++++++++++++++++++++++++++++++')

ans = input("Do you want Generalization? Yes or No: ")
if ans == 'Yes' or ans == 'yes':
    file_name = input('Enter the file name into .csv format: ')
    n = int(input('For Generalization [0-29][30-49][50-69][70-89] insert 1.\n'
                  'For Generalization [0-49][50-79][80-89] insert 2.\n'
                  'For Generalization with two fields insert 3.\n'
                  'For Another Generalization with two fields insert 4: '))
    while ans == 'yes':
        print('--------------------Generalization is starting------------------')
        if n == 1:
            generalized_data, count = generalization_1(copy.deepcopy(hospital_data))
            k, l, entropy, loss = gen(generalized_data, file_name, count, count_race='none', n=1)
        if n == 2:
            generalized_data, count = generalization_2(copy.deepcopy(hospital_data))
            k, l, entropy, loss = gen(generalized_data, file_name, count, count_race='none', n=2)
        if n == 3:
            generalized_data, count, count_race = generalization_3(copy.deepcopy(hospital_data))
            k, l, entropy, loss = gen(generalized_data, file_name, count, count_race, n=3)
        if n == 4:
            generalized_data, count, count_race = generalization_4(copy.deepcopy(hospital_data))
            k, l, entropy, loss = gen(generalized_data, file_name, count, count_race, n=4)

        print('These are the results.\n*****++++++++++++++++++++++++++++++*****')
        print('The value of k-anonymity is: ', k)
        print('The value of l-diversity is: ', l)
        print('The value of entropy l-diversity is: %.3f' %entropy)
        print('The value of ILoss is: %.3f' %loss)
        print('*****++++++++++++++++++++++++++++++*****')
        print('--------------------Generalization finished------------------')

        ans = input('If you want another generalization enter (yes) for (exit = 0): ')
        if ans == '0' or ans != 'yes':
            print('Goodbye and have a nice day!!!')
            break
        file_name = input('Enter the file name into .csv format: ')
        n = int(input('For Generalization [0-29][30-49][50-69][70-89] insert 1.\n'
                      'For Generalization [0-49][50-79][80-89] insert 2.\n'
                      'For Generalization with two fields insert 3.\n'
                      'For Another Generalization with two fields insert 4: '))
else:
    print('Goodbye and have a nice day!!!')
