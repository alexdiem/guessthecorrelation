import random
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

lives = 3
Score = 0
while lives > 0:
    x = np.random.normal(0,random.randint(0,200),random.randint(10,500))
    dev = random.randint(0,300)
    y = [i+np.random.normal(0,dev) for i in x]
    df = pd.DataFrame({'x':x,'y':y})
    sns.jointplot(x='x', y='y', data=df, kind='reg', joint_kws={'line_kws':{'color':'red'}})
    plt.show()
    corr = np.corrcoef(x,y)[0][1]
    corrpercent = 100*corr
    while True:
        try:
            uinput = float(input('Gjett korrelasjonen mellom 0 og 100% '))
            break
        except ValueError:
            print('Input must be float!')
            
    if abs(corrpercent-uinput) > 10:
        lives -= 1
        print('Feil! Korrelasjon: '+ str(corrpercent) +' Liv: ' + str(lives))
    elif abs(corrpercent-uinput) < 3:
        lives  += 1
        Score += 5
        print('Akkurat! Korrelasjon: '+ str(corrpercent) +' Du får et ekstra liv! Liv: ' + str(lives) +' Score: ' + str(Score))    
    else:
        Score += 1
        print('Bra! Korrelasjon: '+ str(corrpercent) +' Resultat: ' + str(Score))
        
print('Game over! Score: '+ str(Score))