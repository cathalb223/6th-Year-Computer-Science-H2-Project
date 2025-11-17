import pandas

info = pandas.read_csv('Terraria DPS_TV1.4.4.9_V1 - Sheet1.csv')
info = info.drop(columns=['OBSERVATIONS'])

print(info.head())
info['DPS (SINGLE TARGET)'] = pandas.to_numeric(info['DPS (SINGLE TARGET)'], errors='coerce')
info = info.dropna(subset=['DPS (SINGLE TARGET)'])

for index, row in info.iterrows():
    if row['CLASS'] not in ["Ranger", "Mage", "Summoner", "Melee"]:
        info.at[index, 'CLASS'] = None

    if row["GAME PROGRESSION"] in ["Post-Moonlord", "Post-Cultist", "Post-WoF", "Post-EoL", "Post-Golem", "Post-Plantera", "Post-SkeletronPrime", "Post-Destroyer", "Post-QueenSlime", "Post-Twins"]:
        info.at[index, 'GAME PROGRESSION'] = 'Hardmode'

    elif row["GAME PROGRESSION"] in ["Post-Brain/Worm", "Pre-Boss", "Post-Deerclops", "Post-QueenBee", "Post-Skeletron", "Post-Eye"]:
        info.at[index, "GAME PROGRESSION"] = 'Pre-Hardmode'
    
    else:
        info.at[index, "GAME PROGRESSION"] = None


info.to_csv('newdata.csv', index=False)   