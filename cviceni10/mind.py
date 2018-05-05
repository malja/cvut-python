import itertools

class mind:
    """
    Třída řešící hru Mastermind ve třech úrovních obtížnosti. 

    Podporované módy:
        1) Hádání 4 pozic se 6 barvami
        2) Hádání 5 pozic s 7 barvami
        3) Hádání 6 pozic s 8 barvami
    
    O zadání, učování správného řešení a ohodnocování jednotlivých tahů
    se stará třída master.

    V prvním kole se pro každý herní mód využije pevně danný tah. Ten by
    měl pro další kola vyloučit co nejvyšší množství "potencíálních" 
    řešení.

    Po ohodnocení prvního kola (zajišťuje master), jsou z množiny všech
    možných řešení dané úlohy vyloučeny ty nesprávné. Tedy ty, pro
    které by (pokud by byly hledaným řešením úlohy) nemohl naposledy
    hraný tah získat stejné ohodnocení, které dostal.

    Postup se opakuje, dokud není množina všech řešení dostatečně malá
    (moemntálně pod 1000 prvků). Zde přichází do hry výběr nejlepšího
    dalšího tahu. Za ten je považován tah, který je nejvíce podobný
    ostatním (má nejvyšší součetsoučtu vůči ostatním nejvyšší skóre).

    """
    def __init__(self):

        # Kódové označení 
        self.codename = "up to 32 characters"
        # Herní mód - obsahuje čísla 4 (4 ze 6), 5 (5 ze 7), 6 (6 z 8)
        self.game_mode = 0
        # Set s všemi možnými řešeními aktuální úlohy
        self.possibilities = set()
        # Jde o první tah?
        self.first_guess = True
        # Ohodnocení posledního pokusu o řešení
        self.last_score = 0
        # Cache vzájemného ohodnocení dvou možností
        self.cache = {}
        
 
    def init(self, numbers, positions):
        """
        Metoda volaná po každé změně obtížnosti (herního typu), aby se 
        nastavilo vše potřebné.

        Parametry:
        ----------
            numbers:integer
                Počet číslic, které mohou být na jedné pozici v rozsahu
                0... numbers-1
            
            positions:integer
                Počet pozic.
        """

        self.game_mode = positions
        self.possibilities = set(itertools.product(range(numbers), repeat=positions))
        self.first_guess = True
        self.cache = {}

    def pick_best_guess(self):
        """
        Metoda, jenž se pokusí o nalezení nejlepšího dalšího tahu.
        Protože je relativně pomalá (porovnává prvky v poli řešení
        každý s každým), měla by se volat až když je pole řešení
        menší.

        Vrací:
        ------
            set
                Nejlepší možný tah.
        """

        best = {}

        if len(self.possibilities) == 1:
            return self.possibilities.pop()

        # Kontroluje každý s každým
        for guess in self.possibilities:
            for compare in self.possibilities:

                # Samo se sebou neporovnává
                if guess == compare:
                    continue

                # Vytvoří počítadlo
                if not guess in best:
                    best[guess] = 0
                    
                # Přičte vzájemné skóre k počítadlu.
                best[guess] += self.get_score( guess, compare)

        # Vrátí tah s nejvyšším součtem všech skóre
        return max(best, key=lambda key: best[key])
                

    def count_matching_colors(self, a, b):
        """
        Spočítá počet stejných barev (na různých pozicích) v řešení a
        a b.

        Parametry:
        ---------
            a:set
                Řešení A
            
            b:set
                Řešení B

        Vrací:
        ------
            integer
                Počet stejných barev.
        """

        count = 0
        a_iterator = iter(sorted(a))
        b_iterator = iter(sorted(b))
        a_value = next(a_iterator)
        b_value = next(b_iterator)
        try:
            while True:
                if a_value == b_value:
                    count += 1
                    a_value = next(a_iterator)
                    b_value = next(b_iterator)
                elif a_value < b_value:
                    a_value = next(a_iterator)
                else:
                    b_value = next(b_iterator)
        except StopIteration:
            return count

    def get_score( self, guess, compare):
        """
        Metoda vracející vzájemné ohodnocení dvou možných řešení.

        Parametry:
        ----------
            guess:set
                Řešení A

            compare:set
                Řešení B
        """

        # Prohledávání cache, zda jsme to už nepočítali.
        # Bohužel mě nenapadlo jak vytvořit unikátní klíč
        # na základě parametrů guess a compare tak, aby
        # nezáleželo na jejich pořadí.
        # 
        # Memoize by asi moc nepomohlo...
        a = guess + compare 
        b = compare + guess
        if a in self.cache: 
            return self.cache[a]
        elif b in self.cache:
            return self.cache[b]

        # Výpočet ohodnocení
        key = a
        blacks = sum(1 for a, b in zip(guess, compare) if a == b)
        color_matches = self.count_matching_colors(guess, compare)
        whites = color_matches - blacks

        # Uložení do cache
        self.cache[key] = blacks * 10 + whites
        return blacks * 10 + whites
    
    def guess(self):

        guess = 0

        if self.first_guess:
            self.first_guess = False

            if self.game_mode == 4:
                guess = (0, 0, 1, 1)
            elif self.game_mode == 5:
                guess = (0, 0, 1, 1, 2)
            elif self.game_mode == 6:
                guess = (0, 0, 1, 1, 2, 2)

            self.possibilities.remove(guess)

        # Čas hledat nejlepší řešení
        # Neosvědčilo se
        """
        if len(self.possibilities) < 1000:
            guess = self.pick_best_guess()
        else:
        """
        guess = self.possibilities.pop()

        return guess

    def eval(self, guess, black, white):
        
        self.last_score = black * 10 + white
        
        # Promaže všechny možnosti, která nemohou být řešením
        self.possibilities = set(filter(
            lambda n: self.get_score(guess,n) == self.last_score, 
            self.possibilities
        ))