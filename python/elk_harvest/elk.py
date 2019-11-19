import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

elk_data = pd.read_csv('Data/elk_2004-2018.csv', index_col='License Year')

elk_data['Overall Efficiency'] = elk_data['Total Harvest'] / elk_data['Days']
elk_data['Bull Efficiency'] = elk_data['Bulls'] / elk_data['Days']
elk_data['Trophy Efficiency'] = elk_data['6 or More Points'] / elk_data['Days']

trophy = elk_data[[' Hunting District','Residency','Days','6 or More Points']]
trophy_sum = trophy[trophy.Residency == 'SUM']

trophy_sum_215 = trophy_sum[trophy_sum[' Hunting District'].isin(['215'])]
trophy_sum_293 = trophy_sum[trophy_sum[' Hunting District'].isin(['293'])]
trophy_sum_312 = trophy_sum[trophy_sum[' Hunting District'].isin(['312'])]
trophy_sum_318 = trophy_sum[trophy_sum[' Hunting District'].isin(['318'])]
trophy_sum_335 = trophy_sum[trophy_sum[' Hunting District'].isin(['335'])]
trophy_sum_343 = trophy_sum[trophy_sum[' Hunting District'].isin(['343'])]
trophy_sum_350 = trophy_sum[trophy_sum[' Hunting District'].isin(['350'])]
trophy_sum_370 = trophy_sum[trophy_sum[' Hunting District'].isin(['370'])]
trophy_sum_388 = trophy_sum[trophy_sum[' Hunting District'].isin(['388'])]
trophy_sum_390 = trophy_sum[trophy_sum[' Hunting District'].isin(['390'])]
trophy_sum_391 = trophy_sum[trophy_sum[' Hunting District'].isin(['391'])]
trophy_sum_392 = trophy_sum[trophy_sum[' Hunting District'].isin(['392'])]
trophy_sum_393 = trophy_sum[trophy_sum[' Hunting District'].isin(['393'])]
trophy_sum_446 = trophy_sum[trophy_sum[' Hunting District'].isin(['446'])]
trophy_sum_451 = trophy_sum[trophy_sum[' Hunting District'].isin(['451'])]
trophy_sum_452 = trophy_sum[trophy_sum[' Hunting District'].isin(['452'])]

HDs = [
    trophy_sum_215, 
    trophy_sum_293,
    #trophy_sum_312,
    trophy_sum_318,
    trophy_sum_335,
    trophy_sum_343,
    #trophy_sum_350,
    #trophy_sum_370,
    trophy_sum_388,
    #trophy_sum_390,
    trophy_sum_391,
    trophy_sum_392,
    #trophy_sum_393,
    #trophy_sum_446,
    #trophy_sum_451,
    #trophy_sum_452
]

for i in range(len(HDs)):
    print(HDs[i], '\n')
    
plt.style.use('seaborn-darkgrid')
my_dpi=96
plt.figure(figsize=(480/my_dpi, 480/my_dpi), dpi=my_dpi)

# gca stands for 'get current axis'
#ax = plt.gca()

#choose Hunting District to highlight
HD_of_interest = trophy_sum_215

for HD in HDs:
    plt.plot(HD.index, HD['6 or More Points'], marker='', color='grey', linewidth=1, alpha=0.4)
    plt.text(2018.1, HD['6 or More Points'].tail(1), HD[' Hunting District'][2018])
    plt.text(2019, HD_of_interest['6 or More Points'].tail(1), "(HD of interest)", color='orange', size='medium')

plt.plot(HD_of_interest.index, HD_of_interest['6 or More Points'], marker='', color='orange', linewidth=4, alpha=0.65)

plt.show()
