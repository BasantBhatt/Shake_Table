print("Welcome, Basant Bhatt")

import math
from matplotlib import pyplot as plt


mass = []
acc = []

H = 100 ## kg
u = 1/5 ## frictional coefficient
m = 450 ## (Maximum load you want to input + 50 ) 


freq = {}
amp = {}

for i in range(50, m, 50): ## calculation starts from 50kg with the increment of 50kg
    
    a = (H/i) - u
    acc.append(a)
    
    freq['fre_' + str(i)] = []
    amp['amp_' + str(i)] = 1000*[]
    
    
    for j in range (5, 100, 5): ### j is the amplitude
       
        amp['amp_' + str(i)].append(j)
        
        f =math.sqrt(a/(j/1000)) / (2 * math.pi )
        freq['fre_' + str(i)].append(f)
        
        
    mass.append(i)



### Graph Plotting of the values
for i in range(50, m, 50):
      plt.plot(freq['fre_' + str(i)], amp['amp_' + str(i)], label= (str(i) + "kg"))
    

font = {'family': 'serif',   ## Making font styles
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
        

plt.style.use('fivethirtyeight')

plt.grid(True) ## shows Major grid lines, automatically
plt.grid(which='minor', alpha = 0.2, linewidth= 0.8) ## Shows minor grid lines between the major grid line
plt.minorticks_on() ## Shows minor tick(|) marks in x&y axies

plt.axvline(x=0, ymin=0, ymax=0)  ## shows the x=0 line in graph
plt.axhline(y=0, xmin=0, xmax=0)  ## shows the y=0 line in graph

plt.title(" Freq vs Amp", fontdict = font)
plt.xlabel("Frequency", fontdict = font)
plt.ylabel("Amplitude", fontdict = font)

plt.tight_layout()
plt.legend()

plt.savefig("Freq_vs_amp_with_all_mass.png")
plt.show()

print("Thank you Basant Bhatt")