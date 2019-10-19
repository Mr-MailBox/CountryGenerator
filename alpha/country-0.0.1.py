#country.py
#v0.0.1
#by github.com/33sixtynine

#imports
import random as rnd

#vowels
v = ['a', 'e', 'i', 'o', 'u']

#consonants
c = ['m', 'n', 'ng', 'ny', 'p', 'b', 't', 'd', 'k', 'g', 'q', "'", 'w', 'y', 'l', 'r', 'f', 'v', 'th', 'dh', 's', 'z', 'sh', 'zh',
    'x', 'gh', 'kh', 'h', 'ch', 'j', 'dzh']

#forms of government
g = ['Anarchist Territory', 'Voluntaryist Territory', 'Confederation', 'Federation', 'Democracy', 'Oligarchy', 'Dictatorship',
    'Monarchy', 'Absolute Monarchy', 'Constitutional Monarchy', 'Republic', 'Union of States', 'Theocracy', 'Corrupt Democracy',
    'Rebel State', 'Commune', 'Communist State', 'Socialist State', 'Libertarian Socialist State', 'Social Democratic State',
    'Libertarian State', 'Colony', 'Ex-Colony', 'Empire', 'Kingdom', 'Principality', 'Duchy', 'Vassal State', 'Dual Monarchy',
    'Fascist State', 'Corporatist State', 'Military Dictatorship', 'Clique', 'Technocracy', 'Beaurocracy', 'Liberal State',
    'Autocracy', 'Surveilance State', 'Minarchy', 'Presidential Republic', 'Parliamentary Republic']

#location types
l = ['on the coast', 'in the mountains', 'below sea level', 'on an island', 'on a chain of islands', 'in the desert', 'on a river',
    'on a peninsula', 'in a steppe', 'in a forest', 'in a jungle', 'on multiple continents', 'in a tundra', 'in a wasteland',
    'in a swamp', 'in a savannah', 'between larger countries', 'inside another country', 'on a plain', 'under the ocean',
    'in space', 'on another planet', 'on a lunar colony', 'in another dimension']

#influence types
i = ['super power', 'world power', 'regional power', 'hegemon', 'world leader', 'rump state', 'important state', 'rogue state',
    'isolationist state', 'unimportant state', 'influential state', 'uninfluential state', 'agressive state', 'warmongering state',
    'well known state', 'not well known state']

#economy types
e = ['developing', 'collapsing', 'growing', 'stagnant', 'tiny', 'small', 'medium', 'large', 'huge']

#number categories
n = ['hundred', 'thousand', 'million', 'billion']

#the main program function, called on launch
def main():

    #get a name
    name = nameGen().capitalize()

    #get a form of government
    gov = rnd.choice(g)
    gov = article(gov) + gov

    #get a location
    loc = rnd.choice(l)

    #rank its influence
    inf = rnd.choice(i)
    inf = article(inf) + inf

    #rank its economy
    eco = rnd.choice(e)
    eco = article(eco) + eco

    #set a land size (km)
    size = str(rnd.randrange(1, 500)) + 'km'

    #set a population
    pop = str(rnd.randrange(1, 100)) + ' ' + rnd.choice(n)

    #print description
    print(name + ' is ' + gov + ' located ' + loc + '. It is ' + inf + ' with ' + eco + ' economy. It has a land mass of ' + size
        + ' and a population of ' + pop + '.')

#generate a name
def nameGen():

    name = ''

    while name == '':

        num = rnd.randint(1, 5)

        for x in range(num):
            syl = sylGen()
            name = name + syl

    return name

#generate a syllable
def sylGen():

    t = rnd.randint(1, 6)

    syl = ''

    if t == 1: #VC
        syl = rnd.choice(v) + rnd.choice(c)

    if t == 2: #CV
        syl = rnd.choice(c) + rnd.choice(v)

    if t == 3: #VCV
        syl = rnd.choice(v) + rnd.choice(c) + rnd.choice(v)

    if t == 4: #CVC
        syl = rnd.choice(c) + rnd.choice(v) + rnd.choice(c)

    if t == 5: #V
        syl = rnd.choice(v)

    return syl

#generate the correct indefinite article
def article(word):

    if word[0] in v:

        return 'an '

    else:

        return 'a '

#program entry point
if __name__ == "__main__":

    main()
