"""
Rule-based intent detection and guidance system for SaarthiAI
Detects user intent and provides appropriate guidance
"""

class IntentEngine:
    """
    Simple rule-based intent detection engine
    Analyzes user queries and returns appropriate guidance
    """
    
    def __init__(self):
        # Define knowledge base for different categories
        self.health_keywords = [
            'fever', 'temperature', 'sick', 'pain', 'headache', 'cold', 
            'cough', 'vomit', 'diarrhea', 'injury', 'wound', 'burn',
            'बुखार', 'दर्द', 'सिरदर्द', 'खांसी', 'ठंड',  # Hindi
            'జ్వరం', 'నొప్పి', 'తలనొప్పి', 'దగ్గు'  # Telugu
        ]
        
        self.scheme_keywords = [
            'scheme', 'yojana', 'application', 'benefit', 'subsidy', 
            'pension', 'ration', 'card', 'apply', 'form', 'government',
            'योजना', 'आवेदन', 'लाभ', 'पेंशन', 'राशन',  # Hindi
            'పథకం', 'దరఖాస్తు', 'ప్రయోజనం', 'పెన్షన్'  # Telugu
        ]
        
        self.climate_keywords = [
            'heatwave', 'flood', 'warning', 'rain', 'storm', 'cyclone',
            'drought', 'hot', 'weather', 'disaster', 'alert', 'emergency',
            'गर्मी', 'बाढ़', 'चेतावनी', 'बारिश', 'तूफान',  # Hindi
            'వేడి', 'వరద', 'హెచ్చరిక', 'వర్షం', 'తుఫాను'  # Telugu
        ]
    
    def detect_intent(self, text):
        """
        Detect user intent from the text
        Returns: 'health', 'schemes', 'climate', or 'general'
        """
        text_lower = text.lower()
        
        # Check for health-related queries
        if any(keyword in text_lower for keyword in self.health_keywords):
            return 'health'
        
        # Check for scheme-related queries
        if any(keyword in text_lower for keyword in self.scheme_keywords):
            return 'schemes'
        
        # Check for climate-related queries
        if any(keyword in text_lower for keyword in self.climate_keywords):
            return 'climate'
        
        return 'general'
    
    def get_guidance(self, text, language='en'):
        """
        Generate appropriate guidance based on intent and language
        Returns: dict with intent and guidance text
        """
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
        """Provide health and first-aid guidance"""
        query_lower = query.lower()
        
        # Fever-specific guidance
        if any(word in query_lower for word in ['fever', 'बुखार', 'జ్వరం', 'temperature']):
            if language == 'hi':
                return """बुखार के लिए प्राथमिक उपचार:
1. रोगी को आराम करने दें
2. ठंडे पानी से स्पंज करें
3. हल्के कपड़े पहनाएं
4. तरल पदार्थ पिलाएं
5. पेरासिटामोल दें (डॉक्टर की सलाह पर)
6. अगर 102°F से ऊपर हो तो तुरंत डॉक्टर को दिखाएं
7. छोटे बच्चों के लिए तुरंत चिकित्सा सहायता लें"""
            elif language == 'te':
                return """జ్వరం కోసం ప్రాథమిక చికిత్స:
1. రోగిని విశ్రాంతి తీసుకోవాలి
2. చల్లని నీటితో స్పాంజ్ చేయండి
3. తేలికపాటి దుస్తులు ధరించండి
4. ద్రవపదార్థాలు తాగించండి
5. పారాసిటమాల్ ఇవ్వండి (వైద్యుల సలహా తీసుకోండి)
6. 102°F కంటే ఎక్కువ ఉంటే వెంటనే వైద్యుడిని సంప్రదించండి
7. చిన్న పిల్లలకు వెంటనే వైద్య సహాయం పొందండి"""
            else:
                return """First Aid for Fever:
1. Make the patient rest
2. Sponge with cool water
3. Wear light clothes
4. Give plenty of fluids
5. Give paracetamol (consult doctor)
6. See doctor immediately if temperature above 102°F
7. For small children, seek medical help immediately"""
        
        # General health advice
        if language == 'hi':
            return """सामान्य स्वास्थ्य सलाह:
1. लक्षणों की जांच करें
2. रोगी को आराम दें
3. हाइड्रेटेड रखें
4. गंभीर लक्षणों के लिए तुरंत डॉक्टर से संपर्क करें
5. साफ-सफाई बनाए रखें"""
        elif language == 'te':
            return """సాధారణ ఆరోగ్య సలహా:
1. లక్షణాలను తనిఖీ చేయండి
2. రోగిని విశ్రాంతి తీసుకోనివ్వండి
3. హైడ్రేటెడ్ గా ఉంచండి
4. తీవ్రమైన లక్షణాలకు వెంటనే వైద్యుడిని సంప్రదించండి
5. పరిశుభ్రతను కొనసాగించండి"""
        else:
            return """General Health Advice:
1. Monitor symptoms carefully
2. Let patient rest
3. Keep hydrated
4. Consult doctor for serious symptoms
5. Maintain hygiene"""
    
    def _get_scheme_guidance(self, query, language):
        """Provide welfare scheme guidance"""
        if language == 'hi':
            return """सरकारी योजनाएं और आवेदन प्रक्रिया:

प्रमुख योजनाएं:
1. प्रधानमंत्री आवास योजना - घर के लिए
2. आयुष्मान भारत - स्वास्थ्य बीमा
3. उज्ज्वला योजना - मुफ्त गैस कनेक्शन
4. वृद्धावस्था पेंशन योजना
5. राशन कार्ड सेवाएं

आवेदन कैसे करें:
1. नजदीकी जन सेवा केंद्र पर जाएं
2. आवश्यक दस्तावेज ले जाएं (आधार, पहचान पत्र)
3. आवेदन फॉर्म भरें
4. सरकारी वेबसाइट पर भी आवेदन कर सकते हैं
5. हेल्पलाइन: 1800-XXX-XXXX"""
        elif language == 'te':
            return """ప్రభుత్వ పథకాలు మరియు దరఖాస్తు ప్రక్రియ:

ప్రధాన పథకాలు:
1. ప్రధాన మంత్రి గృహ పథకం - ఇంటి కోసం
2. ఆయుష్మాన్ భారత్ - ఆరోగ్య భీమా
3. ఉజ్జ్వల పథకం - ఉచిత గ్యాస్ కనెక్షన్
4. వృద్ధాప్య పెన్షన్ పథకం
5. రేషన్ కార్డ్ సేవలు

ఎలా దరఖాస్తు చేసుకోవాలి:
1. సమీప జనసేవా కేంద్రానికి వెళ్లండి
2. అవసరమైన పత్రాలు తీసుకురండి (ఆధార్, గుర్తింపు)
3. దరఖాస్తు ఫారమ్ పూరించండి
4. ప్రభుత్వ వెబ్‌సైట్‌లో కూడా దరఖాస్తు చేసుకోవచ్చు
5. హెల్ప్‌లైన్: 1800-XXX-XXXX"""
        else:
            return """Government Schemes and Application Process:

Key Schemes:
1. PM Awas Yojana - Housing
2. Ayushman Bharat - Health Insurance
3. Ujjwala Yojana - Free Gas Connection
4. Old Age Pension Scheme
5. Ration Card Services

How to Apply:
1. Visit nearest Jan Seva Kendra
2. Bring required documents (Aadhaar, ID proof)
3. Fill application form
4. Can also apply on government website
5. Helpline: 1800-XXX-XXXX"""
    
    def _get_climate_guidance(self, query, language):
        """Provide climate and disaster safety guidance"""
        query_lower = query.lower()
        
        # Heatwave guidance
        if any(word in query_lower for word in ['heatwave', 'hot', 'गर्मी', 'వేడి']):
            if language == 'hi':
                return """गर्मी/लू से बचाव:
1. दोपहर 12-3 बजे बाहर न निकलें
2. ढीले, हल्के रंग के कपड़े पहनें
3. खूब पानी पिएं
4. ओआरएस घोल लें
5. टोपी या छाता उपयोग करें
6. लू लगने पर तुरंत ठंडी जगह पर ले जाएं
7. शरीर पर ठंडा पानी डालें
8. आपातकाल में 108 डायल करें"""
            elif language == 'te':
                return """వేడి/హీట్‌వేవ్ నుండి రక్షణ:
1. మధ్యాహ్నం 12-3 గంటల మధ్య బయటకు వెళ్లవద్దు
2. వదులుగా, లేత రంగు దుస్తులు ధరించండి
3. చాలా నీరు త్రాగండి
4. ORS ద్రావణం తాగండి
5. టోపీ లేదా గొడుగు ఉపయోగించండి
6. హీట్ స్ట్రోక్ వచ్చినప్పుడు వెంటనే చల్లని ప్రదేశానికి తీసుకెళ్లండి
7. శరీరంపై చల్లని నీరు పోయండి
8. అత్యవసర పరిస్థితులలో 108 డయల్ చేయండి"""
            else:
                return """Heatwave Safety:
1. Avoid going out 12-3 PM
2. Wear loose, light-colored clothes
3. Drink plenty of water
4. Take ORS solution
5. Use hat or umbrella
6. If heat stroke, move to cool place immediately
7. Pour cool water on body
8. Dial 108 for emergency"""
        
        # Flood guidance
        if any(word in query_lower for word in ['flood', 'rain', 'बाढ़', 'वर्षा', 'వరద']):
            if language == 'hi':
                return """बाढ़ से सुरक्षा:
1. ऊंची जगह पर जाएं
2. बिजली के उपकरणों को छुएं नहीं
3. बाढ़ के पानी में न चलें
4. आपातकालीन किट तैयार रखें
5. स्थानीय अधिकारियों के निर्देशों का पालन करें
6. महत्वपूर्ण दस्तावेज सुरक्षित रखें
7. राहत शिविर का पता लगाएं"""
            elif language == 'te':
                return """వరద నుండి భద్రత:
1. ఎత్తైన ప్రదేశానికి వెళ్లండి
2. విద్యుత్ పరికరాలను ముట్టుకోవద్దు
3. వరద నీటిలో నడవకండి
4. అత్యవసర కిట్ సిద్ధంగా ఉంచండి
5. స్థానిక అధికారుల సూచనలను పాటించండి
6. ముఖ్యమైన పత్రాలను సురక్షితంగా ఉంచండి
7. సహాయ శిబిరాన్ని గుర్తించండి"""
            else:
                return """Flood Safety:
1. Move to higher ground
2. Don't touch electrical equipment
3. Don't walk in flood water
4. Keep emergency kit ready
5. Follow local authorities' instructions
6. Keep important documents safe
7. Locate relief camp"""
        
        # General climate warning
        if language == 'hi':
            return """मौसम आपातकाल सुरक्षा:
1. मौसम पूर्वानुमान सुनें
2. आपातकालीन संपर्क नंबर सहेजें
3. आपातकालीन किट तैयार रखें
4. परिवार के सदस्यों के साथ योजना बनाएं
5. स्थानीय अधिकारियों के निर्देशों का पालन करें"""
        elif language == 'te':
            return """వాతావరణ అత్యవసర భద్రత:
1. వాతావరణ సూచనలు వినండి
2. అత్యవసర సంప్రదింపు నంబర్లు సేవ్ చేయండి
3. అత్యవసర కిట్ సిద్ధంగా ఉంచండి
4. కుటుంబ సభ్యులతో ప్రణాళిక చేసుకోండి
5. స్థానిక అధికారుల సూచనలను పాటించండి"""
        else:
            return """Weather Emergency Safety:
1. Listen to weather forecasts
2. Save emergency contact numbers
3. Keep emergency kit ready
4. Plan with family members
5. Follow local authorities' instructions"""
    
    def _get_general_guidance(self, language):
        """Provide general help guidance"""
        if language == 'hi':
            return """नमस्ते! मैं साथी AI हूं। मैं आपकी मदद कर सकता हूं:

1. स्वास्थ्य सलाह - बुखार, चोट, प्राथमिक उपचार
2. सरकारी योजनाएं - आवेदन प्रक्रिया, लाभ
3. मौसम सुरक्षा - गर्मी, बाढ़, आपदा सुरक्षा

कृपया अपना सवाल पूछें या मदद के लिए बोलें।"""
        elif language == 'te':
            return """నమస్కారం! నేను సార్థి AI. నేను మీకు సహాయం చేయగలను:

1. ఆరోగ్య సలహా - జ్వరం, గాయం, ప్రాథమిక చికిత్స
2. ప్రభుత్వ పథకాలు - దరఖాస్తు ప్రక్రియ, ప్రయోజనాలు
3. వాతావరణ భద్రత - వేడి, వరద, విపత్తు భద్రత

దయచేసి మీ ప్రశ్న అడగండి లేదా సహాయం కోసం మాట్లాడండి."""
        else:
            return """Hello! I am Saarthi AI. I can help you with:

1. Health Advice - fever, injury, first aid
2. Government Schemes - application process, benefits
3. Climate Safety - heat, flood, disaster safety

Please ask your question or speak for help."""
