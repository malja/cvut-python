# Alternativní řešení
#
# Zadání viz. seq_sum.py
#####################################################################

# Pole čísel
nums = list(map(int, input().split()));

# Maximální číslo
length = len(nums);

sum = 0;
count = 0;

best_sum = 0;
best_count= 0;

# Projde pole
for i in range( length ):
    
    # Pokud jde o první prvek, přeskočí ho. Dále využívám indexu i-1
    # což by v tomto případě způsobilo problémy
    if ( i-1 < 0 ):
        continue;

    # Přičte číslo k aktuální posloupnosti
    sum += nums[i-1];
    # Zvýší počet čísel v posloupnosti
    count += 1;

    # Pokud aktuální číslo je menší, než předchozí, přeruší se posloupnost
    if ( nums[i] < nums[i-1] ):
        # Jestliže byla nalezena lepší posloupnost, nebo má vyšší sumu
        if ( ( count > best_count) or ( (count == best_count ) and ( sum > best_sum ) ) ):

            best_count = count;
            best_sum = sum;

            count = 0;
            sum = 0;

print( best_sum );
print( best_count );
        
            
