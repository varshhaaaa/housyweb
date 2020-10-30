from flask import Flask,render_template,request
import numpy as np
import pickle
model1=pickle.load(open('final_model_pickle.pickle','rb'))
model2=pickle.load(open('delhifinal.pickle','rb'))
model3=pickle.load(open('mumbai_modelfinal.pickle','rb'))

locations3=["area","bhk",'Airoli', 'Andheri East', 'Andheri West',
       'Bandra West', 'Belapur', 'Bhandup West', 'Bhiwandi', 'Boisar',
       'Borivali East', 'Borivali West', 'Chembur', 'Dahisar', 'Dahisar East',
       'Dahisar West', 'Dattapada', 'Dombivali', 'Dombivali East',
       'Dombivli (West)', 'Dronagiri', 'Ghansoli', 'Ghatkopar West',
       'Goregaon', 'Goregaon East', 'Goregaon West', 'Jogeshwari West', 'Juhu',
       'Kalwa', 'Kalyan West', 'Kamothe', 'Kandivali East', 'Kandivali West',
       'Kanjurmarg', 'Karanjade', 'Kharghar', 'Koper Khairane', 'Kurla',
       'Magathane', 'Malad East', 'Malad West', 'Mira Road East',
       'Mira Road and Beyond', 'Mulund East', 'Mulund West', 'Nala Sopara',
       'Nerul', 'Panvel', 'Parel', 'Powai', 'Sanpada', 'Santacruz East',
       'Seawoods', 'Sector 17 Ulwe', 'Sector 20 Kharghar', 'Taloja', 'Thane',
       'Thane West', 'Ulwe', 'Vasai', 'Vasai West', 'Ville Parle East',
       'Virar', 'Wadala', 'Worli', 'others']

locations2=["area","bhk","bath",'Alaknanda', 'Budh', 'Chhattarpur',
       'Chittaranjan', 'Commonwealth Games Village 2010',
       'Dilshad Colony, Dilshad Garden', 'Dilshad Garden', 'Dwarka',
       'Hauz Khas', 'Janakpuri Block A3', 'Kailash', 'KalkaJi', 'Kalkaji',
       'Karol', 'Khanpur, Madangir', 'Krishna Nagar-Safdarjung Enclave',
       'Lajpat', 'Laxmi Nagar', 'Mahavir', 'Malviya', 'Manglapuri', 'Mehrauli',
       'Mohan Garden, Razapur Khurd', 'Narela', 'New Friends Colony', 'Okhla',
       'Paschim', 'Patel', 'Punjabi Bagh', 'Punjabi Bagh East',
       'Punjabi Bagh West', 'Rohini', 'Safdarjung', 'Saket', 'Sarita',
       'Shahdara', 'Sheikh', 'Sitaram Bazar, Chandni Chowk', 'Sultanpur',
       'Taj Enclave, Khairatabad', 'Uttam', 'Vasant', 'Vasundhara', 'others']
locations1=['bath', 'bhk', 'area', ' Devarachikkanahalli', '1st Block Jayanagar', '1st Phase JP Nagar', '2nd Phase Judicial Layout', '2nd Stage Nagarbhavi', '5th Phase JP Nagar', '6th Phase JP Nagar', '7th Phase JP Nagar', '8th Phase JP Nagar', '9th Phase JP Nagar', 'AECS Layout', 'Abbigere', 'Akshaya Nagar', 'Ambalipura', 'Ambedkar Nagar', 'Amruthahalli', 'Anandapura', 'Ananth Nagar', 'Anekal', 'Anjanapura', 'Ardendale', 'Arekere', 'Attibele', 'BEML Layout', 'BTM 2nd Stage', 'BTM Layout', 'Babusapalaya', 'Badavala Nagar', 'Balagere', 'Banashankari', 'Banashankari Stage II', 'Banashankari Stage III', 'Banashankari Stage V', 'Banashankari Stage VI', 'Banaswadi', 'Banjara Layout', 'Bannerghatta', 'Bannerghatta Road', 'Basavangudi', 'Basaveshwara Nagar', 'Battarahalli', 'Begur', 'Begur Road', 'Bellandur', 'Benson Town', 'Bharathi Nagar', 'Bhoganhalli', 'Billekahalli', 'Binny Pete', 'Bisuvanahalli', 'Bommanahalli', 'Bommasandra', 'Bommasandra Industrial Area', 'Bommenahalli', 'Brookefield', 'Budigere', 'CV Raman Nagar', 'Chamrajpet', 'Chandapura', 'Channasandra', 'Chikka Tirupathi', 'Chikkabanavar', 'Chikkalasandra', 'Choodasandra', 'Cooke Town', 'Cox Town', 'Cunningham Road', 'Dasanapura', 'Dasarahalli', 'Devanahalli', 'Dodda Nekkundi', 'Doddaballapur', 'Doddakallasandra', 'Doddathoguru', 'Domlur', 'Dommasandra', 'EPIP Zone', 'Electronic City', 'Electronic City Phase II', 'Electronics City Phase 1', 'Frazer Town', 'GM Palaya', 'Garudachar Palya', 'Giri Nagar', 'Gollarapalya Hosahalli', 'Gottigere', 'Green Glen Layout', 'Gubbalala', 'Gunjur', 'HBR Layout', 'HRBR Layout', 'HSR Layout', 'Haralur Road', 'Harlur', 'Hebbal', 'Hebbal Kempapura', 'Hegde Nagar', 'Hennur', 'Hennur Road', 'Hoodi', 'Horamavu Agara', 'Horamavu Banaswadi', 'Hormavu', 'Hosa Road', 'Hosakerehalli', 'Hoskote', 'Hosur Road', 'Hulimavu', 'ISRO Layout', 'ITPL', 'Iblur Village', 'Indira Nagar', 'JP Nagar', 'Jakkur', 'Jalahalli', 'Jalahalli East', 'Jigani', 'Judicial Layout', 'KR Puram', 'Kadubeesanahalli', 'Kadugodi', 'Kaggadasapura', 'Kaggalipura', 'Kaikondrahalli', 'Kalena Agrahara', 'Kalyan nagar', 'Kambipura', 'Kammanahalli', 'Kammasandra', 'Kanakapura', 'Kanakpura Road', 'Kannamangala', 'Karuna Nagar', 'Kasavanhalli', 'Kasturi Nagar', 'Kathriguppe', 'Kaval Byrasandra', 'Kenchenahalli', 'Kengeri', 'Kengeri Satellite Town', 'Kereguddadahalli', 'Kodichikkanahalli', 'Kodigehaali', 'Kodihalli', 'Kogilu', 'Konanakunte', 'Koramangala', 'Kothannur', 'Kothanur', 'Kudlu', 'Kudlu Gate', 'Kumaraswami Layout', 'Kundalahalli', 'LB Shastri Nagar', 'Laggere', 'Lakshminarayana Pura', 'Lingadheeranahalli', 'Magadi Road', 'Mahadevpura', 'Mahalakshmi Layout', 'Mallasandra', 'Malleshpalya', 'Malleshwaram', 'Marathahalli', 'Margondanahalli', 'Marsur', 'Mico Layout', 'Munnekollal', 'Murugeshpalya', 'Mysore Road', 'NGR Layout', 'NRI Layout', 'Nagarbhavi', 'Nagasandra', 'Nagavara', 'Nagavarapalya', 'Narayanapura', 'Neeladri Nagar', 'OMBR Layout', 'Old Airport Road', 'Old Madras Road', 'Padmanabhanagar', 'Pai Layout', 'Panathur', 'Parappana Agrahara', 'Pattandur Agrahara', 'Poorna Pragna Layout', 'Prithvi Layout', 'R.T. Nagar', 'Rachenahalli', 'Raja Rajeshwari Nagar', 'Rajaji Nagar', 'Rajiv Nagar', 'Ramagondanahalli', 'Ramamurthy Nagar', 'Rayasandra', 'Sahakara Nagar', 'Sanjay nagar', 'Sarakki Nagar', 'Sarjapur', 'Sarjapur  Road', 'Sarjapura - Attibele Road', 'Sector 2 HSR Layout', 'Sector 7 HSR Layout', 'Seegehalli', 'Shampura', 'Shivaji Nagar', 'Singasandra', 'Somasundara Palya', 'Sompura', 'Sonnenahalli', 'Subramanyapura', 'Sultan Palaya', 'TC Palaya', 'Talaghattapura', 'Thanisandra', 'Thigalarapalya', 'Thubarahalli', 'Thyagaraja Nagar', 'Tindlu', 'Tumkur Road', 'Ulsoor', 'Uttarahalli', 'Varthur', 'Varthur Road', 'Vasanthapura', 'Vidyaranyapura', 'Vijayanagar', 'Vishveshwarya Layout', 'Vishwapriya Layout', 'Vittasandra', 'Whitefield', 'Yelachenahalli', 'Yelahanka', 'Yelahanka New Town', 'Yelenahalli', 'Yeshwanthpur']
def fmodel1 (bath,bhk,area,location):

    p=np.zeros(240)
    p[0]=bath
    p[1]=bhk
    p[2]=area
    for i in range(3,240):
        if locations1[i]==location:
            p[i]=1

    return model1.predict([p])
def fmodel2 (bath,bhk,area,location):
    p=np.zeros(47)
    p[2]=bath
    p[1]=bhk
    p[0]=area
    for i in range(3,47):
        if locations2[i]==location:
            p[i]=1

    return model2.predict([p])
def fmodel3 (bhk,area,location):
    p=np.zeros(66)

    p[1]=bhk
    p[0]=area
    for i in range(2,66):
        if locations3[i]==location:
            p[i]=1

    return model3.predict([p])
app=Flask(__name__)
@app.route('/')
def home():

    return render_template('index.html')

@app.route('/select',methods=['POST'])
def select():
    city=request.form["city"]
    if city=="Banglore":
        return render_template('index1.html')
    if city=="Delhi":
        return render_template('index2.html')
    if city=="Mumbai":
        return render_template('index3.html')

@app.route('/predictB',methods=['POST'])
def predictB():
    bath=request.form["bath"]
    bhk=request.form["bhk"]
    area=request.form["area"]
    loc=request.form["loc"]
    return render_template('index1.html',predict_values="predicted amount in lakhs :{}".format(str((fmodel1(bath,bhk,area,loc)[0]))))

@app.route('/predictD',methods=['POST'])
def predictD():
    bath=request.form["bath"]
    bhk=request.form["bhk"]
    area=request.form["area"]
    loc=request.form["loc"]
    return render_template('index2.html',predict_values="predicted amount in lakhs :{}".format(str((fmodel2(bath,bhk,area,loc)[0]))))

@app.route('/predictM',methods=['POST'])
def predictM():

    bhk=request.form["bhk"]
    area=request.form["area"]
    loc=request.form["loc"]
    return render_template('index3.html',predict_values="predicted amount in lakhs :{}".format(str((fmodel3(bhk,area,loc)[0]))))

if __name__=='__main__':
    app.run(debug=True)
