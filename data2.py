import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#data: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Umwelt/Abfallwirtschaft/Tabellen/liste-deponien.html;jsessionid=0FB686343155EDB888675D818413704B.live731
data = pd.read_csv('C:\\Users\\Samuel\\Desktop\\zerodata\\Collected_used_sales_packaging.txt', sep=',',
                   encoding='unicode_escape', decimal='.')

plt.figure(figsize=(15,5))

plt.title('Used Packaging in Germany (in 1000tons)', fontdict= {'fontweight' :'bold','fontsize' : 18})
plt.xlabel('year')
plt.ylabel('collected sales packagings')

plt.plot(data['year'], data['glas'], label='glas')
plt.plot(data['year'],data['paper'],label='paper')
plt.plot(data['year'],data['mixed packaging'],label='mixed packaging')

plt.legend()
plt.show()

plt.title('Used Packaging in Germany (in 1000tons)', fontdict= {'fontweight' :'bold','fontsize' : 18})
plt.xlabel('year')
plt.ylabel('collected sales packagings')

plt.plot(data['year'],data['metals'],label='metals')
plt.plot(data['year'],data['composites'],label='composites')
plt.plot(data['year'],data['plastics'],label= 'plastics')



plt.legend()
plt.show()

