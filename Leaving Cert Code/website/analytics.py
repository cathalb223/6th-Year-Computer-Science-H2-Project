import plotly.express as plt
import pandas



info = pandas.read_csv('newdata.csv')

pandas.DataFrame(info)
dps_median_yay = info['DPS (SINGLE TARGET)'].median()
dps_mean_yay= info['DPS (SINGLE TARGET)'].mean()

print("Dps single median: ", dps_median_yay, " Dps single mean: ", dps_mean_yay)

multi_target_median = info['DPS (MULTI TARGET)'].median()
multi_target_mean = info['DPS (MULTI TARGET)'].mean()

print("Dps multi median: ", multi_target_median, " Dps multi mean: ", multi_target_mean)

dps_projectile_median = info['DPS (SINGLE TARGET + PROJECTILE ONLY)'].median()
dps_projectile_mean = info['DPS (SINGLE TARGET + PROJECTILE ONLY)'].mean()

print("Dps projectile single median: ", dps_projectile_median, " Dps projectile single mean: ", dps_projectile_mean)

dps_projectile_multi_target_median = info['DPS (MULTI TARGET + PROJECTILE ONLY)'].median()
dps_projectile_multi_target_mean = info['DPS (MULTI TARGET + PROJECTILE ONLY)'].mean()


print("Dps projectile multi single median: ", dps_projectile_multi_target_median, " Dps projectile multi single mean: ", dps_projectile_multi_target_mean)

ClassesCount = info['CLASS'].value_counts().reset_index()
ClassesCount.columns = ['Class', 'Frequency']

classgraph = plt.pie(ClassesCount, names= 'Class', values= 'Frequency', title = 'Class Frequencies')
classgraph.write_html("classgraph.html")


random_weapons = info.sample(n=10)

colours = ['blue' if gp == 'Pre-Hardmode' else 'red' for gp in random_weapons['GAME PROGRESSION']]

dpsgraph = plt.bar(random_weapons, x = 'NAME', y = 'DPS (SINGLE TARGET)', title = 'Random selection of Weapon DPS', color = 'GAME PROGRESSION')
dpsgraph.write_html("dpsgraph.html")

random_weapons_multi = info.dropna(subset=['DPS (MULTI TARGET)'] and ['DPS (SINGLE TARGET + PROJECTILE ONLY)'] and ['DPS (MULTI TARGET + PROJECTILE ONLY)'])

DpsMultiTargetGraph = plt.scatter_3d(random_weapons_multi, x= 'DPS (MULTI TARGET)', y= 'DPS (SINGLE TARGET + PROJECTILE ONLY)', z= 'DPS (MULTI TARGET + PROJECTILE ONLY)', title = 'Scatter Plot of Multi Target, Projectile Single Target and Projectile Multi Target DPS', color= 'NAME')
DpsMultiTargetGraph.write_html("DpsMultiTargetGraph.html")