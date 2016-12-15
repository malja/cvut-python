# Zadání:
#########
#
# Napište program, který pomocí konstrukce for i in range(od, do, krok):
# - vytiskněte čísla 10 až 500 po deseti
# - vytiskněte čísla -20 až -600 po dvaceti
# napište program, který udělá to samé pomocí while cyklu:
# - vytiskněte čísla 10 až 500 po deseti
# - vytiskněte čísla -20 až -600 po dvaceti
###############################################################################

for i in range( 10, 500 + 1, 10):
    print(i)

for i in range(-20, -600 - 1, -20):
    print(i)

# To samé pomocí smyčky while. 
# Dle StackOverflow by tato smyčka měla být pomalejší něž pomocí for
# https://stackoverflow.com/questions/869229/why-is-looping-over-range-in-python-faster-than-using-a-while-loop
i = 10
while i <= 500:
    print(i)
    i += 10

i = -20
while i >= -600:
    print(i)
    i -= 20