import random as rand

isRandom = input('Randomize all? (y/n): ').lower()
randomizeAll = False
if isRandom == 'y':
    randomizeAll = True

def choose_concept(isRandom):
    print('\nChoose Concept')
    if not isRandom:
        random = input('Randomize concept? (y/n): ').lower()
        if random == 'y':
            isRandom = True
    if isRandom:
        concepts = ['Jailbird', 'Mafioso', 'Drug Dealer', 'Pimp', 'Carjacker', 'Thug', 'Thief', 'Fence', 
                    'Bum', 'Smuggler', 'Prositute', 'Junkie', 'Pilgrim', 'Biker', 'Gambler',
                    'Musician', 'film star', 'artist', 'club kid', 'model', 'web celebrity', 
                    'writer', 'student', 'scientist', 'philosopher', 'social critic',
                    'detective', 'beat cop', 'government agent', 'private eye', 'witch-hunter', 
                    'child', 'runaway', 'outcast', 'urch', 'gangbanger', 
                    'urban primitive', 'refugee', 'minortiy', 'conspiracy theorist', 'junkie',
                    'judge', 'public official', 'councilor', 'aide', 'speechwriter',
                    'engineer', 'doctor', 'programmer', 'lawyer', 'industrialist',
                    'journailst', 'blogger', 'paparazzo', 'talkshow host', 'media expert',
                    'clubgoer', 'goth', 'skinhead', 'punk', 'barfly', 'hipster', 'substance abuser',
                    'dilettante', 'host', 'playboy', 'sycophant', 'trophy wife',
                    'bodyguard', 'enforcer', 'soldier of fortune', 'killer-for-hire',
                    'trucker', 'farmer', 'wage earner', 'manser vant', 'construction laborer']
        concept = concepts[rand.randint(0, len(concepts) - 1)].lower()
        print('Your concept is', concept.uppercase())
    else:
        concept = input('Enter character concept: ').lower()
    return concept

def choose_clan(isRandom):
    clans = {'Assemite': 'The righteous chosen of a blood cult, the Assassins are masters of silent death and an arcane tradition of wisdom.',
                'Brujah': 'The Rabble are rebels and insurgents, fighting passionately for their disparate causes. The Brujah rage against tyranny — occasionally even their own.',
                'Follower of Set': 'Guardians of the world’s black- est secrets, the Serpents are feared for what they protect, and all too often seduced by it.',
                'Gangrel': 'The nomadic Outlanders are feral and wild. These solitary wanderers are the source of much of the lore that likens vampires to dark beasts.',
                'Giovanni': 'Insular and incestuous, the Necromancers ply their trade in blood, money, and the souls of the dead.',
                'Lasombra': 'The shadowy, wicked Keepers nomi- nally lead the Sabbat. Clan Lasombra serves itself first and its inner darkness second.',
                'Malkavian': 'Dangerously deranged, the Lunatics nonetheless possess uncanny insight.',
                'Nosferatu': 'Disfigured and skulking, the hideous Sewer Rats find themselves shunned by Kindred society, but gather secrets from the darkness that hides them.',
                'Ravnos': 'The Deceivers are adept with the craft of illusion and guile, and often come to embody the prejudices held against them.',
                'Toreador': 'Lovers of the sensuous and the aes- thetic, the Degenerates are trapped in the stagnancy of undeath.',
                'Tremere': 'A Clan of sorcerous blood magicians, the Warlocks are widely distrusted... and just as widely feared.',
                'Tzimisce': 'A Clan of fallen nobles from Eastern Europe, the brilliant but monstrous Fiends now serve the Sabbat.',
                'Ventrue': 'The reluctant aristocracy of the Kin- dred, the Blue Bloods atone for their damnation by en- forcing the Traditions and the Masquerade.',
                'Caitiff': 'Claiming no Clan at all, the Caitiff ex-hibit no common characteristics, and often find them- selves outcast by vampires of distinct pedigree'}
    print('\nChoose Clan')
    if not isRandom:
        random = input('Random clan? (y/n): ').tolower()
        if random == 'y':
            isRandom = True
    if isRandom:
        clan = list(clans.keys())[rand.randint(0, len(clans)-1)]
    else:   
        print('Pick one of the following clans:')
        print('Assemite, Brujah, Followers of Set, Gangrel, Giovanni, Malkavian, Nosferatu, Toreador, Tremere, Ventrue, Lasombra, Tzimisce, Ravnos, Caitiff')
        clan = input('Enter character clan: ').uppercase()
    print()
    print(clan)
    print('\n' + clans[clan])
    return clan

def choose_nature_and_demeanor(isRandom):
    print('\nChoose Nature and Demeanor')
    personalities = {'Architect': 'You build something of lasting value. ', 'Autocrat': 'You need control. ', 'Bon Vivant': 'Unlife is for pleasure. ', 'Bravo': 'Might makes right. ', 'Capitalist': 'Why give it away for free when you can sell it? ', 'Caregiver': 'Everyone needs nurturing. ', 'Celebrant': 'Your cause brings you joy. ', 'Chameleon': 'You manage to blend into any situ- ation. ', 'Child': 'Won’t somebody be there for you? ', 'Competitor': 'You must be the best. ', 'Conformist': 'You follow and assist. ', 'Conniver': 'Others exist for your benefit. ', 'Creep Show': 'Disgusting the straights makes you smile. ', 'Curmudgeon': 'Everything has its flaws. ', 'Dabbler': 'It’s always about the next big thing. ', 'Deviant': 'The status quo is for sheep. ', 'Director': 'You oversee what must be done. ', 'Enigma': 'Just when people think they’ve figured you out, you change the game. ', 'Eye of the Storm': 'Chaos and havoc follow you, but it never gets to you. ', 'Fanatic': 'The cause is all that matters. ', 'Gallant': 'You’re not the showstopper: you’re the show! ', 'Guru': 'People find you spiritually compelling. ', 'Idealist': 'You believe in something greater. ', 'Judge': 'Your judgment will improve things. ', 'Loner': 'You make your own way. ', 'Martyr': 'You suffer for the greater good. ', 'Masochist': 'Pain reminds you that you still exist. ', 'Monster': 'You’re Damned, so act like it! ', 'Pedagogue': 'You save others through knowledge. ', 'Penitent': 'Unlife is a curse, and you must atone for it. ', 'Perfectionist': 'You strive for an unattainable goal. ', 'Rebel': 'You follow no one’s rules. ', 'Rogue': 'It’s all about you. ', 'Sadist': 'You live to cause pain. ', 'Scientist': 'Everything is a puzzle to solve. ', 'Sociopath': 'The inferior must be destroyed. ', 'Soldier': 'You follow orders, but in your own way. ', 'Survivor': 'Nothing can keep you down. ', 'Thrill-Seeker': 'The rush is all that matters. ', 'Traditionalist': 'As it has always been, so it must be. ', 'Trickster': 'Laughter dims the pain. ', 'Visionary': 'Something exists beyond all this. '}
    if not isRandom:
        random = input('Random nature and demeanor? (y/n): ').tolower()
        if random == 'y':
            isRandom = True
    if isRandom:
        nature = list(personalities.keys())[rand.randint(0, len(personalities))].lower()
        demeanor = list(personalities.keys())[rand.randint(0, len(personalities))].lower()
    else:
        print('Pick one of the following nature and demeanor:')
        print('Architect, Autocrat, Bon Vivant, Bravo, Capitalist, Caregiver, Celebrant\nChameleon, Child, Competitor, Conformist, Conniver, Creep Show\nCurmudgeon, Dabbler, Deviant, Director, Enigma, Eye of the Storm\nFanatic, Gallant, Guru, Idealist, Judge, Loner, Martyr, Masochist\nMonster, Pedagogue, Penitent, Perfectionist, Rebel, Rogue, Sadist, Scientist\nSociopath, Soldier, Survivor, Thrill-Seeker, Traditionalist, Trickster, Visionary')
        nature = input('Enter character nature: ').lower()
        demeanor = input('Enter character demeanor: ').lower()
    print()
    print('Your nature is ' + nature + ' and your demeanor is ' + demeanor)
    print(nature, ':', personalities[nature])
    print()
    print(demeanor, ':', personalities[demeanor])
    return nature, demeanor

def choose_attributes(isRandom):
    print('\nChoose Attributes')
    points = [7, 5, 3]
    attributes = {'Physical': {'Strength': 1, 'Dexterity': 1, 'Stamina': 1}, 'Social': {'Charisma': 1, 'Manipulation': 1, 'Appearance': 1}, 'Mental': {'Perception': 1, 'Intelligence': 1, 'Wits': 1}}
    if not isRandom:
        random = input('Random attributes? (y/n): ').tolower()
        if random == 'y':
            isRandom = True
    if isRandom:
        for i in range(3):
            index = rand.randint(0, len(points) - 1)
            while points[index] == 0:
                index = rand.randint(0, len(points) - 1)
            avaliable_points = points[index]
            points[index] = 0
            for j in range(avaliable_points):
                attribute = list(attributes.keys())[i][rand.randint(0,  2)]
                attributes[list(attributes.keys())[i]][attribute] += 1
        print('                  Attributes')
        for i in range(3):
            print(list(attributes.keys())[i])
            print(list(attributes.keys())[i][0], ':', attributes[list(attributes.keys())[i]][list(attributes.keys())[i][0]], ' ', list(attributes.keys())[i][1], ':', attributes[list(attributes.keys())[i]][list(attributes.keys())[i][1]], ' ', list(attributes.keys())[i][2], ':', attributes[list(attributes.keys())[i]][list(attributes.keys())[i][2]])
    else:
        print('Prioritize the three categories: Physical, Social, Mental (7/5/3). Your character automatically has one dot in each Attribute.')
        avaliable_points = [-1, -1, -1]
        print('Choose 7, 5, or 3 points for Physical, Social, and Mental: ')
        physical_points = int(input('Physical: '))
        while physical_points not in avaliable_points and physical_points not in points:
            print('Invalid input.')
            physical_points = int(input('Physical: '))
        avaliable_points[0] = physical_points
        social_points = int(input('Social: '))
        while social_points not in avaliable_points and social_points not in points:
            print('Invalid input.')
            social_points = int(input('Social: '))
        avaliable_points[1] = social_points
        mental_points = int(input('Mental: '))
        while mental_points not in avaliable_points and mental_points not in points:
            print('Invalid input.')
            mental_points = int(input('Mental: '))
        avaliable_points[2] = mental_points
        for i in range(3):
            for j in range(avaliable_points[i]):
                choice = int(input('Type 0 for ' + list(attributes.keys())[i][0] + ' or 1 for ' + list(attributes.keys())[i][1] + ' or 2 for ' + list(attributes.keys())[i][2]))
                if choice == 0:
                    attributes[list(attributes.keys())[i]][list(attributes.keys())[i][0]] += 1
                elif choice == 1:
                    attributes[list(attributes.keys())[i]][list(attributes.keys())[i][1]] += 1
                elif choice == 2:
                    attributes[list(attributes.keys())[i]][list(attributes.keys())[i][2]] += 1
                else:
                    print('Invalid input.')
                    j -= 1
    print()
    print('              Attributes')
    for i in range(3):
        print(list(attributes.keys())[i])
        print(list(attributes.keys())[i][0], ':', attributes[list(attributes.keys())[i]][list(attributes.keys())[i][0]], ' ', list(attributes.keys())[i][1], ':', attributes[list(attributes.keys())[i]][list(attributes.keys())[i][1]], ' ', list(attributes.keys())[i][2], ':', attributes[list(attributes.keys())[i]][list(attributes.keys())[i][2]])
    return attributes