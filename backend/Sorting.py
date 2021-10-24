
import math

container_sizes = [(227, 580, 225), 
                   (227, 1180, 225)]

pallet_sizes = [(102, 140, 12, 25), 
                (102, 122, 12, 22), 
                (90, 122, 12, 20), 
                (75, 110, 12, 12), 
                (89, 138, 12, 18)] #(width, length, height, weight)

Sorted_pallet_sizes = sorted(pallet_sizes, key = lambda pallet: pallet[0]*pallet[1]*pallet[2], reverse=True)
print('Sorted_pallet_sizes:', Sorted_pallet_sizes)
print('-' * 50)
alpha = 0.5 #0-1
item_sequence = [(30, 15, 10, 300),     #4500, 300   #(width, length, height, weight)
                 (30, 5, 10, 350),      #1500, 350 
                 (30, 5, 10, 50),       #1500, 50 
                 (50, 48, 40, 100),     #96000, 100 
                 (70, 30, 50, 10),      #105000, 10 
                 (35, 45, 50, 250),     #78750, 250
                 (2, 2, 2, 200),         #8, 25
                 (2, 2, 2, 2)]          #8, 2
                 
                 

Sorted_item_sequence = sorted(item_sequence, key = lambda box: alpha*box[3] + (1 - alpha)*math.log10(box[0]*box[1]*box[2]), reverse=True)
print('Sorted_item_sequence:', Sorted_item_sequence)

