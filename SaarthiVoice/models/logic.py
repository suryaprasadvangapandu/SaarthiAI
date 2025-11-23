"""
Comprehensive rule-based intent detection and guidance system for SaarthiAI
Provides detailed information on health, government schemes, and climate safety
"""

class IntentEngine:
    """
    Advanced rule-based intent detection engine with comprehensive knowledge base
    Analyzes user queries and provides detailed professional guidance
    """
    
    def __init__(self):
        # Expanded knowledge base with more keywords
        self.health_keywords = [
            # Specific symptoms and medical conditions only (avoid broad terms)
            'fever', 'temperature', 'sick', 'pain', 'headache', 'cold', 'flu',
            'cough', 'vomit', 'diarrhea', 'injury', 'wound', 'burn', 'bleeding',
            'stomach', 'chest', 'breathing', 'dizzy', 'nausea', 'rash', 'allergy',
            'infection', 'dengue', 'malaria', 'typhoid', 'diabetes', 'pressure',
            'fracture', 'sprain', 'swelling', 'bite', 'sting', 'faint',
            # Hindi
            'बुखार', 'दर्द', 'सिरदर्द', 'खांसी', 'ठंड', 'पेट', 'चोट', 'जलना',
            'खून', 'उल्टी', 'दस्त', 'सांस', 'चक्कर', 'एलर्जी', 'संक्रमण',
            # Telugu  
            'జ్వరం', 'నొప్పి', 'తలనొప్పి', 'దగ్గు', 'జలుబు', 'కడుపు', 'గాయం', 'కాలుట',
            'రక్తం', 'వాంతులు', 'విరేచనాలు', 'శ్వాస', 'అలెర్జీ'
        ]
        
        self.scheme_keywords = [
            # Scheme-related
            'scheme', 'yojana', 'application', 'benefit', 'subsidy', 'grant',
            'pension', 'ration', 'card', 'apply', 'form', 'government', 'welfare',
            'ayushman', 'awas', 'ujjwala', 'scholarship', 'loan', 'farmers',
            'widow', 'disability', 'employment', 'skill', 'training', 'mudra',
            'pmjdy', 'pmksy', 'pmfby', 'documents', 'eligibility',
            # Hindi
            'योजना', 'आवेदन', 'लाभ', 'पेंशन', 'राशन', 'सब्सिडी', 'कार्ड',
            'छात्रवृत्ति', 'ऋण', 'किसान', 'विधवा', 'रोजगार', 'प्रशिक्षण',
            # Telugu
            'పథకం', 'దరఖాస్తు', 'ప్రయోజనం', 'పెన్షన్', 'రేషన్', 'సబ్సిడీ',
            'స్కాలర్షిప్', 'రుణం', 'రైతు', 'ఉద్యోగం'
        ]
        
        self.climate_keywords = [
            # Climate & disaster
            'heatwave', 'flood', 'warning', 'rain', 'storm', 'cyclone', 'tornado',
            'drought', 'hot', 'cold', 'weather', 'disaster', 'alert', 'emergency',
            'lightning', 'earthquake', 'tsunami', 'landslide', 'fire', 'smoke',
            'pollution', 'air', 'water', 'evacuation', 'shelter', 'rescue',
            # Hindi
            'गर्मी', 'बाढ़', 'चेतावनी', 'बारिश', 'तूफान', 'सूखा', 'आंधी',
            'बिजली', 'भूकंप', 'आग', 'प्रदूषण', 'निकासी',
            # Telugu
            'వేడి', 'వరద', 'హెచ్చరిక', 'వర్షం', 'తుఫాను', 'కరువు', 'మెరుపు',
            'భూకంపం', 'అగ్ని', 'కాలుష్యం', 'తరలింపు'
        ]
    
    def detect_intent(self, text):
        """Detect user intent from text"""
        text_lower = text.lower()
        
        if any(keyword in text_lower for keyword in self.health_keywords):
            return 'health'
        if any(keyword in text_lower for keyword in self.scheme_keywords):
            return 'schemes'
        if any(keyword in text_lower for keyword in self.climate_keywords):
            return 'climate'
        
        return 'general'
    
    def get_guidance(self, text, language='en'):
        """Generate comprehensive guidance based on intent and language"""
        intent = self.detect_intent(text)
        guidance = self._generate_response(intent, text, language)
        
        return {
            'intent': intent,
            'text': text,
            'guidance': guidance,
            'language': language
        }
    
    def _generate_response(self, intent, query, language):
        """Generate detailed response based on intent"""
        if intent == 'health':
            return self._get_health_guidance(query, language)
        elif intent == 'schemes':
            return self._get_scheme_guidance(query, language)
        elif intent == 'climate':
            return self._get_climate_guidance(query, language)
        else:
            return self._get_general_guidance(language)
    
    def _get_health_guidance(self, query, language):
        """Provide comprehensive health and medical guidance"""
        query_lower = query.lower()
        
        # FEVER - Detailed guidance
        if any(word in query_lower for word in ['fever', 'बुखार', 'జ్వరం', 'temperature']):
            if language == 'hi':
                return """बुखार - विस्तृत प्राथमिक उपचार गाइड:

तत्काल कार्रवाई:
1. तापमान मापें (सामान्य: 98.6°F / 37°C)
2. रोगी को पूरी तरह आराम दें
3. कमरे को ठंडा और हवादार रखें
4. हल्के, सूती कपड़े पहनाएं

उपचार विधि:
5. ठंडे पानी की पट्टी माथे पर रखें
6. हर 2-3 घंटे में स्पंज बाथ दें  
7. बहुत सारे तरल पदार्थ - पानी, नारियल पानी, ORS
8. पेरासिटामोल 500mg (वयस्क - डॉक्टर से पूछें)
9. भारी भोजन न दें, हल्का सुपाच्य भोजन दें

खतरे के संकेत - तुरंत अस्पताल जाएं:
- 103°F (39.4°C) से ऊपर बुखार
- 3 दिन से ज्यादा बुखार
- गंभीर सिरदर्द या उल्टी
- बेहोशी या भ्रम की स्थिति
- सांस लेने में कठिनाई
- शिशुओं में कोई भी बुखार (तुरंत डॉक्टर)

रोकथाम:
- स्वच्छता बनाए रखें
- भीड़भाड़ वाली जगहों से बचें
- पौष्टिक भोजन और पानी पिएं

आपातकालीन नंबर: 102 (एम्बुलेंस), 104 (हेल्पलाइन)"""
            
            elif language == 'te':
                return """జ్వరం - సమగ్ర ప్రాథమిక చికిత్స మార్గదర్శి:

తక్షణ చర్య:
1. ఉష్ణోగ్రత కొలవండి (సాధారణ: 98.6°F / 37°C)
2. రోగికి పూర్తి విశ్రాంతి ఇవ్వండి
3. గదిని చల్లగా మరియు గాలితో ఉంచండి
4. తేలికపాటి, పత్తి బట్టలు ధరించండి

చికిత్స పద్ధతి:
5. చల్లని నీటి వట్టిని నుదుటిపై ఉంచండి
6. ప్రతి 2-3 గంటలకు స్పాంజ్ స్నానం చేయించండి
7. చాలా ద్రవాలు - నీరు, కొబ్బరి నీరు, ORS
8. పారాసిటమాల్ 500mg (పెద్దలకు - వైద్యుడిని అడగండి)
9. భారీ ఆహారం ఇవ్వకండి, తేలికపాటి జీర్ణమయ్యే ఆహారం ఇవ్వండి

ప్రమాద సంకేతాలు - వెంటనే ఆసుపత్రికి వెళ్లండి:
- 103°F (39.4°C) కంటే ఎక్కువ జ్వరం
- 3 రోజుల కంటే ఎక్కువ జ్వరం
- తీవ్రమైన తలనొప్పి లేదా వాంతులు
- స్పృహ కోల్పోవడం లేదా గందరగోళం
- శ్వాస తీసుకోవడంలో ఇబ్బంది
- శిశువులకు ఏదైనా జ్వరం (వెంటనే వైద్యుడు)

నివారణ:
- పరిశుభ్రతను కొనసాగించండి
- రద్దీ ఉన్న ప్రదేశాలను నివారించండి
- పోషకాహారం మరియు నీరు తాగండి

అత్యవసర నంబర్లు: 102 (అంబులెన్స్), 104 (హెల్ప్‌లైన్)"""
            
            else:
                return """FEVER - Comprehensive First Aid Guide:

Immediate Action:
1. Measure temperature (Normal: 98.6°F / 37°C)
2. Make patient rest completely
3. Keep room cool and well-ventilated
4. Wear light, cotton clothing

Treatment Method:
5. Apply cold water compress on forehead
6. Give sponge bath every 2-3 hours
7. Plenty of fluids - water, coconut water, ORS
8. Paracetamol 500mg (adults - consult doctor)
9. No heavy meals, give light digestible food

Danger Signs - Go to Hospital Immediately:
- Fever above 103°F (39.4°C)
- Fever lasting more than 3 days
- Severe headache or vomiting
- Loss of consciousness or confusion
- Difficulty breathing
- Any fever in infants (immediate doctor visit)

Prevention:
- Maintain hygiene
- Avoid crowded places
- Eat nutritious food and drink water

Emergency Numbers: 102 (Ambulance), 104 (Helpline)"""
        
        # COLD/COUGH - Detailed guidance
        if any(word in query_lower for word in ['cold', 'cough', 'खांसी', 'ठंड', 'దగ్గు', 'జలుబు']):
            if language == 'hi':
                return """सर्दी और खांसी - संपूर्ण उपचार गाइड:

लक्षण और प्रकार:
- सूखी खांसी: बलगम नहीं
- गीली खांसी: बलगम के साथ
- सामान्य सर्दी: नाक बहना, छींक, हल्का बुखार
- फ्लू: तेज बुखार, शरीर दर्द, थकान

घरेलू उपचार:
1. कम से कम 7-8 घंटे आराम करें
2. गर्म पानी, हर्बल चाय, शहद-नींबू पानी पिएं
3. दिन में 2-3 बार भाप लें
4. गर्म नमक के पानी से गरारे करें (दिन में 3-4 बार)
5. शहद + अदरक का रस (1 चम्मच दिन में 3 बार)
6. शरीर को गर्म रखें, ठंड से बचें

दवाएं (डॉक्टर की सलाह के बाद):
- सूखी खांसी के लिए कफ सिरप
- नाक बहने के लिए एंटीहिस्टामाइन
- बुखार/शरीर दर्द के लिए पेरासिटामोल

डॉक्टर कब दिखाएं:
- 2 सप्ताह से अधिक खांसी
- खांसी/बलगम में खून
- सीने में दर्द या सांस लेने में कठिनाई
- तेज बुखार (102°F से ऊपर)
- लक्षण बिगड़ रहे हों

रोकथाम:
- बार-बार हाथ धोएं
- बीमार लोगों से दूर रहें
- ठंड में शरीर गर्म रखें
- विटामिन सी वाले खाद्य पदार्थ खाएं
- हमेशा पानी पीते रहें

आपातकालीन: 102, 104"""
            elif language == 'te':
                return """జలుబు మరియు దగ్గు - సంపూర్ణ చికిత్స మార్గదర్శి:

లక్షణాలు మరియు రకాలు:
- పొడి దగ్గు: కఫం లేదు
- తడి దగ్గు: కఫంతో
- సాధారణ జలుబు: ముక్కు కారడం, తుమ్ములు, తక్కువ జ్వరం
- ఫ్లూ: అధిక జ్వరం, శరీర నొప్పులు, అలసట

ఇంటి చికిత్స:
1. కనీసం 7-8 గంటలు విశ్రాంతి తీసుకోండి
2. వేడి నీరు, మూలికా టీ, తేనె-నిమ్మ నీరు త్రాగండి
3. రోజుకు 2-3 సార్లు ఆవిరి పీల్చండి
4. వేడి ఉప్పు నీటితో గార్గిల్ చేయండి (రోజుకు 3-4 సార్లు)
5. తేనె + అల్లం రసం (1 టీస్పూన్ రోజుకు 3 సార్లు)
6. శరీరాన్ని వెచ్చగా ఉంచండి, చలిని నివారించండి

మందులు (వైద్యుడి సలహా తర్వాత):
- పొడి దగ్గు కోసం కఫ్ సిరప్
- ముక్కు కారడం కోసం యాంటిహిస్టామైన్లు
- జ్వరం/శరీర నొప్పి కోసం పారాసిటమాల్

వైద్యుడిని ఎప్పుడు చూడాలి:
- 2 వారాల కంటే ఎక్కువ దగ్గు
- దగ్గు/కఫంలో రక్తం
- ఛాతీ నొప్పి లేదా శ్వాస తీసుకోవడంలో ఇబ్బంది
- అధిక జ్వరం (102°F కంటే ఎక్కువ)
- లక్షణాలు తీవ్రమవుతున్నాయి

నివారణ:
- తరచుగా చేతులు కడుక్కోండి
- అనారోగ్యంతో ఉన్న వ్యక్తులకు దూరంగా ఉండండి
- చలిలో శరీరాన్ని వెచ్చగా ఉంచండి
- విటమిన్ సి ఆహారాలు తినండి
- ఎల్లప్పుడూ హైడ్రేటెడ్ గా ఉండండి

అత్యవసరం: 102, 104"""
            else:
                return """COLD & COUGH - Complete Treatment Guide:

Symptoms & Types:
- Dry Cough: No mucus production
- Wet Cough: With phlegm/mucus  
- Common Cold: Runny nose, sneezing, mild fever
- Flu: High fever, body aches, fatigue

Home Treatment:
1. Rest at least 7-8 hours daily
2. Drink warm water, herbal tea, honey-lemon water
3. Steam inhalation 2-3 times daily
4. Gargle with warm salt water (3-4 times/day)
5. Honey + ginger juice (1 tsp 3 times/day)
6. Keep body warm, avoid cold exposure

Medications (After Doctor Consultation):
- Cough syrup for dry cough
- Antihistamines for runny nose
- Paracetamol for fever/body ache

When to See Doctor:
- Cough lasting more than 2 weeks
- Blood in cough/phlegm
- Chest pain or breathing difficulty
- High fever (above 102°F)
- Symptoms getting worse

Prevention:
- Wash hands frequently
- Avoid contact with sick people
- Keep body warm in cold weather
- Boost immunity with vitamin C foods
- Stay hydrated always

Emergency: 102, 104"""
        
        # STOMACH PROBLEMS
        if any(word in query_lower for word in ['stomach', 'diarrhea', 'vomit', 'पेट', 'दस्त', 'उल्टी', 'కడుపు', 'విరేచనాలు', 'వాంతులు']):
            if language == 'hi':
                return """पेट की समस्याएं - उपचार गाइड:

सामान्य समस्याएं:
1. दस्त (लूज मोशन)
2. उल्टी
3. फूड पॉइजनिंग
4. एसिडिटी/सीने में जलन
5. कब्ज

दस्त के लिए:
- ORS (ओरल रिहाइड्रेशन सॉल्यूशन) - सबसे जरूरी!
- चावल का पानी, नारियल पानी, छाछ
- BRAT आहार: केला, चावल, सेब की चटनी, टोस्ट
- तैलीय, मसालेदार भोजन से बचें
- प्रोबायोटिक्स (दही)
- बच्चों के लिए जिंक सप्लीमेंट

उल्टी के लिए:
- 2-3 घंटे तक कुछ न खाएं
- धीरे-धीरे पानी पिएं (थोड़ी मात्रा में)
- अदरक की चाय या नींबू पानी
- आरामदायक स्थिति में आराम करें
- तेज गंध से बचें

फूड पॉइजनिंग के लिए:
- भरपूर तरल पदार्थ (पानी, ORS)
- पूर्ण आराम
- 6-8 घंटे बाद हल्का भोजन
- गंभीर लक्षणों की निगरानी करें

खतरे के संकेत - डॉक्टर को दिखाएं:
- मल या उल्टी में खून
- गंभीर डीहाइड्रेशन (सूखा मुंह, पेशाब नहीं)
- पेट दर्द के साथ तेज बुखार
- 3 दिन से अधिक दस्त
- तरल पदार्थ पीने में असमर्थ

रोकथाम:
- साफ/उबला पानी पिएं
- खाने से पहले हाथ धोएं
- ताजा पका हुआ खाना खाएं
- भोजन का उचित भंडारण
- रसोई की अच्छी स्वच्छता

आपातकालीन: 102 (एम्बुलेंस)"""
            elif language == 'te':
                return """కడుపు సమస్యలు - చికిత్స మార్గదర్శి:

సాధారణ సమస్యలు:
1. విరేచనాలు (లూజ్ మోషన్స్)
2. వాంతులు
3. ఫుడ్ పాయిజనింగ్
4. యాసిడిటీ/గుండె మంట
5. మలబద్ధకం

విరేచనాల కోసం:
- ORS (ఓరల్ రీహైడ్రేషన్ సొల్యూషన్) - చాలా ముఖ్యం!
- బియ్యం నీరు, కొబ్బరి నీరు, మజ్జిగ
- BRAT ఆహారం: అరటిపండ్లు, బియ్యం, ఆపిల్ సాస్, టోస్ట్
- నూనె, మసాలా ఆహారం నివారించండి
- ప్రోబయోటిక్స్ (పెరుగు)
- పిల్లలకు జింక్ సప్లిమెంట్లు

వాంతుల కోసం:
- 2-3 గంటల పాటు ఏమీ తినవద్దు
- నీటిని నెమ్మదిగా తాగండి (చిన్న మొత్తాలు)
- అల్లం టీ లేదా నిమ్మ నీరు
- సౌకర్యవంతమైన స్థితిలో విశ్రాంతి తీసుకోండి
- బలమైన వాసనలను నివారించండి

ఫుడ్ పాయిజనింగ్ కోసం:
- పుష్కలంగా ద్రవాలు (నీరు, ORS)
- పూర్తి విశ్రాంతి
- 6-8 గంటల తర్వాత తేలికపాటి ఆహారం
- తీవ్ర లక్షణాలను పర్యవేక్షించండి

ప్రమాద సంకేతాలు - వైద్యుడిని చూడండి:
- మలం లేదా వాంతిలో రక్తం
- తీవ్ర నిర్జలీకరణం (పొడి నోరు, మూత్రవిసర్జన లేదు)
- కడుపు నొప్పితో అధిక జ్వరం
- 3 రోజుల కంటే ఎక్కువ విరేచనాలు
- ద్రవాలు తాగలేకపోవడం

నివారణ:
- శుభ్రమైన/ఉడికించిన నీరు త్రాగండి
- తినడానికి ముందు చేతులు కడుక్కోండి
- తాజాగా వండిన ఆహారం తినండి
- సరైన ఆహార నిల్వ
- మంచి వంటగది పరిశుభ్రత

అత్యవసరం: 102 (అంబులెన్స్)"""
            else:
                return """STOMACH PROBLEMS - Treatment Guide:

Common Issues:
1. Diarrhea (Loose motions)
2. Vomiting
3. Food Poisoning
4. Acidity/Heartburn
5. Constipation

For Diarrhea:
- ORS (Oral Rehydration Solution) - Most Important!
- Rice water, coconut water, buttermilk
- BRAT diet: Bananas, Rice, Applesauce, Toast
- Avoid oily, spicy foods
- Probiotics (curd/yogurt)
- Zinc supplements for children

For Vomiting:
- Stop eating for 2-3 hours
- Sip water slowly (small amounts)
- Ginger tea or lemon water
- Rest in comfortable position
- Avoid strong smells

For Food Poisoning:
- Plenty of fluids (water, ORS)
- Complete rest
- Light foods after 6-8 hours
- Monitor for severe symptoms

Danger Signs - See Doctor:
- Blood in stool or vomit
- Severe dehydration (dry mouth, no urination)
- High fever with stomach pain
- Diarrhea lasting more than 3 days
- Unable to keep fluids down

Prevention:
- Drink clean/boiled water
- Wash hands before eating
- Eat freshly cooked food
- Proper food storage
- Good kitchen hygiene

Emergency: 102 (Ambulance)"""
        
        # General Health Advice
        if language == 'hi':
            return """सामान्य स्वास्थ्य मार्गदर्शन:

प्राथमिक उपचार किट में रखें:
- बैंडेज, कॉटन, गॉज
- एंटीसेप्टिक क्रीम (बेटाडाइन)
- पेरासिटामोल, एंटासिड
- ओआरएस पाउडर
- थर्मामीटर
- साफ पानी

सामान्य लक्षण और उपचार:
1. सिरदर्द: आराम, पानी पिएं, पेरासिटामोल
2. चक्कर: लेट जाएं, पैर ऊपर करें
3. छोटी चोट: साफ करें, एंटीसेप्टिक लगाएं
4. मामूली जलना: ठंडे पानी में 10 मिनट रखें
5. नकसीर: आगे झुकें, नाक दबाएं

डॉक्टर कब दिखाएं:
- गंभीर दर्द या असहनीय लक्षण
- सांस लेने में परेशानी
- बेहोशी या भ्रम
- गंभीर चोट या रक्तस्राव
- बच्चों/बुजुर्गों में कोई भी गंभीर लक्षण

आपातकालीन नंबर:
- एम्बुलेंस: 102, 108
- स्वास्थ्य हेल्पलाइन: 104
- महिला हेल्पलाइन: 181
- बाल हेल्पलाइन: 1098

स्वस्थ जीवन के लिए:
- संतुलित आहार, भरपूर पानी
- नियमित व्यायाम (30 मिनट/दिन)
- पर्याप्त नींद (7-8 घंटे)
- तनाव प्रबंधन, ध्यान/योग
- नियमित स्वास्थ्य जांच"""
        elif language == 'te':
            return """సాధారణ ఆరోగ్య మార్గదర్శకత్వం:

ప్రాథమిక చికిత్స కిట్‌లో ఉంచండి:
- బ్యాండేజ్, పత్తి, గాజ్
- క్రిమినాశక క్రీమ్ (బెటాడిన్)
- పారాసిటమాల్, యాంటాసిడ్
- ORS పొడి
- థర్మామీటర్
- శుభ్రమైన నీరు

సాధారణ లక్షణాలు మరియు చికిత్స:
1. తలనొప్పి: విశ్రాంతి, నీరు త్రాగండి, పారాసిటమాల్
2. తల తిరగడం: పడుకోండి, కాళ్లు పైకి
3. చిన్న గాయం: శుభ్రం చేయండి, క్రిమినాశక రాయండి
4. చిన్న కాలుడు: చల్లని నీటిలో 10 నిమిషాలు
5. ముక్కు నుండి రక్తం: ముందుకు వాలండి, ముక్కు నొక్కండి

వైద్యుడిని ఎప్పుడు చూడాలి:
- తీవ్రమైన నొప్పి లేదా అసహ్యకరమైన లక్షణాలు
- శ్వాస తీసుకోవడంలో ఇబ్బంది
- స్పృహ కోల్పోవడం లేదా గందరగోళం
- తీవ్రమైన గాయం లేదా రక్తస్రావం
- పిల్లలు/వృద్ధులలో ఏదైనా తీవ్ర లక్షణం

అత్యవసర నంబర్లు:
- అంబులెన్స్: 102, 108
- ఆరోగ్య హెల్ప్‌లైన్: 104
- మహిళా హెల్ప్‌లైన్: 181
- పిల్లల హెల్ప్‌లైన్: 1098

ఆరోగ్యకరమైన జీవితం కోసం:
- సమతుల్య ఆహారం, పుష్కలంగా నీరు
- క్రమం తప్పకుండా వ్యాయామం (30 నిమిషాలు/రోజు)
- తగినంత నిద్ర (7-8 గంటలు)
- ఒత్తిడి నిర్వహణ, ధ్యానం/యోగా
- క్రమం తప్పకుండా ఆరోగ్య పరీక్షలు"""
        else:
            return """GENERAL HEALTH GUIDANCE:

First Aid Kit Essentials:
- Bandages, cotton, gauze
- Antiseptic cream (Betadine)
- Paracetamol, antacids
- ORS powder
- Thermometer
- Clean water

Common Symptoms & Treatment:
1. Headache: Rest, drink water, paracetamol
2. Dizziness: Lie down, elevate legs
3. Minor cuts: Clean, apply antiseptic
4. Minor burns: Cold water for 10 minutes
5. Nosebleed: Lean forward, pinch nose

When to See Doctor:
- Severe pain or unbearable symptoms
- Breathing difficulty
- Loss of consciousness or confusion
- Serious injury or bleeding
- Any serious symptoms in children/elderly

Emergency Numbers:
- Ambulance: 102, 108
- Health Helpline: 104
- Women Helpline: 181
- Child Helpline: 1098

For Healthy Life:
- Balanced diet, plenty of water
- Regular exercise (30 min/day)
- Adequate sleep (7-8 hours)
- Stress management, meditation/yoga
- Regular health checkups"""
    
    def _get_scheme_guidance(self, query, language):
        """Provide comprehensive welfare scheme guidance"""
        if language == 'hi':
            return """सरकारी योजनाएं - संपूर्ण जानकारी:

╔══════════════════════════════════════╗
║   प्रमुख केंद्रीय सरकारी योजनाएं    ║
╚══════════════════════════════════════╝

1. प्रधानमंत्री आवास योजना (PMAY):
   उद्देश्य: सभी को आवास
   लाभ: ₹2.67 लाख तक सब्सिडी
   पात्रता: EWS/LIG परिवार, कोई पक्का मकान नहीं
   दस्तावेज: आधार, आय प्रमाण, बैंक खाता
   आवेदन: pmaymis.gov.in

2. आयुष्मान भारत (PM-JAY):
   उद्देश्य: निःशुल्क स्वास्थ्य बीमा
   लाभ: ₹5 लाख तक का इलाज मुफ्त
   पात्रता: गरीब और वंचित परिवार
   आवेदन: pmjay.gov.in, CSC केंद्र
   हेल्पलाइन: 14555

3. प्रधानमंत्री उज्ज्वला योजना:
   लाभ: मुफ्त LPG कनेक्शन
   पात्रता: BPL परिवार की महिलाएं
   दस्तावेज: राशन कार्ड, आधार, फोटो
   लाभ: पहला सिलिंडर सब्सिडी के साथ

4. प्रधानमंत्री किसान सम्मान निधि (PM-KISAN):
   लाभ: ₹6,000/वर्ष (तीन किस्तें)
   पात्रता: सभी किसान परिवार
   आवेदन: pmkisan.gov.in
   बैंक खाता आवश्यक (DBT के लिए)

5. वृद्धावस्था पेंशन योजना:
   लाभ: ₹200-1,000/माह (राज्य के अनुसार)
   पात्रता: 60+ वर्ष, BPL परिवार
   आवेदन: जिला समाज कल्याण कार्यालय

6. मुद्रा लोन योजना:
   लाभ: ₹10 लाख तक ऋण (बिना गारंटी)
   शिशु: ₹50,000 तक
   किशोर: ₹50,000 - 5 लाख
   तरुण: ₹5-10 लाख
   आवेदन: बैंक/NBFC

7. छात्रवृत्ति योजनाएं:
   - Pre-Matric: कक्षा 9-10
   - Post-Matric: कक्षा 11 से ऊपर
   - मेरिट आधारित छात्रवृत्ति
   आवेदन: scholarships.gov.in

╔═══════════════════════════════════╗
║   आवेदन कैसे करें - चरण-दर-चरण  ║
╚═══════════════════════════════════╝

ऑनलाइन आवेदन:
1. योजना की आधिकारिक वेबसाइट पर जाएं
2. "Apply Online" या "New Registration" पर क्लिक करें
3. व्यक्तिगत विवरण भरें
4. आवश्यक दस्तावेज अपलोड करें
5. आवेदन जमा करें और रसीद डाउनलोड करें

ऑफलाइन आवेदन:
1. नजदीकी जन सेवा केंद्र (CSC) पर जाएं
2. आवश्यक दस्तावेज ले जाएं
3. सहायक से फॉर्म भरवाएं
4. फॉर्म जमा करें और रसीद लें

आवश्यक दस्तावेज (सामान्य):
✓ आधार कार्ड (अनिवार्य)
✓ बैंक खाता पासबुक
✓ आय प्रमाण पत्र
✓ जाति प्रमाण पत्र (यदि लागू हो)
✓ निवास प्रमाण पत्र
✓ पासपोर्ट साइज फोटो
✓ मोबाइल नंबर

╔════════════════════════════════╗
║   महत्वपूर्ण हेल्पलाइन नंबर    ║
╚════════════════════════════════╝

- PM-JAY: 14555
- PM-KISAN: 155261, 011-24300606
- PMAY: 1800-11-6163
- उज्ज्वला: 1906
- सामान्य शिकायत: pgportal.gov.in

╔═══════════════════════════════╗
║   उपयोगी वेबसाइट            ║
╚═══════════════════════════════╝

- सभी योजनाएं: india.gov.in
- छात्रवृत्ति: scholarships.gov.in
- शिकायत: pgportal.gov.in
- डिजिटल इंडिया: digitalindia.gov.in

नोट: नकली वेबसाइट से सावधान रहें!
केवल .gov.in या .nic.in वेबसाइट पर विश्वास करें।"""
        
        elif language == 'te':
            return """ప్రభుత్వ పథకాలు - సంపూర్ణ సమాచారం:

╔══════════════════════════════════════╗
║   ప్రధాన కేంద్ర ప్రభుత్వ పథకాలు      ║
╚══════════════════════════════════════╝

1. ప్రధాన మంత్రి గృహ పథకం (PMAY):
   లక్ష్యం: అందరికీ గృహం
   లాభం: ₹2.67 లక్షల వరకు సబ్సిడీ
   అర్హత: EWS/LIG కుటుంబాలు, పక్కా ఇల్లు లేదు
   పత్రాలు: ఆధార్, ఆదాయ ధ్రువపత్రం, బ్యాంక్ ఖాతా
   దరఖాస్తు: pmaymis.gov.in

2. ఆయుష్మాన్ భారత్ (PM-JAY):
   లక్ష్యం: ఉచిత ఆరోగ్య బీమా
   లాభం: ₹5 లక్షల వరకు చికిత్స ఉచితం
   అర్హత: పేద మరియు వెనుకబడిన కుటుంబాలు
   దరఖాస్తు: pmjay.gov.in, CSC కేంద్రం
   హెల్ప్‌లైన్: 14555

3. ప్రధాన మంత్రి ఉజ్జ్వల పథకం:
   లాభం: ఉచిత LPG కనెక్షన్
   అర్హత: BPL కుటుంబ మహిళలు
   పత్రాలు: రేషన్ కార్డ్, ఆధార్, ఫోటో
   లాభం: మొదటి సిలిండర్ సబ్సిడీతో

4. PM-KISAN (రైతు సన్మాన్ నిధి):
   లాభం: ₹6,000/సంవత్సరం (మూడు విడతలు)
   అర్హత: అన్ని రైతు కుటుంబాలు
   దరఖాస్తు: pmkisan.gov.in
   బ్యాంక్ ఖాతా అవసరం (DBT కోసం)

5. వృద్ధాప్య పెన్షన్ పథకం:
   లాభం: ₹200-1,000/నెల (రాష్ట్ర ప్రకారం)
   అర్హత: 60+ సంవత్సరాలు, BPL కుటుంబం
   దరఖాస్తు: జిల్లా సమాజ సంక్షేమ కార్యాలయం

6. ముద్ర రుణ పథకం:
   లాభం: ₹10 లక్షల వరకు రుణం (హామీ లేకుండా)
   శిశు: ₹50,000 వరకు
   కిశోర్: ₹50,000 - 5 లక్షలు
   తరుణ్: ₹5-10 లక్షలు
   దరఖాస్తు: బ్యాంక్/NBFC

7. స్కాలర్‌షిప్ పథకాలు:
   - Pre-Matric: 9-10 తరగతులు
   - Post-Matric: 11 తరగతి పైన
   - మెరిట్ ఆధారిత స్కాలర్‌షిప్‌లు
   దరఖాస్తు: scholarships.gov.in

╔═══════════════════════════════════╗
║   ఎలా దరఖాస్తు చేసుకోవాలి?      ║
╚═══════════════════════════════════╝

ఆన్‌లైన్ దరఖాస్తు:
1. పథకం అధికారిక వెబ్‌సైట్‌కు వెళ్లండి
2. "Apply Online" లేదా "New Registration" క్లిక్ చేయండి
3. వ్యక్తిగత వివరాలు పూరించండి
4. అవసరమైన పత్రాలు అప్‌లోడ్ చేయండి
5. దరఖాస్తు సమర్పించి రసీదు డౌన్‌లోడ్ చేయండి

ఆఫ్‌లైన్ దరఖాస్తు:
1. సమీప జన సేవా కేంద్రం (CSC)కి వెళ్లండి
2. అవసరమైన పత్రాలు తీసుకెళ్లండి
3. సహాయకునితో ఫారమ్ పూరించండి
4. ఫారమ్ సమర్పించి రసీదు తీసుకోండి

అవసరమైన పత్రాలు (సాధారణ):
✓ ఆధార్ కార్డ్ (తప్పనిసరి)
✓ బ్యాంక్ ఖాతా పాస్‌బుక్
✓ ఆదాయ ధ్రువపత్రం
✓ కుల ధ్రువపత్రం (వర్తించినట్లయితే)
✓ నివాస ధ్రువపత్రం
✓ పాస్‌పోర్ట్ సైజ్ ఫోటో
✓ మొబైల్ నంబర్

╔════════════════════════════════╗
║   ముఖ్యమైన హెల్ప్‌లైన్ నంబర్లు  ║
╚════════════════════════════════╝

- PM-JAY: 14555
- PM-KISAN: 155261, 011-24300606
- PMAY: 1800-11-6163
- ఉజ్జ్వల: 1906
- సాధారణ ఫిర్యాదు: pgportal.gov.in

╔═══════════════════════════════╗
║   ఉపయోగకరమైన వెబ్‌సైట్‌లు     ║
╚═══════════════════════════════╝

- అన్ని పథకాలు: india.gov.in
- స్కాలర్‌షిప్‌లు: scholarships.gov.in
- ఫిర్యాదు: pgportal.gov.in
- డిజిటల్ ఇండియా: digitalindia.gov.in

గమనిక: నకిలీ వెబ్‌సైట్‌ల నుండి జాగ్రత్త!
.gov.in లేదా .nic.in వెబ్‌సైట్‌లను మాత్రమే నమ్మండి।"""
        
        else:  # English
            return """GOVERNMENT SCHEMES - Complete Information:

╔══════════════════════════════════════╗
║   MAJOR CENTRAL GOVERNMENT SCHEMES   ║
╚══════════════════════════════════════╝

1. Pradhan Mantri Awas Yojana (PMAY):
   Objective: Housing for All
   Benefit: Up to ₹2.67 lakh subsidy
   Eligibility: EWS/LIG families, no pucca house
   Documents: Aadhaar, income proof, bank account
   Apply: pmaymis.gov.in

2. Ayushman Bharat (PM-JAY):
   Objective: Free health insurance
   Benefit: Up to ₹5 lakh free treatment
   Eligibility: Poor and deprived families
   Apply: pmjay.gov.in, CSC centers
   Helpline: 14555

3. Pradhan Mantri Ujjwala Yojana:
   Benefit: Free LPG connection
   Eligibility: BPL family women
   Documents: Ration card, Aadhaar, photo
   Benefit: First cylinder with subsidy

4. PM-KISAN (Kisan Samman Nidhi):
   Benefit: ₹6,000/year (three installments)
   Eligibility: All farmer families
   Apply: pmkisan.gov.in
   Bank account required (for DBT)

5. Old Age Pension Scheme:
   Benefit: ₹200-1,000/month (state-wise)
   Eligibility: 60+ years, BPL family
   Apply: District Social Welfare Office

6. Mudra Loan Scheme:
   Benefit: Up to ₹10 lakh loan (no collateral)
   Shishu: Up to ₹50,000
   Kishor: ₹50,000 - 5 lakh
   Tarun: ₹5-10 lakh
   Apply: Banks/NBFCs

7. Scholarship Schemes:
   - Pre-Matric: Class 9-10
   - Post-Matric: Class 11 onwards
   - Merit-based scholarships
   Apply: scholarships.gov.in

╔═══════════════════════════════════╗
║   HOW TO APPLY - STEP BY STEP     ║
╚═══════════════════════════════════╝

Online Application:
1. Visit scheme's official website
2. Click "Apply Online" or "New Registration"
3. Fill personal details
4. Upload required documents
5. Submit application and download receipt

Offline Application:
1. Visit nearest Jan Seva Kendra (CSC)
2. Take required documents
3. Get form filled by assistant
4. Submit form and take receipt

Required Documents (General):
✓ Aadhaar Card (mandatory)
✓ Bank account passbook
✓ Income certificate
✓ Caste certificate (if applicable)
✓ Residence proof
✓ Passport size photo
✓ Mobile number

╔════════════════════════════════╗
║   IMPORTANT HELPLINE NUMBERS    ║
╚════════════════════════════════╝

- PM-JAY: 14555
- PM-KISAN: 155261, 011-24300606
- PMAY: 1800-11-6163
- Ujjwala: 1906
- General Grievance: pgportal.gov.in

╔═══════════════════════════════╗
║   USEFUL WEBSITES             ║
╚═══════════════════════════════╝

- All Schemes: india.gov.in
- Scholarships: scholarships.gov.in
- Complaints: pgportal.gov.in
- Digital India: digitalindia.gov.in

Note: Beware of fake websites!
Trust only .gov.in or .nic.in websites."""
    
    def _get_climate_guidance(self, query, language):
        """Provide comprehensive climate and disaster safety guidance"""
        query_lower = query.lower()
        
        # Heatwave guidance
        if any(word in query_lower for word in ['heatwave', 'hot', 'heat', 'गर्मी', 'వేడి']):
            if language == 'en':
                return """HEATWAVE SAFETY - Complete Protection Guide:

Understanding Heat Emergencies:
- Heat Cramps: Muscle pain, heavy sweating
- Heat Exhaustion: Weakness, nausea, headache
- Heat Stroke: EMERGENCY - confusion, no sweating, fever 104°F+

Immediate Protection:
1. Stay indoors 11 AM - 4 PM
2. Drink water every 30 minutes (8-10 glasses/day)
3. Wear light, loose, cotton clothes (white/light colors)
4. Use hat, umbrella, sunglasses when outside
5. Avoid alcohol, caffeine, heavy meals

For Heat Cramps:
- Stop activity immediately
- Drink ORS or lemon water with salt
- Massage cramped muscles gently
- Rest in cool place

For Heat Exhaustion:
- Move to cool, shaded area
- Remove excess clothing
- Pour cool water, use wet cloth
- Drink ORS slowly
- Seek medical help if not improving

For Heat Stroke (EMERGENCY):
- Call 102/108 immediately
- Move to cool place
- Remove clothes
- Pour cool water all over body
- Fan the person
- Give water if conscious
- DO NOT give medicine

Who is at High Risk:
- Infants and children under 5
- Elderly (65+ years)
- Outdoor workers
- Pregnant women
- Chronic disease patients

Prevention Tips:
- Drink water before feeling thirsty
- Eat hydrating fruits (watermelon, cucumber)
- Take cool showers multiple times
- Keep curtains closed during day
- Use coolers/fans properly
- Never leave children/pets in vehicles

Emergency Numbers:
- Ambulance: 102, 108
- State Disaster Helpline: 1070
- Health Emergency: 104

Warning Signs to Watch:
- Severe headache
- Dizziness or fainting
- Rapid heartbeat
- Dry skin (not sweating)
- Confusion or irritability"""
            else:
                return self._get_climate_guidance('flood', language)  # Fallback
        
        # Flood guidance
        if any(word in query_lower for word in ['flood', 'rain', 'water', 'बाढ़', 'वर्षा', 'వరద']):
            if language == 'en':
                return """FLOOD SAFETY - Emergency Survival Guide:

BEFORE FLOOD:
Preparation:
1. Keep emergency kit ready (torch, battery, first-aid)
2. Store drinking water (at least 3 days supply)
3. Keep important documents in waterproof bag
4. Know evacuation routes and shelter locations
5. Keep mobile charged, power bank ready
6. Stock dry food items (biscuits, dry fruits)

During Heavy Rain:
7. Monitor weather alerts (TV/Radio/Mobile)
8. Avoid going to low-lying areas
9. Stay away from drainage areas
10. Don't drive through waterlogged roads

DURING FLOOD:
If At Home:
1. Move to highest floor/terrace immediately
2. Turn off electricity and gas
3. Don't touch electrical equipment with wet hands
4. Keep mobile phone charged
5. Signal for help (bright clothes, torch)
6. Don't go near windows

If Outside:
7. Move to higher ground immediately
8. Never walk through moving water (6 inches can knock you down)
9. Avoid flooded roads and bridges
10. Stay away from electric poles and wires
11. Don't try to swim - stay afloat

Car Safety:
- Abandon car if water rising
- Don't drive through flooded areas
- Even 1 foot water can float car
- Electric cars: exit immediately

AFTER FLOOD:
Recovery:
1. Return home only when authorities say safe
2. Check for structural damage before entering
3. Take photos for insurance claims
4. Throw away contaminated food/water
5. Clean and disinfect everything
6. Watch for snakes/insects

Health Precautions:
- Boil water before drinking
- Wash hands frequently
- Watch for skin infections
- Get tetanus shot if injured
- Seek medical help for diarrhea/fever

What NOT to Do:
✗ Don't drink flood water
✗ Don't touch electrical wires
✗ Don't go sightseeing in flooded areas
✗ Don't ignore evacuation orders
✗ Don't spread rumors

Emergency Numbers:
- Disaster Management: 1070
- Police: 100
- Ambulance: 102, 108
- Fire: 101
- NDRF: 011-24363260

Relief & Assistance:
- Move to designated relief camps
- Register with authorities
- Get ration and medical help
- Apply for compensation online"""
            else:
                return self._get_climate_guidance('heatwave', language)
        
        # General climate warning
        if language == 'en':
            return """WEATHER EMERGENCY SAFETY - Complete Guide:

╔══════════════════════════════════╗
║   COMMON WEATHER EMERGENCIES     ║
╚══════════════════════════════════╝

1. CYCLONE/STORM:
   Before: Secure loose items, stock supplies
   During: Stay indoors, away from windows
   After: Check for damage, avoid damaged buildings

2. LIGHTNING:
   - Seek shelter in building/car
   - Avoid trees, metal objects, water
   - If in open: crouch low, feet together
   - If indoors: avoid phones, plumbing

3. EARTHQUAKE:
   During: DROP, COVER, HOLD ON
   - Get under strong table/desk
   - Stay away from windows, shelves
   - If outside: move to open area
   After: Check for injuries, gas leaks

4. DROUGHT:
   - Conserve water strictly
   - Fix leaks immediately
   - Reuse water when possible
   - Grow drought-resistant crops

5. AIR POLLUTION:
   - Stay indoors when AQI high
   - Use air purifiers/masks
   - Avoid morning walks during smog
   - Keep indoor plants

╔════════════════════════════════╗
║   EMERGENCY PREPAREDNESS KIT   ║
╚════════════════════════════════╝

Must Have Items:
✓ Drinking water (3-day supply)
✓ Non-perishable food
✓ First aid kit & medicines
✓ Flashlight & batteries
✓ Radio (battery/hand-crank)
✓ Mobile & power bank
✓ Whistle for signaling
✓ Local maps
✓ Cash in small denominations
✓ Important documents (copies)
✓ Warm clothes/blankets
✓ Toiletries & sanitizer

╔════════════════════════════════╗
║   EMERGENCY CONTACT NUMBERS    ║
╚════════════════════════════════╝

National Emergency Numbers:
- Police: 100
- Fire: 101
- Ambulance: 102, 108
- Disaster Management: 1070
- Women Helpline: 181
- Child Helpline: 1098
- Senior Citizen: 14567
- NDRF: 011-24363260

State Disaster Helplines:
Check your state government website
for specific helpline numbers.

╔════════════════════════════════╗
║   WEATHER ALERTS & TRACKING    ║
╚════════════════════════════════╝

Official Sources:
- IMD: mausam.imd.gov.in
- NDMA: ndma.gov.in
- State Disaster Management websites
- Mobile Apps: Mausam, UMANG

Alert Levels:
🟢 Green: No warning
🟡 Yellow: Be aware
🟠 Orange: Be prepared
🔴 Red: Take action

╔════════════════════════════════╗
║   FAMILY EMERGENCY PLAN        ║
╚════════════════════════════════╝

Prepare Now:
1. Identify safe spots in home
2. Know evacuation routes
3. Decide meeting points
4. Keep emergency contacts handy
5. Practice emergency drills
6. Teach children what to do

Communication Plan:
- Designate out-of-state contact
- Keep written emergency contacts
- Know where children's schools are
- Have backup communication method

Remember: Stay Calm, Stay Safe, Stay Informed!"""
        else:
            return self._get_climate_guidance('flood', language)
    
    def _get_general_guidance(self, language):
        """Provide general help guidance"""
        if language == 'hi':
            return """नमस्ते! मैं साथी AI हूं - आपका स्वास्थ्य और कल्याण सहायक।

मैं आपकी कैसे मदद कर सकता हूं:

🏥 स्वास्थ्य सलाह:
   - बुखार, सर्दी, खांसी का इलाज
   - पेट दर्द, दस्त, उल्टी की देखभाल
   - चोट और जलने का प्राथमिक उपचार
   - सामान्य स्वास्थ्य मार्गदर्शन
   - आपातकालीन नंबर और सहायता

📋 सरकारी योजनाएं:
   - आवास योजना (PM Awas)
   - स्वास्थ्य बीमा (Ayushman Bharat)
   - गैस कनेक्शन (Ujjwala)
   - पेंशन योजनाएं
   - किसान योजनाएं
   - छात्रवृत्ति कार्यक्रम
   - आवेदन प्रक्रिया और दस्तावेज

🌤️ जलवायु सुरक्षा:
   - गर्मी/लू से बचाव
   - बाढ़ सुरक्षा उपाय
   - तूफान और आंधी की चेतावनी
   - आपदा प्रबंधन
   - मौसम अपडेट

बस अपना सवाल बोलें, मैं आपकी मदद करूंगा!

आपातकालीन नंबर:
- एम्बुलेंस: 102, 108
- पुलिस: 100
- आग: 101
- आपदा: 1070"""
        elif language == 'te':
            return """నమస్కారం! నేను సార్థి AI - మీ ఆరోగ్యం మరియు సంక్షేమ సహాయకుడు।

నేను మీకు ఎలా సహాయం చేయగలను:

🏥 ఆరోగ్య సలహా:
   - జ్వరం, జలుబు, దగ్గు చికిత్స
   - కడుపు నొప్పి, విరేచనాలు, వాంతుల సంరక్షణ
   - గాయం మరియు కాలిన గాయాలకు ప్రాథమిక చికిత్స
   - సాధారణ ఆరోగ్య మార్గదర్శకత్వం
   - అత్యవసర నంబర్లు మరియు సహాయం

📋 ప్రభుత్వ పథకాలు:
   - గృహ పథకం (PM Awas)
   - ఆరోగ్య బీమా (Ayushman Bharat)
   - గ్యాస్ కనెక్షన్ (Ujjwala)
   - పెన్షన్ పథకాలు
   - రైతు పథకాలు
   - స్కాలర్‌షిప్ కార్యక్రమాలు
   - దరఖాస్తు ప్రక్రియ మరియు పత్రాలు

🌤️ వాతావరణ భద్రత:
   - వేడి/హీట్‌వేవ్ నుండి రక్షణ
   - వరద భద్రత చర్యలు
   - తుఫాను మరియు తుఫాను హెచ్చరిక
   - విపత్తు నిర్వహణ
   - వాతావరణ నవీకరణలు

మీ ప్రశ్న చెప్పండి, నేను మీకు సహాయం చేస్తాను!

అత్యవసర నంబర్లు:
- అంబులెన్స్: 102, 108
- పోలీసు: 100
- అగ్నిమాపక: 101
- విపత్తు: 1070"""
        else:
            return """Hello! I am Saarthi AI - Your Health & Welfare Assistant.

How can I help you:

🏥 Health Advice:
   - Fever, cold, cough treatment
   - Stomach pain, diarrhea, vomiting care
   - Injury and burn first aid
   - General health guidance
   - Emergency numbers and assistance

📋 Government Schemes:
   - Housing scheme (PM Awas)
   - Health insurance (Ayushman Bharat)
   - Gas connection (Ujjwala)
   - Pension schemes
   - Farmer schemes
   - Scholarship programs
   - Application process and documents

🌤️ Climate Safety:
   - Heat/heatwave protection
   - Flood safety measures
   - Storm and cyclone warnings
   - Disaster management
   - Weather updates

Just ask your question, I'll help you!

Emergency Numbers:
- Ambulance: 102, 108
- Police: 100
- Fire: 101
- Disaster: 1070"""
