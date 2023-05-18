from random import choice

def get_answer(category):
    animals = ['AKITA', 'ANGELFISH', 'ANTELOPE', 'ANTEATER', 'ALLIGATOR', 'ARMADILLO', 'ALBATROSS', 'AVOCET', 'AKBASH', 'AXOLOTL', 'ANT', 'BABOON', 'BISON', 'BONGO', 'BUFFALO', 'BALINESE', 'BURMESE', 'BARB', 'BULLFROG', 'BAT', 'BONOBO', 'BARRACUDA', 'BIRMAN', 'BOMBAY', 'BUTTERFLY', 'BEETLE', 'BULLDOG', 'BEAR', 'BIRD', 'BEAVER', 'BUDGERIGAR', 'BADGER', 'BOOBY', 'BOBCAT', 'BEAGLE', 'BARNACLE', 'BLOODHOUND', 'BANDICOOT', 'BINTURONG', 'CAPYBARA', 'CHICKEN', 'CRANE', 'COLLIE', 'CAT', 'CASSOWARY', 'COW', 'CUSCUS', 'CROCODILE', 'CRAB', 'CHIPMUNK', 'COCKROACH', 'CATERPILLAR', 'COATI', 'CARACAL', 'CUTTLEFISH', 'CHINCHILLA', 'CHINOOK', 'COYOTE', 'CAIMAN', 'CAMEL', 'CHIHUAHUA', 'CORAL', 'CHIMPANZEE', 'CICHLID', 'DACHSHUND', 'DINGO', 'DOLPHIN', 'DUCK', 'DRAGONFLY', 'DUGONG', 'DONKEY', 'DUNKER', 'DALMATIAN', 'DODO', 'DORMOUSE', 'DOG', 'DISCUS', 'DREVER', 'DEER', 'EARWIG', 'EMU', 'ECHIDNA', 'ELEPHANT', 
'EAGLE', 'FLOUNDER', 'FOX', 'FLAMINGO', 'FRIGATEBIRD', 'FISH', 'FOSSA', 'FALCON', 'FLY', 'FROG', 'GOPHER', 'GAR', 'GRASSHOPPER', 'GHARIAL', 'GOAT', 'GOOSE', 'GERBIL', 'GROUSE', 'GIRAFFE', 'GORILLA', 'GIBBON', 'GUPPY', 'GREYHOUND', 'GECKO', 'HIPPOPOTAMUS', 'HUMMINGBIRD', 'HARRIER', 'HAMSTER', 'HAVANESE', 'HERON', 'HORSE', 'HUMAN', 'HIMALAYAN', 'HARE', 'HYENA', 'IMPALA', 'INSECT', 'INDRI', 'IBIS', 'IGUANA', 'JELLYFISH', 'JAVANESE', 'JACKAL', 'JAGUAR', 'KINGFISHER', 'KOALA', 'KUDU', 'KAKAPO', 'KIWI', 'KANGAROO', 'LIZARD', 'LABRADOODLE', 'LEMUR', 'LLAMA', 'LION', 'LEMMING', 'LIONFISH', 'LIGER', 'LEOPARD', 'LOBSTER', 'MOUSE', 'MASTIFF', 'MONGOOSE', 'MOORHEN', 'MULE', 'MANDRILL', 'MONKEY', 'MOLE', 'MOOSE', 'MOTH', 'MONGREL', 'MOLLY', 'MARKHOR', 'MILLIPEDE', 'MANATEE', 'MEERKAT', 'MAYFLY', 'NUMBAT', 'NIGHTINGALE', 'NEWFOUNDLAND', 'NEANDERTHAL', 'NEWT', 'OTTER', 'OSTRICH', 'OKAPI', 'OCTOPUS', 'ORANG-UTAN', 'OYSTER', 'OCELOT', 'QUETZAL', 'QUOLL', 'QUOKKA', 'QUAIL', 'RACCOON', 'RABBIT', 'REINDEER', 'RATTLESNAKE', 'RAGDOLL', 'ROBIN', 'RAT', 'RHINOCEROS', 'SEAHORSE', 'SIAMESE', 'SIBERIAN', 'SCORPION', 'SEAL', 'SNAIL', 'SAOLA', 'SHRIMP', 'SALAMANDER', 'SNAKE', 'SLOTH', 'SHEEP', 
'SWAN', 'SKUNK', 'SERVAL', 'TUATARA', 'TARSIER', 'TIFFANY', 'TANG', 'TURKEY', 'TERMITE', 'TROPICBIRD', 'TOUCAN', 'TIGER', 'TETRA', 'TAPIR', 'TORTOISE', 'UMBRELLABIRD', 'UGUISU', 'UAKARI', 'VULTURE', 'WARTHOG', 'WILDEBEEST', 'WOMBAT', 'WHIPPET', 'WASP', 'WOODLOUSE', 'WALRUS', 'WOLF', 'WOLVERINE', 'WALLABY', 'WRASSE', 'WOODPECKER', 'YAK', 'ZEBRA', 'ZONKEY', 'ZORSE']

    countries = ['AFGHANISTAN', 'ALBANIA', 'ALGERIA', 'ANDORRA', 'ANGOLA', 'ARGENTINA', 'ARMENIA', 'AUSTRALIA', 'AUSTRIA', 'AZERBAIJAN', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM', 'BELIZE', 'BENIN', 'BHUTAN', 'BOLIVIA', 'BOTSWANA', 'BRAZIL', 'BRUNEI', 'BULGARIA', 'BURUNDI', 'CAMBODIA', 'CAMEROON', 'CANADA', 'CHAD', 'CHILE', 'CHINA', 'COLOMBIA', 'COMOROS', 'CROATIA', 'CUBA', 'CYPRUS', 'DENMARK', 'DJIBOUTI', 'DOMINICA', 'ECUADOR', 'EGYPT', 'ENGLAND', 'ERITREA', 'ESTONIA', 'ESWATINI', 'ETHIOPIA', 'FIJI', 'FINLAND', 'FRANCE', 'GABON', 'GEORGIA', 'GERMANY', 'GHANA', 'GREECE', 'GRENADA', 'GUATEMALA', 'GUINEA', 'GUYANA', 'HAITI', 'HONDURAS', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA', 'KIRIBATI', 'KOSOVO', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON', 'LESOTHO', 'LIBERIA', 'LIBYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI', 'MALTA', 'MAURITANIA', 'MAURITIUS', 'MEXICO', 'MOLDOVA', 'MONACO', 'MONGOLIA', 'MONTENEGRO', 'MOROCCO', 'MOZAMBIQUE', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NORWAY', 'OMAN', 'PAKISTAN', 'PALAU', 'PANAMA', 'PARAGUAY', 'PERU', 'PHILIPPINES', 'POLAND', 'PORTUGAL', 'QATAR', 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAMOA', 'SCOTLAND', 'SENEGAL', 'SERBIA', 'SEYCHELLES', 'SINGAPORE', 'SLOVAKIA', 'SLOVENIA', 'SOMALIA', 'SPAIN', 'SUDAN', 'SURINAME', 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN', 'TANZANIA', 'THAILAND', 'TOGO', 'TONGA', 'TUNISIA', 'TURKEY', 'TURKMENISTAN', 'TUVALU', 
'UGANDA', 'UKRAINE', 'USA', 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VATICAN', 'VENEZUELA', 'VIETNAM', 'YEMEN', 'ZAMBIA', 'ZIMBABWE']

    fruits = ['APPLE', 'AVOCADO', 'BANANA', 'BLUEBERRY', 'BLACKBERRY', 'CHERIMOYA', 'CHERRY', 'CRANBERRY', 'CUCUMBER', 'CURRANT', 'DURIAN', 'EGGPLANT', 'ELDERBERRY', 'GOOSEBERRY', 'GRAPE', 'GRAPEFRUIT', 'GUAVA', 'HUCKLEBERRY', 'KIWI', 'KUMQUAT', 'LEMON', 'LIME', 'MANGO', 'MANGOSTEEN', 'MULBERRY', 'MUSKMELON', 'NECTARINE', 'ORANGE', 'PAPAYA', 'PEACH', 'PERSIMMON', 'PINEAPPLE', 'PLUMS', 'PLUOT', 'POMEGRANATE', 'PEAR', 'QUINCE', 'RAMBUTON', 'RASPBERRY', 'STARFRUIT', 'SAPADILLA', 'STRAWBERRY', 'TAMARIND', 'TANGELO', 'TANGERINE', 'TOMATO', 'WATERMELON', 'ZUCCHINI']

    vegetables = ['ARTICHOKE', 'ARUGULA', 'ASPARAGUS', 'AVOCADO', 'BEAN', 'BEET', 'BROCCOLI', 'CABBAGE', 'CALABASH', 'CAPERS', 'CARROT', 'CAULIFLOWER', 'CELERY', 'CELTUCE', 'CHAYOTE', 'CUCUMBER', 'EDAMAME', 'ENDIVE', 'FENNEL', 'FIDDLEHEAD', 'GALANGAL', 'GARLIC', 'GINGER', 'HORSERADISH', 'JĂ\xadCAMA', 'KALE', 'KOHLRABI', 'LEEKS', 'LEMONGRASS', 'LETTUCE', 'NOPALES', 'OKRA', 'OLIVE', 'ONION', 'PARSLEY', 'PARSNIP', 'PEA', 'PEPPER', 'PLANTAIN', 'POTATO', 'PUMPKIN', 'PURSLANE', 'RADICCHIO', 'RADISH', 'RUTABAGA', 'SHALLOTS', 'SPINACH', 'TARO', 'TOMATILLO', 'TOMATO', 'TURNIP', 'WATERCRESS', 'YAMS', 'ZUCCHINI']

    if category.lower() == "animals":
        return choice(animals)
    elif category.lower() == "countries":
        return choice(countries)
    elif category.lower() == "fruits":
        return choice(fruits)
    elif category.lower() == "vegetables":
        return choice(vegetables)