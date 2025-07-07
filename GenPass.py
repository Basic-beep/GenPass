""" Welcome to
   ____            ____               
  / ___| ___ _ __ |  _ \ __ _ ___ ___ 
 | |  _ / _ \ '_ \| |_) / _` / __/ __|
 | |_| |  __/ | | |  __/ (_| \__ \__ \
  \____|\___|_| |_|_|   \__,_|___/___/

  Since you're here in the code, if you find any bugs or can think of improvements, DM me on Slack @Elliott Rose                                 
"""

import string
adj = ('Abject', 'Abandoned','Abdominal','Abhorrent','Abiding','Abject','Able','Able-Bodied','Abnormal','Abounding','Annoyed'
       ,'Babbling','Baby','Background','Backhanded','Bacterial','Bad','Bad-tempered','Baffled','Baffling','Bald','Balding'
       ,'Cackling','Caged','Cagey','Calculable','Calculated','Calculating','Callous','Calm','Calming','Camouflaged','Cancelled'
       ,'Daffy','Daft','Daily','Dainty','Damaged','Damaging','Damp','Dandy','Dangerous','Dapper'
       ,'Eager','Early','Earnest','Ear-piercing','Ear-splitting','Earthshaking','Earthy','Eastern','Eccentric','Edgy','Eerie'
       ,'Fabled','Fabulous','Facetitious','Factual','Faded','Fading','Failed','Fair','Faithful','Faithless'
       ,'Gallent','Gaping','Garbled','Gargantuan','Generous','Generic','Gaseous','Giant','Ghostly','Ghastly'
       ,'Hairy','Handsome','Harmful','Harmless','Hated','Hateful','Hazardous','Helpful','Helpless','Horrid','Humid'
       ,'Icky','Ideal','Impolite','Inclusive','Incorruptable','Indestructible','Indirect','Inevitable','Infamous','Innocent','Imposing'
       ,'Jaded','Jealous','Jolly','Joyful','Joyless','Juicy','Jumpy','Juvenile','Jubilant','Jerky'
       ,'Kind','Knowledgeable','Kingly','Keen','Kaput','Kindhearted','Key','Knowing','Knobby','Knightly','Kindhearted'
       ,'Lacy','Lame','Large','Large','Larger','Largest','Last','Lasting','Later','Latest','Lax'
       ,'Macabre','Macho','Magic','Magical','Main','Magenta','Majestic','Mandatory','Married','Massive'
       ,'Naive','Nameless','Narcissistic','Nasty','Native','Neat','Needless','Needy','Nervous','Nice'
       ,'Obese','Oafish','Oblong','Obscure','Obsolete','Odorless','Offbeat','Ominous','Opportunistic','Ornate'
       ,'Pale','Partial','Passive','Pathetic','Peaceful','Patriotic','Pensive','Perfect','Perky','Petty'
       ,'Quaint','Queasy','Quick','Quirky','Quiet','Quizzical','Questionable','Quickest','Quotable','Queer'
       ,'Radient','Rambunctious','Rampant','Rare','Raspy','Ratty','Raw','Real','Regal','Religious'
       ,'Sacred','Salty','Sane','Sandy','Sassy','Sarcastic','Satiric','Savage','Savvy','Scaly','Savory'
       ,'Taboo','Tame','Tanned','Tart','Tasty','Tearful','Tense','Terrific','Thick','Thrilled'
       ,'Ugly','Ultimate','Unafraid','Unattractive','Uncertain','Unappetizing','Unbreakable','Uncivil','Unclean','Uncommon'
       ,'Vain','Venomous','Verbose','Vulgar','Vulnerable','Vital','Visible','Vicious','Violet','Volatile'
       ,'Wacky','Wasted','Wasteful','Weak','Weary','Weird','Wet','Wicked','Witty','Wooden'
       ,'Yawning','Yearly','Yearning','Yellow','Yelping','Yielding','Young','Younger','Youngest','Yummy'
       ,'Zany','Zealous','Zesty','Zippy','Zestful')
art = ('A','That','The','An')
noun = ()


Response = input('Welcome to GenPass! ' 
'If you want a new Password press "N" for new. ' 
'If you want to see passwords you have saved this session press "S" for saved. ' 
'If you want to end the session press "E" for End.')
