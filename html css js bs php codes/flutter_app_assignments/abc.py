import ast
district = '''24 Paraganas
8TH LANEBHABINIPUR GANJAM
Adilabad
Agra
ALANGIRI
Aligarh
ALIPORE
Alirajpur Katthiwada
Ambedkar Nagar
Amethi
Amreli
AMROHA
Ananthapur
Angul
Antagarh
ARARIA
Arwal
Asansol
ASHOK NAGAR
AURAIYA
AURANGABAD
AURANGABAD(BH)
Azamgarh
Badaun
Baduria
BAGHI SHIMLA
BAKSA
BALAGHAT
Balangir
Balasore
Baleshwar
Baleswar
Balichak
Ballia
Baloda Bazar
Balrampur
Bamnala
Banarpal
BANKA
BANKIPORE
BANKIPORE PATNA
Bankura
Bansada
Barabanki
BARDHAMAN
BAREILLY
Bareily
Bargarh
BARKOLA
Barpeta
Barrackpur
Barwala
BASTAR
BAZAR SAMITI PATNA
Begusarai
BEMETARA
Betul
Bhadrak
Bhagalpur
Bhanjanagar
Bhanupratappur
Bhind
BHOJPUR
Bhopal
Bhubaneshwar
Bhubaneswar
Biharsharif
BIJAPUR
Bijnor
BILASPUR
BIRBHUM
Bokaro
Bongaigaon
Brahmapur
Bulandshahr
Burdwan
busun
BUXAR
Cachar
CALCUTTA
CHAITAL
Champua
Chandabali
Chandauli
CHANDRA
Chandrapur
Chatra
CHENNAI
Chhatarpur
Chinsurah Magra
CHIRAIA
COIMBATORE
Colliery
COOCH BEHAR
CUDDALORE
Cuttack
Cuttack Sadar
Dakshin Dinajpur
Damoh
DANAPUR
DANTEWADA
Darbhanga
Darjiling
Darrang
Datia
Debagarh
DEBAI
DEOGHAR
Deoria
dewas
DHAMTARI
Dhanbad
dhar
Dhemaji
Dhenkanal
DHERUA
Dhubri
Dibrugarh
DINDIGUL
Domjur
DUMKA
DURG
DURGAPUR
EAST CHAMPARAN
EAST DELHI
EAST GODAVARI
EAST MIDNAPORE
East Singhbhum
East Singhbum
Egra
ERODE
Etah
Etawah
Faizabad
Faridabad
Farrukhabad
Fatehpur
Firozabad
Gajapati
Ganjam
GARHWA
Garhwa Jharkhand
GARIABAND
Gautam Buddha Nagar
GAYA
GB Nagar
GHATSHILA
Ghaziabad
Ghazipur
GIRIDH
GIRIDIH
Goalpara
GODDA
Golaghat
Gonda
GOPALGANJ
Gorakhpur
Gumla
GUNTUR
GUSHKARA NEW TOWN
GUWAHATI
Gwalior
Hamirpur
Hanamkonda
Hapur
Hardoi
hathras
Hathtas
HAZARI BAGH
HAZARIBAG
Hazaribagh
Hazaribaghh
Hojai
Hooghly
HOWRAH
Hyderabad
indore
Jagatsinghapur
Jagatsinghapur JAGATSINGHPUR
Jagdalpur
Jajapur
Jajpur
Jalpaiguri
Jamsedpur
Jamshedpur
JAMTARA
Jamui
Jangipur
Janjgir Champa
Jashpur
Jaunpur
Jehanabad
Jhansi
Jhargram
Jharsuguda
Jorhat
Jyotiba Phule Nagar
K.V.Rangareddy
Kaimur
Kalahandi
kali mandir,
Kalimela
Kamrup
KAMRUP METROPOLITAN
Kanchipuram
Kanchrapara
KANDHAMAL
KANKARBAGH PATNA
KANKER
Kanpur
Kanpur Dehat
Kanpur Nagar
Karbi Anglong
Karimganj
Karur
Kasganj
Katihar
KAWARDHA
Kendrapara
Kendujhar
Kendujhar Sadar
KEUT KHALISA
KHAGARIA
KHARAGON
Kharagpur
KHARGONE
Kharsodkalan Ujjain
Kheri
Khorda
Khordha
Khunti
Kishanganj
KODERMA
Kokrajhar
Kolkata
Kondagaon
Koraput
KORBA
KORIYA
KRISHNA
Krodha
Kuchaikote
Kuwarpur hathras
LADPUR HATHRAS
LAKHISARAI
Lalgola
LATEHAR
LOHARDAGA
Lucknow
Madhepura
MADHU BAN
Madhubani
Madurai
MAHASAMUND
Mahoba
Mainpuri
MAKSI
MALDA
MALIA
MALINCHA
Malkangiri
Mandsaur
Marigaon
MARKANDA
Mathura
Mau
Mayurbhanj
Medak
Medinipur
MEDINIPUR,KHARAGPUR
Meerut
MIDNAPORE
Midnapore East
Midnapore West
MIDNAPUR
Mirzapur
Moradabad
MORENA
Motihari
MUNGER
Murshidabad
Muzaffarnagar
Muzaffarpur
Nabadwip
Nadia
Nagaon
NAGAR KURNOOL
NAGRIYA NANDRAMHATHRAS
NALANDA
Nalbari
NAMAKKAL
NARAYANPUR
NAWADA
NAWADAH
Nayagarh
Nearby OrlovHoteNoida Gauta Noida
NELLORE
New Delhi
Nizamabad
Noida
NORTH 24 PARGANAS
North Dinajpur
NORTH TWENTY FOUR PARGANAS
NORTH WEST DELHI
Nuapada
NULL
Ojhra khargone
Pakhanjur
PAKUR
PALAMAU
Palamu
Paschim Bardhaman
Paschim Medinipur
Patan
Patna
PATNA SADAR
PATNA SADAR PATNA
Pilibhit
Prakasam
Prayagraj
PUDUKKOTTAI
Purba Bardhaman
Purba Medinipur
Puri
Purnia
PURULIA
Raebareli
RAIGARH
RAIPUR
Raisen
RAJGARH
RAJNANDGAON
RAMGARH
Ramnagar
Rampur
Ranchi
RANGAREDDY
Raxaul
Rayagada
rewa
ROHTAS
Sabalpur Dhanbad
Saharanpur
SAHARSA
Sahebganj
Sahibganj
SALEM
Samastipur
Sambalpur
Sambhal
SANDAPARA
Sant Kabir Nagar
Sant ravidas Nagar
Saraikela
Saraikela Kharsawan
Saran
Satna
Seraikela Kharsawan
SERAIKELA-KHARSAWAN
Serampur Uttarpara
Shahpur
SHAMLI
SHEIKHPURA
Sheohar
Shivpuri
SIDDHARTHNAGAR
SIDDIPET
SILCHAR
Siliguri
Simdega
SINGHBHUM
Sitamarhi
Sitapur
SIVAGANGA
Sivasagar
Siwan
Sonapur
Sonarpur
Sonbhadra
Sonitpur
Soro
SOUTH 24 PARGANAS
SOUTH DELHI
SRI MADHOJI MILLS
SRIKAKULAM
Sultanpur
Sundargarh
Sundergarh
Supaul
Surajpur
SURGUJA
Tensa
Tezpur
Thakurganj
THENI
Tihidi
TIKAMGARH
Tinsukia
TIRUCHIRAPPALLI
Tirunelveli
TIRUPPUR
TIRUVALLUR
TIRUVANNAMALAI
TOLLYGUNGE
TUTICORIN
ujjain
Unnao
Uttar Dinajpur
Vaishali
Varanasi
VELLORE
VIDHISHA
vidisha
VILLUPURAM
VIRUDHUNAGAR
VISAKHAPATNAM
VIZIANAGARAM
Warangal
West Champaran
WEST DELHI
WEST GODAVARI
West Midnapore
west midnapore kharagpur
WEST SINGHBHUM'''
text = district.split('\n')

for i in range(len(text)):
    txt = '<option value="'+text[i]+'">'+text[i]+'</option>'
    print(txt)