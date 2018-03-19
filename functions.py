import csv, math

def sorting(first_csv, last_csv, column, field):
    reader = csv.reader(open(first_csv), delimiter=";")
    with open(first_csv):
        if column == 2 and field == 'num':
            sortedlist = sorted(reader, key=lambda row: int(row[column]), reverse=False)
        elif column == 2 and field == 'txt':
            sortedlist = sorted(reader, key=lambda row: row[column], reverse=False)
        else:
            sortedlist = sorted(reader, key=lambda row: row[column], reverse=False)
        with open(last_csv, "w") as csv_file:
            for row in sortedlist:
                for column in row:
                    csv_file.write('%s;' % column)
                csv_file.write('\n')
            csv_file.close()
    return sortedlist

def QID_maker(first, last):
    sorting(first, last, 0, 'txt')
    sorting(last, last, 1, 'txt')
    return sorting(last, last, 2, 'num')


def k_anonymity_func(final_array):
    row = k = 1
    group_count = 0
    k_list = []

    while row < 10000:
        if final_array[row - 1][0] == final_array[row][0] and final_array[row - 1][1] == final_array[row][1] and \
                        final_array[row - 1][2] == final_array[row][2]:
            k += 1
        else:
            k_list.append(k)
            group_count += 1
            k = 1
        row += 1
    else:
        k_list.append(k)
        group_count += 1

    return k_list, group_count, min(k_list)


def l_diversity_func(k_list, final_array, group_count):
    diseases = []
    l_list = []
    r = row = 1
    for k in range(0, group_count):
        while k_list[k] >= r:
            if not (final_array[row - 1][3] in diseases):
                diseases.append(final_array[row - 1][3])
            r += 1
            row += 1
        l_list.append(len(diseases))
        diseases = []
        r = 1

    return min(l_list)

def entropy_l_diversity_func(k_list, final_array, group_count):
    entropy = []
    r = row = 1
    result = 0
    min_entropy = 1000
    for k in range(0, group_count):
        while k_list[k] >= r:
            entropy.append(final_array[row - 1][3])
            r += 1
            row += 1
        for disease in entropy:
            l = entropy.count(disease)
            result = result + (-l / k_list[k] * math.log(l / k_list[k]))
        if result < min_entropy:
            min_entropy = result
        if min_entropy == 0.0:
            min_entropy = 1
        entropy = []
        r = 1
        result = 0
    return min_entropy

def i_loss_func(generalized_data, k_list, count, count_race, n):
    row, i, j, k, iloss = 1, 0, 0, 0, 0

    while row <= 9999:
        if n == 1 or n == 2:
            row += k_list[i]

            iloss += ((count[j] - 1) / 100) * k_list[i]

            if row == 10001:
                break
            if generalized_data[row-2][2] != generalized_data[row-1][2]:
                j += 1
            i += 1
        elif n == 3 or n == 4:
            row += k_list[i]

            iloss += (((count[j] - 1) / 100) + ((count_race[k] - 1) / sum(count_race))) * k_list[i]

            if row == 10001:
                break
            if generalized_data[row - 2][2] != generalized_data[row - 1][2]:
                j += 1
            if generalized_data[row - 2][1] != generalized_data[row - 1][1]:
                k += 1
                if k == len(count_race):
                    k = 0
            i += 1
    return iloss

def generalization_1(data):
    row = 1
    count = []
    count1 = []
    count2 = []
    count3 = []
    count4 = []
    while row <= 10000:
        if int(data[row-1][2]) < 30:
            if data[row-1][2] not in count1:
                count1.append(data[row-1][2])
            data[row - 1][2] = '[0-29]'
        elif int(data[row-1][2]) < 50:
            if data[row-1][2] not in count2:
                count2.append(data[row-1][2])
            data[row - 1][2] = '[30-49]'
        elif int(data[row-1][2]) < 70:
            if data[row-1][2] not in count3:
                count3.append(data[row-1][2])
            data[row - 1][2] = '[50-69]'
        elif int(data[row-1][2]) < 90:
            if data[row-1][2] not in count4:
                count4.append(data[row-1][2])
            data[row - 1][2] = '[70-89]'

        row += 1
    count.append(len(count1))
    count.append(len(count2))
    count.append(len(count3))
    count.append(len(count4))
    return data, count

def generalization_2(data):
    row = 1
    count = []
    count1 = []
    count2 = []
    count3 = []
    while row <= 10000:
        if int(data[row-1][2]) < 50:
            if data[row-1][2] not in count1:
                count1.append(data[row-1][2])
            data[row - 1][2] = '[0-49]'
        elif int(data[row - 1][2]) < 80:
            if data[row-1][2] not in count2:
                count2.append(data[row-1][2])
            data[row - 1][2] = '[50-79]'
        elif int(data[row - 1][2]) < 90:
            if data[row-1][2] not in count3:
                count3.append(data[row-1][2])
            data[row - 1][2] = '[80-89]'

        row += 1
    count.append(len(count1))
    count.append(len(count2))
    count.append(len(count3))
    return data, count

def generalization_3(data):
    row = 1
    count, count1, count2, count_race, count_race1, count_race2, count_race3, count_race4, count_race5 = [], [], [], [], [], [], [], [], []
    while row <= 10000:
        if 'Asian or Asian British:' in data[row-1][1]:
            if data[row-1][1] not in count_race1:
                count_race1.append(data[row - 1][1])
            data[row - 1][1] = 'Asian'
        elif 'Black or Black British:' in data[row-1][1]:
            if data[row-1][1] not in count_race2:
                count_race2.append(data[row - 1][1])
            data[row - 1][1] = 'Black'
        elif 'Mixed:' in data[row-1][1]:
            if data[row-1][1] not in count_race3:
                count_race3.append(data[row - 1][1])
            data[row - 1][1] = 'Mixed'
        elif 'Other:' in data[row-1][1]:
            if data[row-1][1] not in count_race4:
                count_race4.append(data[row - 1][1])
            data[row - 1][1] = 'Other'
        elif 'White:' in data[row - 1][1]:
            if data[row-1][1] not in count_race5:
                count_race5.append(data[row - 1][1])
            data[row - 1][1] = 'White'

        if int(data[row-1][2]) < 65:
            if data[row-1][2] not in count1:
                count1.append(data[row-1][2])
            data[row - 1][2] = '[0-64]'
        elif int(data[row - 1][2]) < 90:
            if data[row-1][2] not in count2:
                count2.append(data[row-1][2])
            data[row - 1][2] = '[65-89]'

        row += 1
    count.append(len(count1))
    count.append(len(count2))

    count_race.append(len(count_race1))
    count_race.append(len(count_race2))
    count_race.append(len(count_race3))
    count_race.append(len(count_race4))
    count_race.append(len(count_race5))
    return data, count, count_race

def generalization_4(data):
    row = 1
    count, count1, count2, count_race, count_race1, count_race2, count_race3, count_race4, count_race5, count_race6 = [], [], [], [], [], [], [], [], [], []
    while row <= 10000:
        if 'Asian or Asian British:' in data[row-1][1]:
            if data[row-1][1] not in count_race1:
                count_race1.append(data[row - 1][1])
            data[row - 1][1] = 'Asian'
        elif 'Black or Black British:' in data[row-1][1]:
            if data[row-1][1] not in count_race2:
                count_race2.append(data[row - 1][1])
            data[row - 1][1] = 'Black'
        elif 'Mixed:' in data[row-1][1]:
            if data[row-1][1] not in count_race3:
                count_race3.append(data[row - 1][1])
            data[row - 1][1] = 'Mixed'
        elif 'Other:' or 'White: Other' in data[row-1][1]:
            if data[row-1][1] not in count_race4:
                count_race4.append(data[row - 1][1])
            data[row - 1][1] = 'Other'
        elif 'White: British' in data[row - 1][1]:
            if data[row-1][1] not in count_race5:
                count_race5.append(data[row - 1][1])
            data[row - 1][1] = 'White British'
        elif 'White: Irish' or 'White: Gypsy or Irish Traveller' in data[row - 1][1]:
            if data[row-1][1] not in count_race6:
                count_race6.append(data[row - 1][1])
            data[row - 1][1] = 'White Irish'

        if int(data[row-1][2]) < 75:
            if data[row-1][2] not in count1:
                count1.append(data[row-1][2])
            data[row - 1][2] = '[0-74]'
        elif int(data[row - 1][2]) < 90:
            if data[row-1][2] not in count2:
                count2.append(data[row-1][2])
            data[row - 1][2] = '[75-89]'

        row += 1
    count.append(len(count1))
    count.append(len(count2))

    count_race.append(len(count_race1))
    count_race.append(len(count_race2))
    count_race.append(len(count_race3))
    count_race.append(len(count_race4))
    count_race.append(len(count_race5))
    count_race.append(len(count_race6))
    return data, count, count_race


def gen(generalized_data, gen_csv, count, count_race, n):

    with open(gen_csv, "w") as csv_file:
        for row in generalized_data:
            for column in row:
                csv_file.write('%s;' % column)
            csv_file.write('\n')
        csv_file.close()

    sorting(gen_csv, gen_csv, 0, 'txt')
    sorting(gen_csv, gen_csv, 1, 'txt')
    first_generalized_data = sorting(gen_csv, gen_csv, 2, 'txt')

    k_list, group_count, k_anonymity = k_anonymity_func(first_generalized_data)
    l_diversity = l_diversity_func(k_list, first_generalized_data, group_count)
    entropy_l_diversity = entropy_l_diversity_func(k_list, first_generalized_data, group_count)
    iloss = i_loss_func(first_generalized_data, k_list, count, count_race, n)

    return k_anonymity, l_diversity, entropy_l_diversity, iloss