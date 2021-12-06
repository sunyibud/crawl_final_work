import pygal_maps_world.maps

world_map_chart = pygal_maps_world.maps.World()
world_map_chart.title = "世界范围内的数据采集"
world_map_chart.add("600+", {
    'us': 8714,
    'cn': 2831,
    'in': 2402,  # 印度
    'gb': 1392,  # United Kingdom，英国
    'de': 1139,  # 德国
    'br': 998,
    'ca': 901,
    'fr': 830,  # 法国
    'ru': 821,  # 俄国
    'at': 629,
})
world_map_chart.add("30+", {
    "jp": 523,
    "hk": 234,
    "tw": 243,
    "it": 334,
    "kr": 323,
    "mo": 300,
    "ca": 245,
    "br": 123,
    "th": 32,
    "ar": 31,
    "co": 36,
    "pt": 45,
    "pk": 47,
    "pl": 48,
    "bd": 40,
    "se": 30,
    "tr": 34,
    "ve": 32,
    "gb": 32,
})
world_map_chart.add("30-", {
    "nl": 3,
    "hu": 1,
    "cl": 23,
    "ph": 21,
    "my": 12,
    "kr": 3,
    "uy": 1,
    "ro": 1,
    "eg": 1,
    "ke": 1,
    "kp": 3,
    "cz": 6,
    "sk": 8,
    "mg": 2,
})
world_map_chart.render_to_file('author_map.svg')

'''
code	Country
 
ad	Andorra
ae	United Arab Emirates
af	Afghanistan
al	Albania
am	Armenia
ao	Angola
aq	Antarctica
ar	Argentina
at	Austria
au	Australia
az	Azerbaijan
ba	Bosnia and Herzegovina
bd	Bangladesh
be	Belgium
bf	Burkina Faso
bg	Bulgaria
bh	Bahrain
bi	Burundi
bj	Benin
bn	Brunei Darussalam
bo	Bolivia, Plurinational State of
br	Brazil
bt	Bhutan
bw	Botswana
by	Belarus
bz	Belize
ca	Canada
cd	Congo, the Democratic Republic of the
cf	Central African Republic
cg	Congo
ch	Switzerland
ci	Cote d’Ivoire
cl	Chile
cm	Cameroon
cn	China
co	Colombia
cr	Costa Rica
cu	Cuba
cv	Cape Verde
cy	Cyprus
cz	Czech Republic
de	Germany
dj	Djibouti
dk	Denmark
do	Dominican Republic
dz	Algeria
ec	Ecuador
ee	Estonia
eg	Egypt
eh	Western Sahara
er	Eritrea
es	Spain
et	Ethiopia
fi	Finland
fr	France
ga	Gabon
gb	United Kingdom
ge	Georgia
gf	French Guiana
gh	Ghana
gl	Greenland
gm	Gambia
gn	Guinea
gq	Equatorial Guinea
gr	Greece
gt	Guatemala
gu	Guam
gw	Guinea-Bissau
gy	Guyana
hk	Hong Kong
hn	Honduras
hr	Croatia
ht	Haiti
hu	Hungary
id	Indonesia
ie	Ireland
il	Israel
in	India
iq	Iraq
ir	Iran, Islamic Republic of
is	Iceland
it	Italy
jm	Jamaica
jo	Jordan
jp	Japan
ke	Kenya
kg	Kyrgyzstan
kh	Cambodia
kp	Korea, Democratic People’s Republic of
kr	Korea, Republic of
kw	Kuwait
kz	Kazakhstan
la	Lao People’s Democratic Republic
lb	Lebanon
li	Liechtenstein
lk	Sri Lanka
lr	Liberia
ls	Lesotho
lt	Lithuania
lu	Luxembourg
lv	Latvia
ly	Libyan Arab Jamahiriya
ma	Morocco
mc	Monaco
md	Moldova, Republic of
me	Montenegro
mg	Madagascar
mk	Macedonia, the former Yugoslav Republic of
ml	Mali
mm	Myanmar
mn	Mongolia
mo	Macao
mr	Mauritania
mt	Malta
mu	Mauritius
mv	Maldives
mw	Malawi
mx	Mexico
my	Malaysia
mz	Mozambique
na	Namibia
ne	Niger
ng	Nigeria
ni	Nicaragua
nl	Netherlands
no	Norway
np	Nepal
nz	New Zealand
om	Oman
pa	Panama
pe	Peru
pg	Papua New Guinea
ph	Philippines
pk	Pakistan
pl	Poland
pr	Puerto Rico
ps	Palestine, State of
pt	Portugal
py	Paraguay
re	Reunion
ro	Romania
rs	Serbia
ru	Russian Federation
rw	Rwanda
sa	Saudi Arabia
sc	Seychelles
sd	Sudan
se	Sweden
sg	Singapore
sh	Saint Helena, Ascension and Tristan da Cunha
si	Slovenia
sk	Slovakia
sl	Sierra Leone
sm	San Marino
sn	Senegal
so	Somalia
sr	Suriname
st	Sao Tome and Principe
sv	El Salvador
sy	Syrian Arab Republic
sz	Swaziland
td	Chad
tg	Togo
th	Thailand
tj	Tajikistan
tl	Timor-Leste
tm	Turkmenistan
tn	Tunisia
tr	Turkey
tw	Taiwan (Republic of China)
tz	Tanzania, United Republic of
ua	Ukraine
ug	Uganda
us	United States
uy	Uruguay
uz	Uzbekistan
va	Holy See (Vatican City State)
ve	Venezuela, Bolivarian Republic of
vn	Viet Nam
ye	Yemen
yt	Mayotte
za	South Africa
zm	Zambia
zw	Zimbabwe
'''
