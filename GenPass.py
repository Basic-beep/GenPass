""" Welcome to
   ____            ____               
  / ___| ___ _ __ |  _ \ __ _ ___ ___ 
 | |  _ / _ \ '_ \| |_) / _` / __/ __|
 | |_| |  __/ | | |  __/ (_| \__ \__ \
  \____|\___|_| |_|_|   \__,_|___/___/

  Since you're here in the code, if you find any bugs or can think of improvements, DM me on Slack @Elliott Rose                                 
"""
import random
import string
types = ('Abject', 'Abandoned','Abdominal','Abhorrent','Abiding','Abject','Able','Able-Bodied','Abnormal','Abounding','Annoyed'
       ,'Babbling','Baby','Background','Backhanded','Bacterial','Basic','Bad-tempered','Baffled','Baffling','Bald','Balding'
       ,'Cackling','Caged','Cagey','Calculable','Calculated','Calculating','Callous','Calm','Calming','Camouflaged','Cancelled'
       ,'Daffy','Daft','Daily','Dainty','Damaged','Damaging','Damp','Dandy','Dangerous','Dapper'
       ,'Eager','Early','Earnest','Ear-piercing','Ear-splitting','Earthshaking','Earthy','Eastern','Eccentric','Edgy','Eerie'
       ,'Fabled','Fabulous','Facetitious','Factual','Faded','Fading','Failed','Fair','Faithful','Faithless'
       ,'Gallent','Gaping','Garbled','Gargantuan','Generous','Generic','Gay','Giant','Ghostly','Ghastly'
       ,'Hairy','Handsome','Harmful','Harmless','Hated','Hateful','Hazardous','Hack','Helpless','Horrid','Humid'
       ,'Icky','Ideal','Impolite','Inclusive','Incorruptable','Indestructible','Indirect','Inevitable','Infamous','Innocent','Imposing'
       ,'Jaded','Jealous','Jolly','Joyful','Joyless','Juicy','Jumpy','Juvenile','Jubilant','Jerky'
       ,'Kind','Knowledgeable','Kingly','Keen','Kaput','Kindhearted','Key','Knowing','Knobby','Knightly','Kindhearted'
       ,'Lacy','Lame','Large','Large','Larger','Largest','Last','Lasting','Later','Latest'
       ,'Macabre','Macho','Magic','Magical','Main','Magenta','Majestic','Mindful','Married','Massive'
       ,'Naive','Nameless','Narcissistic','Nasty','Native','Neat','Needless','Needy','Nervous'
       ,'Obese','Oafish','Oblong','Obscure','Obsolete','Odorless','Offbeat','Ominous','Opportunistic','Ornate'
       ,'Pale','Partial','Passive','Pathetic','Peaceful','Patriotic','Pensive','Perfect','Perky','Petty'
       ,'Quaint','Queasy','Quick','Quirky','Quiet','Quizzical','Questionable','Quickest','Quotable','Queer'
       ,'Radient','Rambunctious','Rampant','Rare','Raspy','Ratty','Raw','Real','Regal','Religious'
       ,'Sacred','Salty','Straight','Sandy','Sassy','Sarcastic','Satiric','Savage','Savvy','Scaly','Savory'
       ,'Taboo','Tame','Tanned','Tart','Tasty','Tearful','Tense','Terrific','Thick','Thrilled'
       ,'Ugly','Ultimate','Unafraid','Unattractive','Uncertain','Unappetizing','Unbreakable','Uncivil','Unclean','Uncommon'
       ,'Vain','Venomous','Verbose','Vulgar','Vulnerable','Vital','Visible','Vicious','Violet','Volatile'
       ,'Wacky','Wasted','Wasteful','Weak','Weary','Weird','Wet','Wicked','Witty','Wooden'
       ,'Yawning','Yearly','Yearning','Yellow','Yelping','Yielding','Young','Younger','Youngest','Yummy'
       ,'Zany','Zealous','Zesty','Zippy','Zestful')
art = ('A','That','The','An','Very')
thing = ('Aardvark','Abacus','Access','Acorn','Art','Accordion','Acre','Aglet','Airbag','Albatross'
        ,'Bathtub','Baseball','Bathhouse','Beach','Bean','Beech','Bellows','Bird','Blind','Bowl'
        ,'Cabin','Cake','Canoe','Cannon','Club','Card','Carpet','Cat','Cave','Chasm'
        ,'Deer','Deep','Dawn','Dog','Default','Demure','Denim','Demon','Design','Diabetes'
        ,'Ear','Ease','Edge','Eel','Eggplant','Eraser','Essay','Excerpt','Eyeball','Explosion'
        ,'Fabric','Father','Faucet','Favorite','Feather','Fiddle','Foxglove','Frog','Fruit','Fritter'
        ,'Gnome','Gadget','Gender','Genre','Glacier','Git','Gorilla','Governor','Gradient','Gopher'
        ,'Havoc','Heterosexual','Heron','Homosexual','Hearth','Helmet','Hyphenation','Human','Hummus','Hypothermia'
        ,'Ice','Ideal','Ignorant','Imagination','Immortal','Import','Impala','Impact','Impostor'
        ,'Jackal','Jaguar','Jazz','Jockey','Juggernaut','Joke','Joint','Jumpsuit','Jug','Joey'
        ,'Kale','Kidney','Kimono','Kitchen','Knee','Koala','Kingdom','King','Kitty','Kiosk'
        ,'Lab','Ladybug','Lesbian','Lamp','Lantern','Lawmaker','Lung','Lumberman','Lotion','Loophole'
        ,'Macaroon','Mammoth','Mango','Manatee','Mangrove','Mansion','Marble','Mayor','Meadow','Meat'
        ,'Nature','Neighbor','Neighbour','Neighborhood','Neighbourhood','Nephew','Nitrogen','Notebook','Nuke','Nutmeg'
        ,'Oasis','ocelot','Octagon','Octave','Opossum','Optimist','Ostrich','Otter','Oval','Oxygen'
        ,'Pacemaker','Pagoda','Pancreas','Panther','Pamphlet','Paragraph','Parent','Parsley','Parsnip','Pasta'
        ,'Quail','Queen','Quest','Quinoa','Quilt','Quiet','Quote','Quota','Quiche','Quiver'
        ,'Raft','Raffle','Raisin','Rally','Rambler','Refuge','Register','Reject','Researcher','Riddle'
        ,'Sage','Salmon','Sailor','Sail','Salami','Sandal','Scalp','Scarf','Scissors','Scheme'
        ,'Teen','Taco','Time','Toucan','Tarp','Tart','Tip','Theme','Thumb','Tick'
        ,'Umbrella','Universe','Uncle','Utensil','Unity','Undertaker','Union','Usher','Underpass','Unblinking'
        ,'Valley','Vein','Velvet','Veneer','Venti','Venue','Vet','Village','Vinegar','Virus'
        ,'Walrus','Walnut','Warlock','Waveform','Waterwheel','Webpage','Wetsuit','Wuss','Whirlpool','Wildebeest'
        ,'Yacht','Yak','Yahoo','Yarn','Yogurt','Yolk','Yoke','Youth','Youngster'
        ,'Zebra','Zebrafish','Zoo','Zoologist','Zucchini')
sym = ('!','@','#','$','^','&','*','(',')','-','_','+','=','`','~','<','>','?',';',':','.',',')
while True:
    adj = random.choice(types)
    open = random.choice(art)
    noun = random.choice(thing)
    chara = random.choice(sym)
    num = random.randrange(0,99)
    p = F"Your new GenPass password is: {open}{adj}{noun}{chara}{num}"
    print(p)
    Response = input('If you want a new Password, press anything for new. If you want to end the program, press "E" for End.')
    if Response == 'E':
        break
