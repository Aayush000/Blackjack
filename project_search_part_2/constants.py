import json
import re
import requests

ADVANCED = \
  "Any advanced searches?\n" \
  "1. Article title length\n" \
  "2. Number of articles\n" \
  "3. Get one random article\n" \
  "4. Check whether favorite author in list\n" \
  "5. Titles and authors only\n" \
  "6. Multiple keywords\n" \
  "7. None\n" \
  "Please enter a number corresponding to which advanced search you would like to perform: "

ADVANCED_TO_QUESTION = {
  1: "What's the max article title length (in number of characters) you're looking for? ",
  2: "What's the max number of articles you would like? ",
  3: "Please provide a random number to get a random article: ",
  4: "Who's your favorite author? ",
  5: "",
  6: "What's the other keyword you would like to search for? ",
  7: ""
}

BASIC = "What are you searching for? "

WIKI_API = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&pageids={}&formatversion=2&explaintext=1"

# List of random Wikipedia page IDs
ARTICLES = [
  {
    "title": "List of Canadian musicians",
    "contributor_username": "Bearcat",
    "id": "102873",
    "timestamp": "1181623340",
    "num_characters": "21023"
  },
  {
    "title": "French pop music",
    "contributor_username": "Brandon",
    "id": "6180884",
    "timestamp": "1172208041",
    "num_characters": "5569"
  },
  {
    "title": "Edogawa, Tokyo",
    "contributor_username": "Ciphers",
    "id": "335972",
    "timestamp": "1222607041",
    "num_characters": "4526"
  },
  {
    "title": "Noise (music)",
    "contributor_username": "Epbr123",
    "id": "87595",
    "timestamp": "1194207604",
    "num_characters": "15641"
  },
  {
    "title": "1922 in music",
    "contributor_username": "Jafeluv",
    "id": "163737",
    "timestamp": "1242717698",
    "num_characters": "11576"
  },
  {
    "title": "Ken Kennedy (computer scientist)",
    "contributor_username": "Jlalbee",
    "id": "9416375",
    "timestamp": "1246308670",
    "num_characters": "4144"
  },
  {
    "title": "1986 in music",
    "contributor_username": "Michael",
    "id": "160792",
    "timestamp": "1048918054",
    "num_characters": "6632"
  },
  {
    "title": "Spain national beach soccer team",
    "contributor_username": "Pegship",
    "id": "15103011",
    "timestamp": "1233458894",
    "num_characters": "1526"
  },
  {
    "title": "Kevin Cadogan",
    "contributor_username": "Renesis",
    "id": "1570956",
    "timestamp": "1144136316",
    "num_characters": "3917"
  },
  {
    "title": "Endogenous cannabinoid",
    "contributor_username": "RussBot",
    "id": "8016606",
    "timestamp": "1168971903",
    "num_characters": "26"
  },
  {
    "title": "2009 in music",
    "contributor_username": "SE KinG",
    "id": "18696414",
    "timestamp": "1235133583",
    "num_characters": "69451"
  },
  {
    "title": "Rock music",
    "contributor_username": "Sabrebd",
    "id": "25423",
    "timestamp": "1258069053",
    "num_characters": "119498"
  },
  {
    "title": "Medical value travel",
    "contributor_username": "Argon233",
    "id": "3189956",
    "timestamp": "1153157342",
    "num_characters": "4149"
  },
  {
    "title": "Lights (musician)",
    "contributor_username": "Espo3699",
    "id": "15801404",
    "timestamp": "1213914297",
    "num_characters": "5898"
  },
  {
    "title": "List of soul musicians",
    "contributor_username": "Ghmyrtle",
    "id": "170098",
    "timestamp": "1175455921",
    "num_characters": "4878"
  },
  {
    "title": "Human computer",
    "contributor_username": "Giftlite",
    "id": "3833695",
    "timestamp": "1248275178",
    "num_characters": "4750"
  },
  {
    "title": "Aube (musician)",
    "contributor_username": "Nihonjoe",
    "id": "2258925",
    "timestamp": "1145410600",
    "num_characters": "3152"
  },
  {
    "title": "List of overtone musicians",
    "contributor_username": "Sborsody",
    "id": "10759510",
    "timestamp": "1176928050",
    "num_characters": "2299"
  },
  {
    "title": "Black dog (ghost)",
    "contributor_username": "SmackBot",
    "id": "7137314",
    "timestamp": "1220471117",
    "num_characters": "14746"
  },
  {
    "title": "USC Trojans volleyball",
    "contributor_username": "Smuckers",
    "id": "5769756",
    "timestamp": "1218049435",
    "num_characters": "5525"
  },
  {
    "title": "Tim Arnold (musician)",
    "contributor_username": "Sohohobo",
    "id": "11484209",
    "timestamp": "1181480380",
    "num_characters": "4551"
  },
  {
    "title": "2007 Bulldogs RLFC season",
    "contributor_username": "Timmah86",
    "id": "7916044",
    "timestamp": "1177410119",
    "num_characters": "11116"
  },
  {
    "title": "Peter Brown (music industry)",
    "contributor_username": "Zephyrad",
    "id": "5777260",
    "timestamp": "1240235639",
    "num_characters": "2837"
  },
  {
    "title": "Mexican dog-faced bat",
    "contributor_username": "AnomieBOT",
    "id": "24555375",
    "timestamp": "1255316429",
    "num_characters": "1138"
  },
  {
    "title": "Embryo drawing",
    "contributor_username": "AxelBoldt",
    "id": "10273",
    "timestamp": "1034459202",
    "num_characters": "1712"
  },
  {
    "title": "Old-time music",
    "contributor_username": "Badagnani",
    "id": "479513",
    "timestamp": "1124771619",
    "num_characters": "12755"
  },
  {
    "title": "Arabic music",
    "contributor_username": "Badagnani",
    "id": "251740",
    "timestamp": "1209417864",
    "num_characters": "25114"
  },
  {
    "title": "C Sharp (programming language)",
    "contributor_username": "Eaglizard",
    "id": "2356196",
    "timestamp": "1232492672",
    "num_characters": "52364"
  },
  {
    "title": "List of Saturday Night Live musical sketches",
    "contributor_username": "Gary King",
    "id": "3181362",
    "timestamp": "1134966249",
    "num_characters": "13287"
  },
  {
    "title": "Joe Becker (musician)",
    "contributor_username": "Gary King",
    "id": "12255566",
    "timestamp": "1203234507",
    "num_characters": "5842"
  },
  {
    "title": "Will Johnson (soccer)",
    "contributor_username": "Mayumashu",
    "id": "3964439",
    "timestamp": "1218489712",
    "num_characters": "3562"
  },
  {
    "title": "Aco (musician)",
    "contributor_username": "Noodleboy",
    "id": "1018822",
    "timestamp": "1132546632",
    "num_characters": "3129"
  },
  {
    "title": "Geoff Smith (British musician)",
    "contributor_username": "Richardrj",
    "id": "4306585",
    "timestamp": "1194687509",
    "num_characters": "2043"
  },
  {
    "title": "Fiskerton, Lincolnshire",
    "contributor_username": "Snigbrook",
    "id": "4744436",
    "timestamp": "1259869948",
    "num_characters": "5853"
  },
  {
    "title": "Reflection-oriented programming",
    "contributor_username": "Soumyasch",
    "id": "4520792",
    "timestamp": "1143366937",
    "num_characters": "38"
  },
  {
    "title": "B (programming language)",
    "contributor_username": "Uvaphdman",
    "id": "4475",
    "timestamp": "1196622610",
    "num_characters": "5482"
  },
  {
    "title": "Richard Wright (musician)",
    "contributor_username": "Bdubiscool",
    "id": "19332171",
    "timestamp": "1189536295",
    "num_characters": "16185"
  },
  {
    "title": "Voice classification in non-classical music",
    "contributor_username": "Iridescent",
    "id": "14597488",
    "timestamp": "1198092852",
    "num_characters": "11280"
  },
  {
    "title": "Dalmatian (dog)",
    "contributor_username": "J. Spencer",
    "id": "19255892",
    "timestamp": "1207793294",
    "num_characters": "26582"
  },
  {
    "title": "1936 in music",
    "contributor_username": "JohnRogers",
    "id": "163570",
    "timestamp": "1243745950",
    "num_characters": "23417"
  },
  {
    "title": "Guide dog",
    "contributor_username": "Sarranduin",
    "id": "76885",
    "timestamp": "1165601603",
    "num_characters": "7339"
  },
  {
    "title": "1962 in country music",
    "contributor_username": "Briguy52748",
    "id": "2068000",
    "timestamp": "1249862464",
    "num_characters": "7954"
  },
  {
    "title": "List of dystopian music, TV programs, and games",
    "contributor_username": "Notinasnaid",
    "id": "1899265",
    "timestamp": "1165317338",
    "num_characters": "13458"
  },
  {
    "title": "Steven Cohen (soccer)",
    "contributor_username": "Scouselad10",
    "id": "5317001",
    "timestamp": "1237669593",
    "num_characters": "2117"
  },
  {
    "title": "Steve Perry (musician)",
    "contributor_username": "Woohookitty",
    "id": "1010610",
    "timestamp": "1254812045",
    "num_characters": "22204"
  },
  {
    "title": "2009 Louisiana Tech Bulldogs football team",
    "contributor_username": "AllisonFoley",
    "id": "23281761",
    "timestamp": "1245796406",
    "num_characters": "22410"
  },
  {
    "title": "David Gray (musician)",
    "contributor_username": "RattleandHum",
    "id": "876542",
    "timestamp": "1159841492",
    "num_characters": "7203"
  },
  {
    "title": "Craig Martin (soccer)",
    "contributor_username": "Darius Dhlomo",
    "id": "10118827",
    "timestamp": "1174203493",
    "num_characters": "709"
  },
  {
    "title": "Georgia Bulldogs football",
    "contributor_username": "Davidscharoun",
    "id": "2517159",
    "timestamp": "1166567889",
    "num_characters": "43718"
  },
  {
    "title": "Time travel",
    "contributor_username": "Thug outlaw69",
    "id": "31591",
    "timestamp": "1140826049",
    "num_characters": "35170"
  },
  {
    "title": "Fisk University",
    "contributor_username": "NerdyScienceDude",
    "id": "189946",
    "timestamp": "1263393671",
    "num_characters": "16246"
  },
  {
    "title": "Annie (musical)",
    "contributor_username": "Piano non troppo",
    "id": "357505",
    "timestamp": "1223619626",
    "num_characters": "27558"
  },
  {
    "title": "Alex Turner (musician)",
    "contributor_username": "CambridgeBayWeather",
    "id": "3003683",
    "timestamp": "1187010135",
    "num_characters": "9718"
  },
  {
    "title": "Python (programming language)",
    "contributor_username": "Lulu of the Lotus-Eaters",
    "id": "23862",
    "timestamp": "1137530195",
    "num_characters": "41571"
  },
  {
    "title": "List of gospel musicians",
    "contributor_username": "Absolon",
    "id": "179191",
    "timestamp": "1197658845",
    "num_characters": "3805"
  },
  {
    "title": "Tom Hooper (musician)",
    "contributor_username": "Bearcat",
    "id": "1283174",
    "timestamp": "1204967541",
    "num_characters": "1441"
  },
  {
    "title": "Endoglin",
    "contributor_username": "DOI bot",
    "id": "6732448",
    "timestamp": "1212259031",
    "num_characters": "6778"
  },
  {
    "title": "Indian classical music",
    "contributor_username": "Davydog",
    "id": "223014",
    "timestamp": "1222543238",
    "num_characters": "9503"
  },
  {
    "title": "Sun dog",
    "contributor_username": "Hellbus",
    "id": "323221",
    "timestamp": "1208969289",
    "num_characters": "18050"
  },
  {
    "title": "1996 in music",
    "contributor_username": "Kharker",
    "id": "160807",
    "timestamp": "1148585201",
    "num_characters": "21688"
  },
  {
    "title": "Lua (programming language)",
    "contributor_username": "Makkuro",
    "id": "46150",
    "timestamp": "1113957128",
    "num_characters": "0"
  },
  {
    "title": "Single-board computer",
    "contributor_username": "Nathael",
    "id": "194424",
    "timestamp": "1220260601",
    "num_characters": "8271"
  },
  {
    "title": "Mets de Guaynabo (volleyball)",
    "contributor_username": "Osplace",
    "id": "21895213",
    "timestamp": "1239156764",
    "num_characters": "2091"
  },
  {
    "title": "United States men's national soccer team 2009 results",
    "contributor_username": "Rebajc3",
    "id": "24259281",
    "timestamp": "1252384026",
    "num_characters": "79089"
  },
  {
    "title": "Joseph Williams (musician)",
    "contributor_username": "RussBot",
    "id": "3439709",
    "timestamp": "1140752684",
    "num_characters": "4253"
  },
  {
    "title": "The Hunchback of Notre Dame (musical)",
    "contributor_username": "RussBot",
    "id": "10251273",
    "timestamp": "1192176615",
    "num_characters": "42"
  },
  {
    "title": "China national soccer team",
    "contributor_username": "Seedbot",
    "id": "12231335",
    "timestamp": "1199103839",
    "num_characters": "45"
  },
  {
    "title": "Covariance and contravariance (computer science)",
    "contributor_username": "Wakapop",
    "id": "1104704",
    "timestamp": "1167547364",
    "num_characters": "7453"
  },
  {
    "title": "English folk music (1500–1899)",
    "contributor_username": "Ashley Y",
    "id": "1138211",
    "timestamp": "1177634764",
    "num_characters": "2073"
  },
  {
    "title": "Personal computer",
    "contributor_username": "Darklock",
    "id": "18457137",
    "timestamp": "1220391790",
    "num_characters": "45663"
  },
  {
    "title": "The Mandogs",
    "contributor_username": "DerHexer",
    "id": "12746175",
    "timestamp": "1205282029",
    "num_characters": "3968"
  },
  {
    "title": "David Levi (musician)",
    "contributor_username": "DumZiBoT",
    "id": "9659487",
    "timestamp": "1212260237",
    "num_characters": "3949"
  },
  {
    "title": "Scores (computer virus)",
    "contributor_username": "LilHelpa",
    "id": "7970552",
    "timestamp": "1235850703",
    "num_characters": "2706"
  },
  {
    "title": "Digital photography",
    "contributor_username": "Mintleaf",
    "id": "3616597",
    "timestamp": "1095727840",
    "num_characters": "18093"
  },
  {
    "title": "George Crum (musician)",
    "contributor_username": "SmackBot",
    "id": "13703703",
    "timestamp": "1252996687",
    "num_characters": "3848"
  },
  {
    "title": "Solver (computer science)",
    "contributor_username": "SmackBot",
    "id": "19125134",
    "timestamp": "1253282654",
    "num_characters": "1861"
  },
  {
    "title": "Georgia Bulldogs football under Robert Winston",
    "contributor_username": "Tlmclain",
    "id": "8422002",
    "timestamp": "1166046122",
    "num_characters": "1989"
  },
  {
    "title": "Wildlife photography",
    "contributor_username": "Zargulon",
    "id": "3957571",
    "timestamp": "1165248747",
    "num_characters": "1410"
  },
  {
    "title": "Traditional Thai musical instruments",
    "contributor_username": "Badagnani",
    "id": "13619511",
    "timestamp": "1191830919",
    "num_characters": "6775"
  },
  {
    "title": "Landseer (dog)",
    "contributor_username": "Birdgirl5",
    "id": "1379724",
    "timestamp": "1231438650",
    "num_characters": "2006"
  },
  {
    "title": "Charles McPherson (musician)",
    "contributor_username": "Cosprings",
    "id": "11095669",
    "timestamp": "1255183865",
    "num_characters": "3007"
  },
  {
    "title": "Comparison of programming languages (basic instructions)",
    "contributor_username": "IanOsgood",
    "id": "14513019",
    "timestamp": "1238781354",
    "num_characters": "61644"
  },
  {
    "title": "Les Cousins (music club)",
    "contributor_username": "Rodparkes",
    "id": "7691512",
    "timestamp": "1187072433",
    "num_characters": "4926"
  },
  {
    "title": "Paul Carr (musician)",
    "contributor_username": "Snalwibma",
    "id": "18516531",
    "timestamp": "1254142018",
    "num_characters": "5716"
  },
  {
    "title": "2006 in music",
    "contributor_username": "Suduser85",
    "id": "1570433",
    "timestamp": "1171547747",
    "num_characters": "105280"
  },
  {
    "title": "Spawning (computer gaming)",
    "contributor_username": "Vendettax",
    "id": "1196080",
    "timestamp": "1176750529",
    "num_characters": "3413"
  },
  {
    "title": "Sean Delaney (musician)",
    "contributor_username": "Bestcellar",
    "id": "16023479",
    "timestamp": "1204328174",
    "num_characters": "5638"
  },
  {
    "title": "Tony Kaye (musician)",
    "contributor_username": "Bondegezou",
    "id": "447066",
    "timestamp": "1141489894",
    "num_characters": "8419"
  },
  {
    "title": "Danja (musician)",
    "contributor_username": "Crusoe8181",
    "id": "7549507",
    "timestamp": "1257155543",
    "num_characters": "6925"
  },
  {
    "title": "Ruby (programming language)",
    "contributor_username": "Hervegirod",
    "id": "25768",
    "timestamp": "1193928035",
    "num_characters": "30284"
  },
  {
    "title": "Texture (music)",
    "contributor_username": "J Lorraine",
    "id": "410850",
    "timestamp": "1161070178",
    "num_characters": "3626"
  },
  {
    "title": "List of computer role-playing games",
    "contributor_username": "Lllockwood",
    "id": "6217026",
    "timestamp": "1179441080",
    "num_characters": "43088"
  },
  {
    "title": "Register (music)",
    "contributor_username": "Hyacinth",
    "id": "612508",
    "timestamp": "1082665179",
    "num_characters": "598"
  },
  {
    "title": "Mode (computer interface)",
    "contributor_username": "Donreed",
    "id": "2311336",
    "timestamp": "1182732608",
    "num_characters": "2991"
  },
  {
    "title": "2007 in music",
    "contributor_username": "Squilly",
    "id": "6459333",
    "timestamp": "1169248845",
    "num_characters": "45652"
  },
  {
    "title": "List of video games with time travel",
    "contributor_username": "Rockfang",
    "id": "21437409",
    "timestamp": "1234110556",
    "num_characters": "2344"
  },
  {
    "title": "2008 in music",
    "contributor_username": "Ba11innnn",
    "id": "8785767",
    "timestamp": "1217641857",
    "num_characters": "107605"
  },
  {
    "title": "Semaphore (programming)",
    "contributor_username": "Edcolins",
    "id": "164557",
    "timestamp": "1144850850",
    "num_characters": "7616"
  },
  {
    "title": "Wake Forest Demon Deacons men's soccer",
    "contributor_username": "Rebajc3",
    "id": "25057749",
    "timestamp": "1260577388",
    "num_characters": "26745"
  }
]

METADATA = [['List of Canadian musicians', 'Bearcat', 1181623340, 21023, ['canadian', 'canada', 'lee', 'jazz', 'and', 'rock', 'singer', 'songwriter', 'also', 'known', 'hip', 'hop', 'musician', 'folk', 'pop', 'composer', 'drummer', 'player', 'rapper', 'john', 'don', 'guitarist', 'the', 'andrew', 'country', 'indie', 'charlie', 'alternative', 'paul', 'matt', 'james', 'blues', 'bassist', 'cellist', 'pianist', 'artist', 'marie', 'dance', 'winner', 'idol', 'mike', 'keyboardist', 'jason', 'music', 'tim', 'kim', 'soprano', 'kevin', 'martin', 'violinist', 'dan', 'blue', 'new', 'daniel', 'producer', 'punk', 'conductor', 'gospel', 'dave', 'big', 'band', 'george', 'brian', 'bill', 'classical', 'david', 'operatic', 'michael', 'film', 'jon', 'soul', 'billy', 'record', 'jim', 'member', 'broken', 'social', 'scene', 'musical', 'theatre', 'actress', 'actor', 'peter', 'ian', 'electronic', 'rhythm', 'taylor', 'vocalist', 'jesse', 'radio', 'personality', 'for', 'andy', 'former', 'solo', 'chris', 'ryan', 'mark', 'scott', 'kate', 'multi', 'formerly', 'mother', 'instrumentalist', 'johnson', 'white', 'smith']], ['French pop music', 'Brandon', 1172208041, 5569, ['french', 'pop', 'music', 'the', 'france', 'and', 'radio']], ['Edogawa, Tokyo', 'Ciphers', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']], ['Noise (music)', 'Epbr123', 1194207604, 15641, ['noise', 'music', 'that', 'the', 'use', 'musical', 'this', 'made', 'and', 'sound', 'based', 'some', 'can', 'instruments', 'may', 'machine', 'sounds', 'audio', 'recordings', 'recording', 'other', 'produced', 'electronic', 'such', 'also', 'more', 'with', 'art', 'was', 'for', 'aesthetic', 'example', 'being', 'fluxus', 'artists', 'composition', 'early', 'young', 'rock', 'wave', 'industrial', 'works', 'his', 'from', 'one', 'not', 'signal', 'what', 'any', 'have', 'time', 'like', 'paul', 'hegarty', 'work', 'these', 'john', 'cage', 'which', 'all', 'japanese', 'genre', 'but', 'russolo', 'used', 'white', 'same', 'track', 'artist', 'first', 'had', 'found', 'called', 'created', 'paris', 'sirens', 'piece', 'using', 'percussion', 'tape', 'musique', 'concrète', 'group', 'recorded', 'various', '1960', 'album', 'cassette', 'ubuweb', 'com', 'ubu']], ['1922 in music', 'Jafeluv', 1242717698, 11576, ['music', 'the', '1922', 'january', 'first', 'may', 'orchestra', 'radio', 'october', 'and', 'for', 'paul', 'walter', 'george', 'billy', 'harry', 'you', 'march', 'april', 'production', 'opened', 'theatre', 'september', 'ran', 'performances', 'august', 'american', 'singer', 'actress', 'composer', 'june']], ['Ken Kennedy (computer scientist)', 'Jlalbee', 1246308670, 4144, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']], ['1986 in music', 'Michael', 1048918054, 6632, ['music', 'the', '1986', 'british', 'jazz', 'january', 'and', 'february', 'for', 'record', 'artist', 'may', 'june', 'september', 'october', 'november', 'december', 'musical', 'march', 'april', 'july', 'flute', 'opera', 'london', 'korean', 'singer', 'actor', 'american', 'english', 'guitarist', 'australian', 'musician', 'songwriter', 'composer', 'actress', 'producer', 'dancer']], ['Spain national beach soccer team', 'Pegship', 1233458894, 1526, ['beach', 'soccer', 'fifa']], ['Kevin Cadogan', 'Renesis', 1144136316, 3917, ['cadogan', 'record', 'and', 'the', 'band', 'third', 'eye', 'blind', 'with', 'from', 'their', 'album', 'his', 'jenkins', 'recording', 'elektra', 'records', 'was', 'for', 'california', 'two', 'music', 'that', 'have', 'were']], ['Endogenous cannabinoid', 'RussBot', 1168971903, 26, []], ['2009 in music', 'SE KinG', 1235133583, 69451, ['this', 'and', '2009', 'music', 'american', 'british', 'canadian', 'new', 'rock', 'pop', 'jazz', 'january', 'lady', 'gaga', 'debut', 'single', 'just', 'dance', 'hit', 'number', 'one', 'the', 'billboard', 'hot', '100', 'after', 'weeks', 'second', 'since', 'with', 'november', 'also', 'singles', 'chart', 'three', 'week', 'february', 'day', 'out', 'festival', 'takes', 'place', 'are', 'all', 'concert', 'held', 'beyoncé', 'shakira', 'taylor', 'songs', 'performed', 'had', 'album', 'including', 'jay', 'for', 'kelly', 'clarkson', 'record', 'her', 'life', 'would', 'you', 'from', '000', 'first', 'release', 'announces', 'that', 'she', 'tour', 'run', 'july', 'top', 'five', 'time', 'show', 'awards', 'which', 'win', 'their', 'year', 'wins', 'best', 'song', 'two', 'artist', 'blink', '182', 'rihanna', 'announced', 'was', 'live', '2008', 'sold', 'releases', 'third', 'female', 'only', 'his', 'last', 'years', 'march', 'john', '2003', 'million', 'britney', 'spears', 'world', 'michael', 'jackson', 'concerts', 'death', 'name', 'selling', 'ever', 'singer', 'studio', 'face', 'becomes', 'rapper', 'april', 'paul', '2002', 'black', 'band', 'featuring', 'bass', 'musical', 'have', 'may', 'december', '2004', 'hiatus', '2005', 'june', 'stage', 'september', 'august', 'eyed', 'peas', 'west', 'kanye', 'girls', 'october', 'hits', 'touring', '2001', 'drummer', 'love', 'boom', 'guitarist', 'musician', 'composer', 'songwriter']], ['Rock music', 'Sabrebd', 1258069053, 119498, ['rock', 'music', 'genre', 'popular', 'that', 'and', 'roll', 'the', 'united', 'states', 'late', 'early', '1950s', 'developed', 'into', 'range', 'different', 'styles', 'mid', '1960s', 'later', 'particularly', 'kingdom', 'has', 'its', 'style', 'which', 'from', 'genres', 'blues', 'rhythm', 'country', 'also', 'number', 'other', 'such', 'electric', 'folk', 'incorporated', 'influences', 'jazz', 'musical', 'for', 'instrumentation', 'guitar', 'usually', 'part', 'group', 'with', 'drums', 'one', 'more', 'song', 'based', 'time', 'using', 'form', 'but', 'become', 'diverse', 'like', 'pop', 'lyrics', 'often', 'variety', 'themes', 'are', 'social', 'political', 'period', 'distinct', 'subgenres', 'had', 'emerged', 'including', 'southern', 'many', 'development', 'psychedelic', 'was', 'influenced', 'scene', 'new', 'included', 'progressive', 'elements', 'glam', 'subgenre', 'heavy', 'metal', 'power', 'second', '1970s', 'punk', 'down', 'influence', '1980s', 'wave', 'post', 'alternative', '1990s', 'began', 'mainstream', 'grunge', 'britpop', 'indie', 'have', 'since', 'electronic', 'rap', 'well', 'history', 'garage', '2000s', 'saw', 'decline', 'popularity', 'cultural', 'hip', 'hop', 'most', 'leading', 'major', 'out', 'culture', 'emo', 'been', 'associated', 'sex', 'use', 'seen', 'youth', 'against', 'sound', 'sounds', 'pioneered', 'same', 'era', 'produced', 'this', 'instruments', 'derived', 'band', 'lead', 'musicians', 'between', 'members', 'whose', 'guitarist', 'simple', 'beat', 'two', 'four', 'common', 'used', 'there', 'considerable', 'forms', 'rebellion', 'these', 'were', 'christgau', 'cool', 'white', 'male', 'black', 'largely', 'audience', 'both', 'some', 'term', 'being', 'emphasis', 'performance', 'than', 'art', 'soul', 'even', 'through', 'much', 'his', 'all', 'record', 'singer', 'boys', 'their', 'during', 'world', 'playing', 'first', 'describe', 'recorded', 'records', 'around', 'became', 'top', 'billboard', 'airplay', 'charts', 'worldwide', 'single', 'artists', 'hits', 'soon', 'american', 'who', 'dominated', 'decade', 'played', 'commercial', 'success', 'would', 'hurricane', 'along', 'brothers', 'they', 'traditional', 'vocal', 'gained', 'groups', 'acts', 'songs', 'among', 'successful', 'link', 'brought', 'britain', 'hit', 'helped', 'john', 'moved', 'figures', 'end', 'instrumental', 'general', 'about', '1967', 'increasingly', 'albums', 'existing', 'trends', 'not', 'while', 'performers', 'female', 'can', 'british', 'recording', 'significant', 'led', 'becoming', 'pursued', 'careers', 'singles', 'recordings', 'santana', '1969', 'album', 'surf', 'distinctive', 'regional', 'following', 'bands', 'formed', 'california', 'ten', 'national', '1963', 'known', 'achieved', 'work', 'them', 'reached', 'make', 'invasion', 'what', 'beatles', 'rolling', 'stones', 'yardbirds', 'directly', 'high', 'tended', 'less', 'however', 'followed', 'selling', 'subsequent', 'international', 'america', 'scenes', 'greater', 'labels', 'commercially', '1968', 'college', 'psychedelia', 'although', 'taken', 'inspired', 'acoustic', 'adopted', 'after', 'key', 'green', 'off', 'jimi', 'hendrix', 'away', 'hard', 'continued', 'revival', 'movement', 'dylan', 'byrds', 'took', 'york', 'peak', 'sometimes', 'mixed', 'beside', 'label', 'oriented', 'came', '1970', 'radio', '1976', 'christian', 'independent', 'hardcore', 'heartland', '2001', 'women']], ['Medical value travel', 'Argon233', 1153157342, 4149, []], ['Lights (musician)', 'Espo3699', 1213914297, 5898, ['lights', 'april', 'canadian', 'and', 'from', 'she', 'for', 'second', 'was', 'the', '2009', 'new', 'music', 'her', 'released', 'september', '2008', 'which', 'release', 'first', 'album', 'listening', 'siberia', 'october', 'canada', 'little', 'machines', '2014', 'skin', 'earth', '2017', 'with', 'acoustic', 'songs', 'early', 'one', 'song', 'track', 'band', 'august', 'july', 'single', 'had', 'video', 'its', 'their', 'tour', 'received', 'that', 'were']], ['List of soul musicians', 'Ghmyrtle', 1175455921, 4878, ['the']], ['Human computer', 'Giftlite', 1248275178, 4750, ['the', 'computer', 'from', 'first', 'one', 'who', 'mathematical', 'calculations', 'computers', 'human', 'often', 'women', 'were', 'used', 'and', 'work', 'was', 'that', 'this', 'also', 'with', 'for', 'computing', 'tables', 'project', 'his', 'had', 'worked', 'data', 'harvard', 'committee', 'pearson', 'humans', 'world', 'war']], ['Aube (musician)', 'Nihonjoe', 1145410600, 3152, ['akifumi', 'his', 'aube', 'was', 'and', 'the', 'with']], ['List of overtone musicians', 'Sborsody', 1176928050, 2299, ['and', 'overtone', 'singing', 'the', 'with', 'from', 'musician', 'singer']], ['Black dog (ghost)', 'SmackBot', 1220471117, 14746, ['black', 'dog', 'found', 'the', 'folklore', 'some', 'and', 'often', 'said', 'with', 'devil', 'described', 'its', 'was', 'death', 'has', 'large', 'eyes', 'sometimes', 'such', 'shuck', 'also', 'are', 'dogs', 'have', 'been', 'this', 'were', 'way', 'that', 'barghest', 'they', 'may', 'for', 'known', 'night', 'them', 'from', 'other', 'padfoot', 'skriker', 'church', 'grim', 'not', 'can', 'form', 'england', 'being', 'who', 'his', 'when', 'hounds', 'appeared', 'around', 'ghostly', 'story', 'hound', 'near', 'haunted', 'named', 'which', 'area', 'haunt', 'heard', 'omen', 'seen', 'haunts', 'had', 'name', 'but', 'man', 'village', 'would', 'one', 'there', 'home', 'any', 'where', 'through', 'old', 'legend', 'before', 'their', 'people', 'another', 'like', 'then', 'usually', 'local', 'will']], ['USC Trojans volleyball', 'Smuckers', 1218049435, 5525, ['the', 'usc', 'women', 'volleyball', 'team', 'first', 'ncaa', 'national', 'and', 'final', '2008', 'indoor', 'troy', 'season', 'olympian']], ['Tim Arnold (musician)', 'Sohohobo', 1181480380, 4551, ['arnold', 'and', 'london', 'his', 'music', 'the', 'with', 'also', 'for', 'soho', 'released', 'album', 'was', 'solo', 'would', 'song', 'love']], ['2007 Bulldogs RLFC season', 'Timmah86', 1177410119, 11116, ['the', '2007', 'bulldogs', 'season', 'was', 'telstra', 'and', 'against', 'stadium', 'game', 'for', 'down', 'one', 'comeback', 'saw', 'week', 'their', 'first', 'win', 'front', 'round', 'with', 'match', 'points', 'dogs', 'from', 'another', 'top', 'publishing', 'isbn', 'rugby', 'league']], ['Peter Brown (music industry)', 'Zephyrad', 1240235639, 2837, ['brown', 'epstein', 'the', 'beatles', 'and', 'member']], ['Mexican dog-faced bat', 'AnomieBOT', 1255316429, 1138, ['the', 'dog', 'faced', 'bat', 'and']], ['Embryo drawing', 'AxelBoldt', 1034459202, 1712, ['embryo', 'the', 'embryos', 'developmental', 'and', 'animals', 'from', 'that', 'form', 'which', 'early', 'different', 'species', 'this', 'drawings', 'are', 'biology', 'embryonic', 'stages', 'between', 'evolution', 'has', 'both', 'ernst', 'haeckel', 'vertebrate', 'recapitulation', 'theory', 'development', 'evolutionary', 'work', 'comparative', 'anatomy', 'into', 'embryology', 'more', 'were', 'similar', 'for', 'but', 'although', 'his', 'biogenetic', 'law', 'certain', 'von', 'baer', 'wilhelm', 'not', 'gould', 'other', 'richardson', 'university', 'was', 'laws', 'series', 'most', 'one', 'with', 'phylogenetic', 'history', 'through', 'argues', 'features', 'general', 'than', 'human', 'rather', 'specifically', 'comparison', 'science', 'darwin']], ['Old-time music', 'Badagnani', 1124771619, 12755, ['old', 'time', 'music', 'north', 'american', 'folk', 'developed', 'with', 'such', 'dancing', 'and', 'played', 'instruments', 'generally', 'fiddle', 'string', 'most', 'often', 'the', 'banjo', 'guitar', 'that', 'are', 'traditional', 'some', 'also', 'prominent', 'while', 'many', 'dance', 'tunes', 'other', 'native', 'one', 'first', 'recordings', 'country', 'for', 'which', 'appalachian', 'southern', 'style', 'but', 'were', 'these', 'mountain', '19th', 'early', 'styles', 'united', 'states', 'century', 'region', 'include', 'new', 'city', 'musicians', 'their', 'band', 'was', 'well', 'tradition', 'particularly', 'from', 'bluegrass', 'players', 'there', 'finger', 'three', 'have', 'been', 'more', 'this', 'dulcimer', 'regional', 'appalachia', 'its', 'own', 'songs', 'has', 'canada', 'traditions', 'west', 'carolina', 'virginia', 'family', 'tennessee', 'festival', 'bands', 'established', 'schools', 'directed']], ['Arabic music', 'Badagnani', 1209417864, 25114, ['arabic', 'music', 'arab', 'the', 'world', 'with', 'all', 'styles', 'and', 'genres', 'have', 'many', 'also', 'region', 'traditional', 'has', 'other', 'musical', 'that', 'islamic', 'arabian', 'was', 'middle', 'most', 'there', 'between', 'century', 'used', 'notes', 'would', 'not', 'these', 'some', 'instruments', 'such', 'songs', 'were', 'singer', 'maqam', 'notable', 'from', 'which', 'early', 'both', 'are', 'system', 'can', 'several', 'like', 'oud', 'theory', 'including', 'tones', 'scale', 'modern', 'his', 'tone', 'form', 'western', 'for', 'first', 'european', 'egypt', 'cairo', 'singers', 'this', 'been', 'popular', 'later', 'artists', 'use', 'pop', 'rock', 'east', 'quarter', 'genre', 'guitar', 'known', 'scholars', 'but', 'morocco', 'jazz', 'ajnas']], ['C Sharp (programming language)', 'Eaglizard', 1232492672, 52364, ['sharp', 'like', 'the', 'but', 'with', 'number', 'programming', 'language', 'functional', 'object', 'class', 'and', 'was', 'microsoft', 'its', 'net', 'standard', 'ecma', 'iso', 'mono', 'name', 'open', 'source', 'project', 'compiler', 'runtime', 'for', 'languages', 'common', 'infrastructure', 'cli', 'most', 'which', 'design', 'support', 'such', 'type', 'use', 'variables', 'garbage', 'are', 'very', 'code', 'programmers', 'both', 'from', 'that', 'functions', 'memory', 'not', 'framework', 'libraries', 'using', 'system', 'called', 'time', 'been', 'has', 'java', 'have', 'similar', 'two', 'can', 'used', 'any', 'other', 'features', 'linq', 'expressions', 'methods', 'types', 'through', 'data', 'program', 'this', 'also', 'specification', 'implementation', 'into', 'classes', 'value', 'some', 'does', 'specific', 'implicit', 'keyword', 'only', 'default', 'defined', 'unlike', 'all', 'static', 'method', 'each', 'they', 'namespace', 'same', 'reference', 'instance', 'example', 'console']], ['List of Saturday Night Live musical sketches', 'Gary King', 1134966249, 13287, ['saturday', 'night', 'live', 'the', 'chris']], ['Joe Becker (musician)', 'Gary King', 1203234507, 5842, ['becker', 'and', 'guitar', 'the', 'joe', 'music', 'records', 'film', 'soundtrack', 'horror', 'released', 'performed']], ['Will Johnson (soccer)', 'Mayumashu', 1218489712, 3562, ['johnson', 'canadian', 'soccer', 'player', 'played', 'for', 'league', 'canada', 'was', 'the', 'his', 'and', 'team', 'season', 'after', 'year', 'mls', 'first', 'scored', 'goal', 'with', 'december', '2008', 'real', 'salt', 'lake', 'against', 'cup', '2013', '2016']], ['Aco (musician)', 'Noodleboy', 1132546632, 3129, ['the']], ['Geoff Smith (British musician)', 'Richardrj', 1194687509, 2043, ['smith', 'was', 'the', 'film']], ['Fiskerton, Lincolnshire', 'Snigbrook', 1259869948, 5853, ['fiskerton', 'village', 'and', 'the', 'was', 'which', 'that', 'been']], ['Reflection-oriented programming', 'Soumyasch', 1143366937, 38, []], ['B (programming language)', 'Uvaphdman', 1196622610, 5482, ['language', 'the', 'thompson', 'ritchie', 'was', 'from', 'bcpl', 'and', 'that', 'for', 'pdp', 'version', 'this']], ['Richard Wright (musician)', 'Bdubiscool', 1189536295, 16185, ['wright', 'was', 'and', 'member', 'the', 'band', 'pink', 'floyd', 'all', 'but', 'one', 'playing', 'end', 'waters', 'mason', 'while', 'after', 'joined', 'barrett', 'group', 'him', 'gilmour', 'with', 'later', 'touring', 'wall', 'for', 'became', 'full', 'time', 'division', 'bell', 'sessions', 'during', 'were', 'released', 'album', 'from', 'two', 'solo', 'including', 'broken', 'live', 'part', 'lead', 'such', 'his', 'farfisa', 'hammond', 'took', 'early', 'play', 'guitar', 'piano', 'mother', 'musical', 'music', 'which', 'not', 'had', 'london', 'organ', 'through', 'first', 'that', 'vocals', 'played', 'keyboards', 'would', 'concert', 'been', 'more', 'some', 'tour', 'said', 'used', 'using']], ['Voice classification in non-classical music', 'Iridescent', 1198092852, 11280, ['system', 'voice', 'classification', 'non', 'classical', 'music', 'are', 'used', 'not', 'vocal', 'but', 'range', 'these', 'with', 'singers', 'and', 'that', 'the', 'term', 'systems', 'type', 'for', 'voices', 'within', 'singing', 'this', 'two', 'one', 'opera', 'choral', 'other', 'men', 'women', 'soprano', 'mezzo', 'contralto', 'tenor', 'categories', 'alto', 'male', 'sing', 'female', 'singer', 'would', 'have', 'line', 'middle', 'however', 'below', 'list']], ['Dalmatian (dog)', 'J. Spencer', 1207793294, 26582, ['the', 'dalmatian', 'breed', 'dog', 'for', 'its', 'with', 'liver', 'spots', 'and', 'used', 'can', 'that', 'were', 'breeds', 'dalmatians', 'kennel', 'club', 'well', 'akc', 'standard', 'from', 'both', 'but', 'not', 'are', 'usually', 'color', 'blue', 'dogs', 'other', 'puppies', 'their', 'first', 'they', 'have', 'may', 'which', 'often', 'health', 'deafness', 'hearing', 'years', 'was', 'this', 'also', 'been', 'hyperuricemia', 'uric', 'acid', 'backcross', 'project', 'horses', 'fire']], ['1936 in music', 'JohnRogers', 1243745950, 23417, ['music', 'the', '1936', 'country', 'january', 'march', 'symphony', 'orchestra', 'april', 'concerto', 'may', 'and', 'little', 'time', 'december', 'film', 'opera', 'cole', 'with', 'his', 'conductor', 'introduced', 'shirley', 'dorothy', 'fields', 'jerome', 'kern', 'fred', 'astaire', 'swing', 'your', 'for', 'musical', 'love', 'dance', 'billy', 'harry', 'you', 'ginger', 'rogers', 'irving', 'berlin', 'follow', 'fleet', 'richard', 'johnny', 'rhythm', 'bing', 'crosby', 'sing', 'singer', 'jack', 'string', 'quartet', 'london', 'production', 'opened', 'theatre', 'ran', 'performances', 'september', 'october', 'starring', 'november', 'featuring', 'composer', 'pianist', 'songwriter', 'february', 'june', 'august']], ['Guide dog', 'Sarranduin', 1165601603, 7339, ['guide', 'dogs', 'the', 'are', 'assistance', 'trained', 'blind', 'and', 'people', 'human', 'training', 'who', 'from', 'dog', 'with', 'most', 'service', 'animals', 'public', 'was', 'that', 'have', 'used', 'for', 'other', 'their', 'first', 'animal', 'were', 'not', 'united', 'states', 'german', 'access', 'breed', 'labrador', 'act', 'general', 'rights', 'more', 'allowed']], ['1962 in country music', 'Briguy52748', 1249862464, 7954, ['country', 'music', 'the', 'and', 'singer']], ['List of dystopian music, TV programs, and games', 'Notinasnaid', 1165317338, 13458, ['this', 'dystopian', 'themes', 'music', 'and', 'games', 'computer', 'role', 'the', 'features', 'rock', 'band', 'black', 'with', 'their', 'american', 'both', 'from', 'which', 'dystopia', 'one', 'most', 'was', 'living', 'various', 'songs', 'society', 'world', 'that', 'life', '2000', 'about', 'future', 'government', 'space', 'many', 'are', 'set', 'based', 'man', 'series', 'against', 'have', 'human', '1984', 'orwell', 'book', 'while', 'video', 'for', 'song', 'album', 'death', '2010', 'concept', 'shooter', 'new', 'after', 'last', 'year', 'four', 'known', 'fighting', 'organization', 'earth', '1987', '2002', 'planet', 'final', 'when', '2007', 'where', 'corporate', 'who', 'two', 'controlled', 'syndicate', 'technology', 'being', 'has', 'around', 'post', 'nuclear', 'apocalyptic', 'utopia', 'between', 'main', 'his', 'they', 'story', 'takes', 'place', 'artificial', 'people', 'end', 'such', 'evil', 'global', 'humanity', 'time', 'point', 'control', 'into', 'group', 'power', 'zero', 'take', 'back', 'alternate', 'alien', 'all', 'first', 'through', 'also', 'citizens', 'police', 'rule', 'protagonist', 'order', 'dark', '2005', '2015', '2008', 'its', 'system', 'ruled', 'city', 'her', 'television', 'present', 'created', 'but', 'only', 'under', 'episode', '2013', 'had', 'united', 'states', 'there', 'war', 'years', '2003', 'bbc', 'century', 'now', 'season', 'universe', 'state', 'out', 'near', 'called', 'taken', 'economic', 'collapse', 'were', 'developed', 'crime', 'left', 'humans', 'oppressive', 'game', 'over', 'america', 'population', 'begins', 'been', 'virus', 'him', 'girls', 'race', 'them', 'prevent', 'player', 'person', 'deus']], ['Steven Cohen (soccer)', 'Scouselad10', 1237669593, 2117, ['cohen', 'the', 'world', 'soccer', 'daily', 'was', 'club', 'his', 'liverpool', 'for', 'and', 'that']], ['Steve Perry (musician)', 'Woohookitty', 1254812045, 22204, ['perry', 'singer', 'and', 'the', 'lead', 'rock', 'band', 'journey', 'during', 'their', 'from', '1998', 'also', 'had', 'solo', 'music', 'time', 'voice', 'has', 'been', 'greatest', 'was', 'california', 'his', 'radio', 'mother', 'then', 'with', 'for', 'song', 'after', 'first', 'that', 'wrote', 'were', 'record', 'album', 'project', 'would', 'never', 'tour', 'former', 'which', 'vocals', 'trial', 'fire', 'songs', 'released', 'sherrie', 'out', 'steve', 'two']], ['2009 Louisiana Tech Bulldogs football team', 'AllisonFoley', 1245796406, 22410, ['the', 'team', 'joe', 'red', 'from', 'quarter', 'pass', 'dennis', 'morris', 'daniel', 'porter', 'run', 'point', 'williams', 'two', '1st', 'aub', 'wes', 'byrum', 'ross', 'jenkins', 'matt', 'nelson', 'kick', 'chris', 'navy', 'return', 'state', 'nev', 'kyle', 'bsu', 'brotzman', 'fres', 'kevin', 'goessling']], ['David Gray (musician)', 'RattleandHum', 1159841492, 7203, ['david', 'gray', 'released', 'his', 'first', 'album', 'and', 'the', 'release', 'white', 'ladder', 'was', 'chart', 'for', 'which', 'two', 'also', 'united', 'best', 'october', 'awards', 'life', 'with', 'had', 'that', 'music', 'sell', 'songs', 'guitar', 'year', 'its', 'single', 'vocals', 'new', 'touring', 'september', 'tour', 'backing']], ['Craig Martin (soccer)', 'Darius Dhlomo', 1174203493, 709, ['the']], ['Georgia Bulldogs football', 'Davidscharoun', 1166567889, 43718, ['the', 'georgia', 'bulldogs', 'football', 'university', 'bowl', 'national', 'athletic', 'and', 'division', 'conference', 'sec', 'they', 'their', 'home', 'games', 'sanford', 'stadium', 'season', 'was', 'uga', 'two', 'championships', '1980', 'have', 'champion', 'has', 'also', 'been', 'one', 'other', '1920', 'won', 'tied', 'for', 'second', 'most', 'history', 'all', 'time', 'team', 'its', 'bulldog', 'over', 'times', 'which', 'were', 'southern', 'first', 'from', 'during', 'years', 'with', 'championship', 'head', 'game', 'against', 'after', 'vince', 'dooley', 'coach', 'are', 'played', 'hall', 'fame', 'inducted', 'fans', 'that', 'used', 'red', 'black', 'since', 'white', 'when', 'silver', 'britches', 'changed', 'uniform', 'pants', 'players', 'helmet', 'jerseys', 'stripe', 'numbers', 'away']], ['Time travel', 'Thug outlaw69', 1140826049, 35170, ['time', 'travel', 'the', 'concept', 'between', 'certain', 'different', 'space', 'object', 'person', 'with', 'known', 'machine', 'and', 'fiction', 'idea', 'was', 'past', 'possible', 'forward', 'special', 'relativity', 'general', 'however', 'one', 'more', 'than', 'another', 'not', 'for', 'backward', 'that', 'allow', 'such', 'traveling', 'point', 'spacetime', 'has', 'physics', 'only', 'quantum', 'mechanics', 'wormholes', 'history', 'some', 'story', 'who', 'when', 'earth', 'many', 'have', 'first', 'his', 'future', 'where', 'been', 'but', 'science', 'early', 'are', 'through', 'means', 'used', 'these', 'which', 'about', 'from', 'because', 'traveler', 'does', 'present', 'back', 'events', 'real', 'other', 'same', 'example', 'before', 'this', 'may', 'clock', 'might', 'into', 'were', 'physicists', 'possibility', 'closed', 'curves', 'world', 'their', 'own', 'there', 'any', 'theory', 'would', 'causality', 'grandfather', 'paradox', 'what', 'novikov', 'can', 'self', 'principle', 'worlds', 'interpretation', 'faster', 'speed', 'light', 'gravity', 'effects', 'hawking', 'exist', 'also', 'its', 'all', 'wormhole', 'way', 'end', 'dilation', 'either', 'will', 'matter', 'two', 'existence', 'negative', 'energy', 'argued', 'could', 'each', 'violation', 'classical', 'impossible', 'region', 'signal', 'event', 'information', 'they', 'even', 'single', 'travelers', 'experiment', 'photons', 'philosophers', 'presentism']], ['Fisk University', 'NerdyScienceDude', 1263393671, 16246, ['fisk', 'university', 'black', 'nashville', 'the', 'was', 'and', 'its', 'campus', 'historic', 'national', 'first', 'african', 'american', 'association', 'colleges', 'schools', 'for', 'school', 'education', 'that', 'named', 'which', 'with', 'student', 'from', 'during', 'students', 'two', 'became', 'arts', 'college', 'had', 'hall', 'building', 'built', 'president', 'program', 'other', 'stieglitz', 'collection', 'art']], ['Annie (musical)', 'Piano non troppo', 1223619626, 27558, ['annie', 'broadway', 'musical', 'the', 'little', 'orphan', 'with', 'charnin', 'and', 'book', 'meehan', 'original', 'production', 'opened', '1977', 'for', 'theatre', 'now', 'many', 'national', 'tours', 'including', 'songs', 'tomorrow', 'hard', 'knock', 'life', 'are', 'most', 'year', 'old', 'girls', 'orphanage', 'other', 'orphans', 'when', 'molly', 'from', 'she', 'pepper', 'july', 'tells', 'into', 'back', 'then', 'her', 'parents', 'they', 'this', 'maybe', 'but', 'miss', 'hannigan', 'later', 'his', 'after', 'their', 'reprise', 'him', 'where', 'made', 'have', 'like', 'you', 'who', 'been', 'grace', 'farrell', 'oliver', 'warbucks', 'christmas', 'was', 'all', 'new', 'york', 'rooster', 'lily', 'that', 'not', 'one', 'show', 'song', 'never', 'fully', 'dressed', 'without', 'smile', 'about', 'shows', 'two', 'more', 'second', 'produced', 'united', 'first', 'were', 'character', 'version', 'had', 'out', 'novelisation', 'actress', 'play', 'title', 'role', 'producers', 'performances', 'played', 'starred', 'daddy', 'ann', 'also', 'closed', 'january', 'until', '2009', 'touring', 'run', 'there', 'tour', 'company', '1978', 'may', '1979', 'took', 'over', '1981', 'september', 'west', '1982', 'film', 'playing', 'cast', 'end', 'recording', 'performed', 'revival', '1997', 'anniversary', 'nell', 'carter', 'released', '1998', '1999', '2000', '2001', '2010', '2007', '2011', '2005', 'directed', '2012', 'school', 'references', 'episode']], ['Alex Turner (musician)', 'CambridgeBayWeather', 1187010135, 9718, ['david', 'turner', 'english', 'and', 'the', 'rock', 'band', 'arctic', 'monkeys', 'with', 'has', 'released', 'albums', 'also', 'recorded', 'his', 'side', 'last', 'shadow', 'puppets', 'when', 'was', 'three', 'friends', 'their', 'sheffield', 'debut', 'album', 'that', 'what', 'not', 'stone', 'all', 'time', 'studio', '2007', '2011', '2013', 'tranquility', 'base', 'hotel', '2018', 'have', 'music', 'festival', 'both', 'performed', 'during', '2012', 'london', 'summer', 'miles', 'kane', 'two', 'age', '2008', 'you', 'come', '2016', 'for', 'wrote', 'savior', '2017', 'from', 'been', 'times', 'early', 'school', 'said', 'father', 'were', 'played', 'had', 'some', 'years', 'helders', 'they', 'joined', 'other', 'while', 'guitar', 'nicholson', 'him', 'year', 'who', 'than', 'noted', 'too', 'writing', '2004', 'get', 'out', 'one', 'after', 'began', 'mid', 'about', 'songs', 'later', 'would', 'just', 'first', 'york', 'voice', 'song', 'working', 'part', 'richard', 'clarke', 'attention', 'april', 'most', 'single', 'tour', 'james', 'ford', 'lyrics', 'new', 'remarked', 'are', 'petridis', 'guardian', 'described', 'like', 'but', 'love', 'writer', 'pitchfork', 'stage', 'style', 'los', 'angeles', 'more']], ['Python (programming language)', 'Lulu of the Lotus-Eaters', 1137530195, 41571, ['python', 'and', 'programming', 'language', 'van', 'rossum', 'first', 'released', 'design', 'philosophy', 'code', 'with', 'its', 'use', 'object', 'oriented', 'for', 'large', 'multiple', 'including', 'often', 'standard', 'library', 'was', 'the', 'features', 'like', 'list', 'system', 'reference', 'major', 'that', 'not', 'run', 'release', 'more', 'other', 'will', 'are', 'supported', 'available', 'many', 'community', 'cpython', 'implementation', 'software', 'development', 'project', 'from', 'new', 'support', 'version', 'releases', 'include', 'which', 'methods', 'uses', 'also', 'name', 'method', 'variable', 'names', 'program', 'some', 'has', 'functions', 'expressions', 'modules', 'such', 'better', 'than', 'rather', 'all', 'into', 'this', 'applications', 'interpreter', 'syntax', 'while', 'there', 'one', 'can', 'time', 'written', 'languages', 'spam', 'eggs', 'common', 'have', 'style', 'where', 'statements', 'indentation', 'block', 'but', 'most', 'assignment', 'statement', 'value', 'type', 'using', 'same', 'example', 'since', 'may', 'objects', 'types', 'strings', 'data', 'three', 'each', 'used', 'class', 'function', 'before', 'operator', 'import', 'module', 'similar', 'java', 'division', 'integer', 'libraries', 'part', 'expression', 'both', 'number', 'string', 'blah', 'index', 'negative', 'third', 'classes', 'round', 'several', 'scripting', 'processing', 'web', 'implementations', 'package', 'programs', 'compiles', 'been', '2012', 'isbn', '978']], ['List of gospel musicians', 'Absolon', 1197658845, 3805, ['list', 'christian', 'music', 'performers', 'the', 'gospel']], ['Tom Hooper (musician)', 'Bearcat', 1204967541, 1441, ['hooper', 'and', 'the']], ['Endoglin', 'DOI bot', 1212259031, 6778, ['endoglin', 'cell', 'and', 'the', 'tgf', 'beta', 'receptor', 'complex', 'has', 'role', 'for', 'tumor', 'growth', 'cancer', 'cells', 'other', 'gene', 'expression', 'with', 'this', 'that', 'which', 'are', 'extracellular', 'domain', 'cytoplasmic', 'region', 'bmp', 'can', 'been', 'binding', 'bind', 'cellular', 'its']], ['Indian classical music', 'Davydog', 1222543238, 9503, ['indian', 'classical', 'music', 'the', 'subcontinent', 'which', 'india', 'and', 'most', 'after', 'western', 'has', 'two', 'major', 'traditions', 'north', 'tradition', 'called', 'hindustani', 'while', 'south', 'expression', 'carnatic', 'these', 'were', 'not', 'about', '16th', 'century', 'into', 'forms', 'raga', 'based', 'however', 'systems', 'have', 'more', 'than', 'are', 'found', 'hinduism', 'ancient', 'natyashastra', 'sanskrit', 'text', 'performance', 'both', 'tala', 'notes', 'melodic', 'structure', 'time', 'from', 'with', 'for', 'between', 'such', 'dance', 'form', 'this', 'his', 'one', 'some', 'texts', 'part', 'musical', 'swaras', 'octave', 'song', 'different', 'ragas', 'but', 'example', 'also', 'according', 'that', 'was', 'instruments', 'four', 'their', 'each', 'states', 'system', 'theory', 'talas', 'modern', 'era', 'musicians', 'hindu', 'many', 'other', 'scholars', 'its', 'folk', 'influences', 'persian', 'may', 'performed', 'link', 'scale', 'university', 'press', 'isbn', '978', 'cs1', 'maint', 'ref', 'harv', '2012', 'oxford', 'moutal', 'patrick']], ['Sun dog', 'Hellbus', 1208969289, 18050, ['sun', 'dog', 'parhelia', 'that', 'one', 'the', 'two', 'dogs', 'halo', 'ice', 'crystals', 'light', 'and', 'they', 'can', 'seen', 'are', 'from', 'with', 'their', 'more', 'for', 'which', 'other', 'being', 'suns', 'weather', 'day', 'his', 'was', 'were']], ['1996 in music', 'Kharker', 1148585201, 21688, ['music', 'that', 'the', 'year', '1996', 'country', 'january', 'and', 'madonna', 'american', 'for', 'been', 'are', 'records', 'released', 'song', 'all', 'their', 'dancer', 'singer', 'one', 'from', 'michael', 'february', 'day', 'out', 'new', 'after', 'with', 'musical', 'its', 'first', 'kiss', 'they', 'awards', 'band', 'his', 'releases', 'album', 'september', 'record', 'reunion', 'march', 'john', 'concert', 'tour', 'april', 'mtv', 'video', 'july', 'producer', 'may', 'actress', 'june', 'group', 'single', 'august', 'guitarist', 'david', 'rapper', 'jack', 'october', 'november', 'december', 'concerto', 'broadway', 'songwriter', 'musician', 'actor', 'composer']], ['Lua (programming language)', 'Makkuro', 1113957128, 0, ['lua', 'from', 'programming', 'language', 'for', 'use', 'applications', 'the', 'and', 'api', 'into', 'was', 'software', 'most', 'languages', 'features', 'were', 'not', 'such', 'extension', 'its', 'ierusalimschy', 'tecgraf', 'had', 'that', 'data', 'object', 'any', 'only', 'which', 'syntax', 'scripting', 'new', 'other', 'also', 'example', 'with', 'function', 'table', 'functions', 'are', 'can', 'using', 'first', 'class', 'number', 'values', 'array', 'this', 'loop', 'nil', 'tables', 'key', 'value', 'used', 'stack', 'based', 'game', 'isbn', '978', 'archived', 'original', 'july', '2018']], ['Single-board computer', 'Nathael', 1220260601, 8271, ['single', 'board', 'computer', 'with', 'and', 'computers', 'are', 'for', 'embedded', 'often', 'such', 'more', 'plug', 'backplane', 'system', 'the', 'used', 'sbcs', 'motherboard', 'cards']], ['Mets de Guaynabo (volleyball)', 'Osplace', 1239156764, 2091, []], ["United States men's national soccer team 2009 results", 'Rebajc3', 1252384026, 79089, []], ['Joseph Williams (musician)', 'RussBot', 1140752684, 4253, ['williams', 'and', 'film', 'for', 'his', 'the', 'toto', 'lead', 'from', 'was', 'albums', 'album', 'compilation', '2006', 'vocals', 'solo', 'released', 'project', 'songs', 'song']], ['The Hunchback of Notre Dame (musical)', 'RussBot', 1192176615, 42, ['the', 'hunchback', 'notre', 'dame', 'musical', 'with', 'songs', 'from', 'disney', 'film', 'original', '1999', 'berlin', 'der', 'glöckner', 'von', 'was', 'first', 'premiere', 'for', 'one', 'english', 'had', 'its', 'playhouse', '2014', 'and', 'show', 'new', 'which', 'after', 'that', 'would', 'not', 'broadway', '2017', 'german', 'production', 'stage', 'into', 'received', 'king', 'this', 'version', 'arts', 'cast', 'quasimodo', 'his', 'nominations', 'award']], ['China national soccer team', 'Seedbot', 1199103839, 45, []], ['Covariance and contravariance (computer science)', 'Wakapop', 1167547364, 7453, ['programming', 'language', 'type', 'support', 'subtyping', 'for', 'the', 'cat', 'subtype', 'animal', 'then', 'should', 'used', 'variance', 'how', 'more', 'complex', 'types', 'example', 'list', 'function', 'that', 'constructor', 'may', 'ocaml', 'because', 'covariant', 'this', 'are', 'other', 'from', 'contravariant', 'parameter', 'will', 'consider', 'when', 'rules', 'such', 'arrays', 'inheritance', 'and', 'generic', 'constructors', 'instead', 'invariant', 'programs', 'contravariance', 'runtime', 'can', 'system', 'allow', 'useful', 'would', 'safe', 'could', 'rule', 'which', 'specific', 'both', 'these', 'time', 'not', 'some', 'common', 'ilist', 'interface', 'declared', 'out', 'parameters', 'each', 'compiler', 'with', 'any', 'use', 'above', 'interfaces', 'than', 'one', 'return', 'first', 'class', 'argument', 'only', 'read', 'data', 'write', 'general', 'array', 'have', 'since', 'but', 'possible', 'into', 'also', 'immutable', 'java', 'generics', 'two', 'using', 'object', 'method', 'all', 'functions', 'however', 'covariantly', 'check', 'there', 'error', 'covariance', 'parameterized', 'way', 'languages', 'like', 'need', 'was', 'displaystyle', 'leq', 'must', 'overriding', 'has', 'while', 'scala', 'methods', 'where', 'been', 'objects', 'compareto', 'comparable', 'provide', 'multiple', 'dispatch', 'most', 'programmer', 'declaration', 'site', 'annotations', 'ienumerator', 'valid', 'contravariantly', 'classes', 'structure', 'they', 'wildcards', 'wildcard', 'extends', 'capture']], ['English folk music (1500–1899)', 'Ashley Y', 1177634764, 2073, ['and', 'english']], ['Personal computer', 'Darklock', 1220391790, 45663, ['personal', 'computer', 'capabilities', 'and', 'price', 'for', 'use', 'computers', 'are', 'directly', 'end', 'user', 'than', 'large', 'time', 'many', 'people', 'the', 'same', 'not', 'used', 'with', 'had', 'their', 'any', 'machines', 'while', 'users', 'may', 'applications', 'usually', 'these', 'systems', 'run', 'software', 'which', 'most', 'often', 'form', 'developed', 'from', 'hardware', 'operating', 'system', 'programming', 'still', 'this', 'mobile', 'only', 'available', 'through', 'since', 'early', 'microsoft', 'intel', 'market', 'first', 'windows', 'share', 'include', 'apple', 'such', 'linux', 'digital', 'have', 'all', 'ibm', 'its', 'but', 'term', 'some', 'were', 'they', 'one', 'computing', 'could', 'single', 'connected', 'research', 'would', 'been', 'expensive', 'was', 'made', 'integrated', 'later', 'based', 'small', 'called', 'that', 'word', 'video', 'mouse', 'required', 'business', 'generally', 'sold', 'kit', 'panel', 'displays', 'disk', 'drives', 'units', '1973', 'portable', 'scamp', 'apl', 'machine', 'processor', 'drive', 'keyboard', 'desktop', 'performance', 'other', 'about', 'another', 'shipped', 'also', 'introduced', 'display', 'storage', 'designed', 'standard', 'power', 'case', 'mass', '1977', 'however', 'year', 'over', '000', 'more', 'card', 'memory', 'high', 'cost', 'home', 'graphics', 'text', 'million', 'unit', 'sound', 'processors', 'laptop', 'internet', 'tasks', 'pcs', 'can', 'components', 'motherboard', 'external', 'monitor', 'screen', 'into', 'usb', 'gaming', 'input', 'devices', 'laptops', '2008', 'cards', 'netbooks', 'data', 'tablet', 'using', 'pocket', 'expansion', 'provide', 'application', 'how', 'according', 'billion', 'sales', 'shipments', 'quarter', 'decline', 'selling']], ['The Mandogs', 'DerHexer', 1205282029, 3968, ['the', 'mandogs', 'was', 'show', 'hosts', 'and', '2012', 'for', 'has', 'other', 'his', 'jay']], ['David Levi (musician)', 'DumZiBoT', 1212260237, 3949, ['the', 'naked', 'brothers', 'band']], ['Scores (computer virus)', 'LilHelpa', 1235850703, 2706, ['scores', 'virus', '1988', 'and', 'the', 'system']], ['Digital photography', 'Mintleaf', 1095727840, 18093, ['digital', 'photography', 'cameras', 'images', 'lens', 'photographic', 'film', 'the', 'are', 'and', 'stored', 'computer', 'file', 'for', 'processing', 'such', 'technology', 'photographs', 'were', 'which', 'was', 'image', 'typically', 'without', 'first', 'consumer', 'when', 'their', 'professional', 'using', 'than', 'social', 'media', 'since', 'have', 'also', 'from', 'camera', 'format', 'quality', 'but', 'many', 'advanced', 'while', 'has', 'only', 'its', 'later', 'produced', 'semiconductor', 'development', 'sensors', 'device', 'ccd', 'sensor', 'they', 'that', 'one', 'used', 'taken', 'with', 'not', 'this', 'color', 'picture', 'jpeg', 'most', 'kodak', 'had', 'resolution', 'megapixels', 'pixels', 'capture', 'single', 'nikon', 'available', 'pictures', 'photographers', 'more', 'use', 'number', 'photos', 'memory', 'space', 'raw', 'pixel', 'some', 'end', 'card', 'may', 'can', 'take', 'cards', 'same', 'all', 'similar', 'however', 'print', 'different', 'these', 'dynamic', 'range', 'high', 'other', 'photo', 'prints', 'gamut', 'ratio', 'aspect']], ['George Crum (musician)', 'SmackBot', 1252996687, 3848, ['george', 'crum', 'was', 'the', 'national', 'ballet', 'and', 'with', 'also', 'his', 'opera', 'conducted']], ['Solver (computer science)', 'SmackBot', 1253282654, 1861, ['solver', 'the', 'that', 'problem', 'problems', 'with', 'solvers', 'linear', 'equations', 'systems', 'for']], ['Georgia Bulldogs football under Robert Winston', 'Tlmclain', 1166046122, 1989, []], ['Wildlife photography', 'Zargulon', 1165248747, 1410, ['wildlife', 'photography', 'with', 'for', 'and', 'the', 'photos']], ['Traditional Thai musical instruments', 'Badagnani', 1191830919, 6775, ['traditional', 'thai', 'musical', 'instruments', 'are', 'the', 'used', 'and', 'music', 'thailand', 'string', 'percussion', 'played', 'plucked', 'also', 'region', 'with', 'three', 'two', 'made', 'from', 'isan', 'northern', 'set', 'saw', 'hardwood', 'northeast', 'bamboo', 'drum', 'hands', 'piphat', 'ensemble', 'large', 'klong', 'pair', 'frame', 'southern', 'nora', 'tuned', 'gong', 'khong', 'small', 'bossed', 'gongs', 'ranat', 'instrument', 'called', 'wooden', 'khlui', 'reed', 'glong']], ['Landseer (dog)', 'Birdgirl5', 1231438650, 2006, ['the', 'landseer', 'black', 'and', 'newfoundland', 'dogs', 'with']], ['Charles McPherson (musician)', 'Cosprings', 1255183865, 3007, ['charles', 'mcpherson', 'jazz', 'with', 'mingus', 'the', 'prestige', 'xanadu', '1980']], ['Comparison of programming languages (basic instructions)', 'IanOsgood', 1238781354, 61644, ['languages', 'are', 'this', 'the', 'statements', 'with', 'type', 'standard', 'constants', 'int', 'and', 'can', 'used', 'short', 'long', 'size', 'max', 'for', 'not', 'width', 'integer', 'types', 'required', 'bits', 'array', 'have', 'floating', 'point', 'strings', 'has', 'precision', 'value', 'function', 'run', 'time', 'number', 'variable', 'same', 'real', 'only', 'instead', 'there', 'may', 'std']], ['Les Cousins (music club)', 'Rodparkes', 1187072433, 4926, ['les', 'cousins', 'was', 'and', 'club', 'the', 'john']], ['Paul Carr (musician)', 'Snalwibma', 1254142018, 5716, ['carr', 'the', 'and']], ['2006 in music', 'Suduser85', 1171547747, 105280, ['music', 'that', 'place', 'the', 'year', '2006', 'british', 'country', 'jazz', 'january', 'releases', 'album', 'and', 'begins', 'with', 'new', 'band', 'composer', 'held', 'usa', 'her', 'tour', 'after', 'five', 'years', 'announces', 'their', 'was', 'february', 'day', 'out', 'festival', 'australia', 'studio', 'also', 'from', 'all', 'for', 'american', 'show', 'may', 'drummer', 'paul', 'records', 'opera', 'have', 'his', 'awards', 'are', 'madonna', 'third', 'time', 'rock', 'win', 'song', 'you', 'wins', 'record', 'john', 'artist', 'three', 'first', 'since', 'james', 'one', 'include', 'brown', 'debut', 'march', 'second', 'single', 'number', 'hot', 'weeks', 'hit', 'group', 'film', 'world', 'top', 'billboard', '100', 'release', 'lead', 'singer', 'april', 'original', 'released', 'its', 'week', 'love', 'don', 'taylor', 'television', 'june', 'selling', '000', 'shakira', 'nelly', 'furtado', 'july', 'orchestra', 'justin', 'timberlake', 'songwriter', 'featuring', 'video', 'august', 'mtv', 'september', 'beyoncé', 'solo', 'singles', 'bass', 'english', 'october', 'guitarist', 'december', 'which', 'november', 'musician', 'broadway', 'performances', 'pianist']], ['Spawning (computer gaming)', 'Vendettax', 1176750529, 3413, ['games', 'the', 'its', 'game', 'player', 'spawn', 'some', 'and', 'points', 'players', 'for', 'team', 'enemies']], ['Sean Delaney (musician)', 'Bestcellar', 1204328174, 5638, ['delaney', 'sean', 'was', 'and', 'for', 'his', 'work', 'with', 'the', 'rock', 'band', 'kiss', 'from', 'early', 'their', 'wrote', 'songs', 'album', 'all', 'also', 'song', 'that', 'solo', 'produced', 'gene', 'simmons', 'peter', 'criss', '1978', 'member', 'after', 'had', 'records', 'bill', 'aucoin', 'were', 'neil', 'casablanca', 'who', 'they', 'have', 'this', 'death', 'while', 'piper', 'released', 'which', 'other', 'skatt', 'bros']], ['Tony Kaye (musician)', 'Bondegezou', 1141489894, 8419, ['kaye', 'and', 'member', 'the', 'rock', 'band', 'yes', 'was', 'music', 'joined', 'his', 'from', '1971', 'played', 'their', 'first', 'then', 'badger', 'after', 'which', 'with', 'david', 'detective', 'badfinger', 'album', 'for', 'left', '1994', 'circa', '2009', 'two', 'also', 'early', 'piano', 'who', 'time', 'had', 'playing', 'but', 'during', 'big', 'led', 'group', 'tour', 'that', 'more', 'this', 'singer', 'new', 'squire', 'some', 'hammond', '1969', 'keyboards', 'all', 'offer', 'one', 'live', 'white', 'various', 'rabin', '90125', 'keyboard', 'tribute', '2007', 'artists']], ['Danja (musician)', 'Crusoe8181', 1257155543, 6925, ['danja', 'and', 'for', 'timbaland', 'produced', 'the', 'his', 'with', 'album', 'also']], ['Ruby (programming language)', 'Hervegirod', 1193928035, 30284, ['ruby', 'programming', 'language', 'was', 'and', 'the', 'matsumoto', 'uses', 'including', 'object', 'oriented', 'perl', 'has', 'that', 'list', 'some', 'with', 'not', 'but', 'like', 'python', 'then', 'features', 'for', 'use', 'one', 'design', 'being', 'its', 'name', 'code', 'been', 'written', 'two', 'were', 'later', 'first', 'release', 'japanese', 'more', 'released', 'which', 'new', 'this', 'many', 'classes', 'exception', 'handling', 'following', 'time', 'than', 'there', 'only', 'standard', 'rails', 'christmas', 'day', 'from', 'changes', 'over', 'block', 'variables', 'are', 'they', 'syntax', 'hash', 'using', 'value', 'string', 'support', 'since', 'will', 'users', 'version', 'added', 'method', 'class', 'array', 'similar', 'also', 'include', 'performance', 'few', 'all', 'can', 'other', 'instance', 'variable', 'come', 'methods', 'programmer', 'machine', 'run', 'principle', 'least', 'such', 'surprise', 'may', 'languages', 'defined', 'example', 'metaprogramming', 'function', 'called', 'interpreter', 'used', 'line', 'java', 'implementation', 'exceptions', 'implementations', 'jruby']], ['Texture (music)', 'J Lorraine', 1161070178, 3626, ['music', 'texture', 'the', 'and', 'are', 'parts', 'musical', 'with']], ['List of computer role-playing games', 'Lllockwood', 1179441080, 43088, []], ['Register (music)', 'Hyacinth', 1082665179, 598, ['register', 'the', 'and', 'vocal']], ['Mode (computer interface)', 'Donreed', 1182732608, 2991, ['user', 'interface', 'design', 'mode', 'computer', 'any', 'which', 'the', 'will', 'different', 'from', 'that', 'other', 'modal', 'lock', 'and', 'keys', 'keyboard', 'into', 'after', 'modes', 'modeless', 'errors', 'action', 'one', 'while', 'for', 'his', 'raskin', 'with', 'when', 'current', 'state', 'not', 'system', 'this', 'change', 'was', 'some', 'where', 'interaction', 'may', 'has', 'have', 'text', 'are', 'can', 'key', 'also', 'command', 'emacs', 'application', 'use', 'window', 'they', 'error', 'such', 'does', 'way', 'used']], ['2007 in music', 'Squilly', 1169248845, 45652, ['music', 'that', 'place', 'the', 'year', '2007', 'british', 'canadian', 'country', 'albums', 'released', 'january', 'for', 'new', 'john', 'and', 'are', 'february', 'festival', 'will', 'tour', 'after', 'years', 'release', 'band', 'annual', 'awards', 'may', 'his', 'single', 'from', 'her', 'album', 'best', 'with', 'producer', 'record', 'song', 'their', 'rock', 'first', 'musical', 'back', 'was', 'american', 'march', 'musician', 'indefinite', 'hiatus', 'announces', 'concert', 'april', 'genesis', 'studio', 'billboard', 'held', 'selling', 'drummer', 'guitarist', 'august', 'since', 'singer', 'linkin', 'park', '000', 'bands', 'june', 'july', 'duran', 'september', 'bassist', 'october', 'conductor', 'electronic', 'november', 'vocalist', 'pianist', 'december', 'soprano', 'tenor', 'jazz', 'composer', 'songwriter']], ['List of video games with time travel', 'Rockfang', 1234110556, 2344, []], ['2008 in music', 'Ba11innnn', 1217641857, 107605, ['and', '2008', 'music', 'year', 'was', 'the', 'record', 'sales', 'united', 'with', 'since', 'british', 'canadian', 'new', 'rock', 'country', 'jazz', 'january', 'her', 'concert', 'pianist', 'concerto', 'violin', 'festival', 'february', 'day', 'australia', 'their', 'first', 'australian', 'years', 'that', 'for', 'wins', 'album', 'best', 'selling', 'producer', 'annual', 'takes', 'place', 'song', 'artist', 'guitarist', 'band', 'his', 'international', 'held', 'march', 'tour', 'musician', 'from', 'after', 'april', 'single', 'number', 'top', 'billboard', 'hot', '100', 'female', 'solo', 'you', 'studio', 'week', 'london', 'may', 'american', 'show', 'june', 'park', 'which', 'released', 'release', 'july', 'september', 'august', 'singer', 'saxophonist', 'dave', 'one', 'vocalist', 'due', 'debut', 'orchestra', 'october', 'november', 'composer', 'last', 'conductor', 'december', 'musical', 'weeks', 'heart', 'attack', 'cancer', 'trumpeter', 'songwriter', 'drummer', 'folk', 'jamaican', 'blues']], ['Semaphore (programming)', 'Edcolins', 1144850850, 7616, ['semaphore', 'variable', 'used', 'resource', 'processes', 'system', 'this', 'critical', 'section', 'and', 'process', 'the', 'that', 'for', 'are', 'available', 'with', 'operations', 'free', 'wait', 'semaphores', 'their', 'use', 'from', 'which', 'called', 'dijkstra', 'when', 'has', 'rooms', 'one', 'student', 'time', 'students', 'room', 'they', 'using', 'only', 'number', 'them', 'can', 'not', 'value', 'empty', 'there', 'waiting', 'resources', 'may', 'release', 'than', 'problem', 'operation', 'its', 'signal', 'queue', 'producer', 'consumer', 'emptycount', 'fullcount', 'usequeue', 'producers', 'mutex', 'task']], ["Wake Forest Demon Deacons men's soccer", 'Rebajc3', 1260577388, 26745, ['the', 'wake', 'forest', 'deacons', 'team', 'ncaa', 'their', '2007', 'all', 'acc', 'first', 'season', 'coach', 'and', '2008', '2009', '2015', '2017', '2016', 'players', 'plays', 'for', 'mls', 'usl', 'united', '2013']]]
