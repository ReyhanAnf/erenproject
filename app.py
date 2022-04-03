#====================
#== Import Module ===

from flask import Flask, render_template, request
import statistics as stat
import re
from flask_jsonpify import jsonify
import sys
import nltk
from rate import *
from predict import *
import sqlite3
#nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import joblib
from scrap import Scrap
from googletrans import  Translator
from langdetect import detect

#====================


#============================================
#== Load Module and configuration package ===

#Load Model Ml
vec = joblib.load("model/vector_ind.joblib")
pred = joblib.load("model/pnews_ind.joblib")
vec_en = joblib.load("model/vector_en.joblib")
pred_en = joblib.load("model/pnews_en.joblib")
#configuration package
port_stem = PorterStemmer()
ts = Translator()
bahasa = {"af": "afrikaans", "sq": "albanian", "am": "amharic", "ar": "arabic", "hy": "armenian", "az": "azerbaijani", "eu": "basque", "be": "belarusian", "bn": "bengali", "bs": "bosnian", "bg": "bulgarian", "ca": "catalan", "ceb": "cebuano", "ny": "chichewa", "zh-cn": "chinese (simplified)", "zh-tw": "chinese (traditional)", "co": "corsican", "hr": "croatian", "cs": "czech", "da": "danish", "nl": "dutch", "en": "english", "eo": "esperanto", "et": "estonian", "tl": "filipino", "fi": "finnish", "fr": "french", "fy": "frisian", "gl": "galician", "ka": "georgian", "de": "german", "el": "greek", "gu": "gujarati", "ht": "haitian creole", "ha": "hausa", "haw": "hawaiian", "iw": "hebrew", "hi": "hindi", "hmn": "hmong", "hu": "hungarian", "is": "icelandic", "ig": "igbo", "id": "indonesian", "ga": "irish", "it": "italian", "ja": "japanese", "jw": "javanese", "kn": "kannada", "kk": "kazakh", "km": "khmer", "ko": "korean", "ku": "kurdish (kurmanji)", "ky": "kyrgyz", "lo": "lao", "la": "latin", "lv": "latvian", "lt": "lithuanian", "lb": "luxembourgish", "mk": "macedonian", "mg": "malagasy", "ms": "malay", "ml": "malayalam", "mt": "maltese", "mi": "maori", "mr": "marathi", "mn": "mongolian", "my": "myanmar (burmese)", "ne": "nepali", "no": "norwegian", "ps": "pashto", "fa": "persian", "pl": "polish", "pt": "portuguese", "pa": "punjabi", "ro": "romanian", "ru": "russian", "sm": "samoan", "gd": "scots gaelic", "sr": "serbian", "st": "sesotho", "sn": "shona", "sd": "sindhi", "si": "sinhala", "sk": "slovak", "sl": "slovenian", "so": "somali", "es": "spanish", "su": "sundanese", "sw": "swahili", "sv": "swedish", "tg": "tajik", "ta": "tamil", "te": "telugu", "th": "thai", "tr": "turkish", "uk": "ukrainian", "ur": "urdu", "uz": "uzbek", "vi": "vietnamese", "cy": "welsh", "xh": "xhosa", "yi": "yiddish", "yo": "yoruba", "zu": "zulu", "fil": "Filipino", "he": "Hebrew"}

#============================================



#==========================================================
#== create function for stemmer and translate text data ===

#stremmer in Bahasa to all
def stemmingin(x1):
    #l = detect(stem_content)
    lg = "indonesian"
    stem_content = re.sub("[^a-zA-Z]", " ", str(x1))
    stem_content = stem_content.lower()
    stem_content = stem_content.split()
    stem_content = [port_stem.stem(word) for word in stem_content if not word is stopwords.words(lg)]  
    stem_content = " ".join(stem_content)
    print(stem_content)
    txt = ts.translate(stem_content, dest="indonesian")
    stem_content = txt.text
    return stem_content
#stremmer in Language to all
def stemmingen(x2):
    #l = detect(stem_content)
    lg = "english"
    stem_content = re.sub("[^a-zA-Z]", " ", str(x2))
    stem_content = stem_content.lower()
    stem_content = stem_content.split()
    stem_content = [port_stem.stem(word) for word in stem_content if not word is stopwords.words(lg)]  
    stem_content = " ".join(stem_content)
    
    txt = ts.translate(stem_content, dest="english")
    stem_content = txt.text
    return stem_content






#==========================================================




#==========================================================
#==========================================================
#== create flask app route ===
#==========================================================
#==========================================================

#====================
#== Import Module ===

app = Flask(__name__) 

#====================



#====================
#== Routing =========

#home
@app.route("/", methods=["GET","POST"]) 
def home():
    if request.method == "POST":
        if request.form.get("rbtn")=="Kirim Feedback":
             valrate = request.form.get("valrate")
             nama = request.form.get("nama")
             anonima = request.form.get("anonim")
             anonima = str(anonima)
             anonimc = ''
             if anonima == 'on':
                 anonimc += 'true'
             elif anonima == 'None':
                 anonimc += 'false'
             else:
                 print(anonima)
            
            
             ulas = request.form.get("ulas")
             if str(nama) == "None":
                 nama = "orang"
             else:
                 pass
             
             inputT(name=nama,rate=valrate,message=ulas, anonim=anonimc)
        else:
             print(request.form)
    else:
        pass
    
    data = printT()
    r_id = data["id"]
    rname = data["name"]
    rmessage = data["message"]
    r_rate = data["rate"]
    ranonim = data["anonim"]
    return render_template("kosong.html", drate=r_rate, dname=rname, did=r_id, dmessage=rmessage, danonim=ranonim)

#page one predict news
@app.route("/predict-news/", methods=["GET","POST"])
def news_pred():
    if request.method == "POST":
        if request.form.get("rbtn")=="Kirim Feedback":
             valrate = request.form.get("valrate")
             nama = request.form.get("nama")
             anonima = request.form.get("anonim")
             anonima = str(anonima)
             anonimc = ''
             if anonima == 'on':
                 anonimc += 'true'
             elif anonima == 'None':
                 anonimc += 'false'
             else:
                 print(anonima)
            
            
             ulas = request.form.get("ulas")
             if str(nama) == "None":
                 nama = "orang"
             else:
                 pass
             
             inputT(name=nama,rate=valrate,message=ulas, anonim=anonimc)
        else:
             print(request.form)
    else:
        pass
    
    data = printT()
    r_id = data["id"]
    rname = data["name"]
    rmessage = data["message"]
    r_rate = data["rate"]
    ranonim = data["anonim"]
    return render_template("predict-news.html", drate=r_rate, dname=rname, did=r_id, dmessage=rmessage, danonim = ranonim)

#result page predict news
@app.route("/predict-news/result/", methods=["GET", "POST"])
def result_np():
    print(request.form.get("yokpred"))
    if request.method == "POST":
        if request.form.get("yokpred")=="Predict":
           
            predscore_true = 50
            predscore_false = 50
            
            err = "False"
            text1 = ""
            tltext1 = ""
            title1 = []
            content1 = []
            
            if request.method == "POST":
                text = request.form.get("text")
                tltext = request.form.get("ttl")
                url = request.form.get("url")
                text1 += text
                tltext1 += tltext
            
            else:
                pass
            
            print("")
            if len(text) > 2:
                for n in range(2):
                    tltext = stemmingin(tltext)
                    text = stemmingen(text)
                    
                    tltext = vec.transform([tltext])
                    text = vec_en.transform([text])
                    
                    prediction1 = pred.predict(tltext)
                    prediction2 = pred_en.predict(text)
                    prediction = prediction1 + prediction2
                
                for i in prediction:
                    if i == 0:
                        predscore_true += 3
                    elif i == 1:
                        predscore_false += 2
                                           
                
            else:
                predscore_false += 0.5
                predscore_true += 0.5
            
            print("")
            
            if len(url) > 2:
                print("benar url")
                tc = Scrap(url)
                title = tc["title"]
                content = tc["content"]
                
                title1 += title
                content1 += content
                
                
                title = [stemmingin(t) for t in title]
                content = [stemmingen(c) for c in content]
                
                
                title = vec.transform(title)
                content = vec_en.transform(content)
                    
                prediction1 = pred.predict(title)
                prediction2 = pred_en.predict(content)
                prediction = prediction1 + prediction2
                
                for i in prediction:
                     if i == 0:
                        predscore_true += 3
                     elif i == 1:
                        predscore_false += 2

            
            else:
                predscore_false += 0.5
                predscore_true += 0.5

            
            
            persentrue = (100/(predscore_true + predscore_false)) * predscore_true
            persenfalse = (100/(predscore_true + predscore_false)) * predscore_false
            
            ac = ""
            at = ""
            for i in content1:
                ac += " " + i
            for i in title1:
                at += " " + i
            
            data = printT()
            r_id = data["id"]
            r_name = data["name"]
            r_rate = data["rate"]
            r_message = data["message"]
            inputTP(teks=text1,judul=tltext1,url=url,ujudul=at,ukonten=ac,pstrue=persentrue,psfalse=persenfalse,pdtrue=predscore_true,pdfalse=predscore_false,err=err)
              
        elif request.form.get("rbtn")=="Kirim Feedback":
             valrate = request.form.get("valrate")
             nama = request.form.get("nama")
             anonima = request.form.get("anonim")
             anonima = str(anonima)
             anonimc = ''
             if anonima == 'on':
                 anonimc += 'true'
             elif anonima == 'None':
                 anonimc += 'false'
             else:
                 print(anonima)
            
            
             ulas = request.form.get("ulas")
             if str(nama) == "None":
                 nama = "orang"
             else:
                 pass
             
             inputT(name=nama,rate=valrate,message=ulas, anonim=anonimc)
             datadb = printTP()
             """
             Ketentuan
             1. setiap prediksi benar memiliki poin +3
             2. setiap prediksi salah memiliki poin +2
             3. jika tidak ada nilai yang didapat, maka keduanya dapat poin masing masing 0.5
             3. Nilai awal setiap variabel yaitu 50
             """
            
             persentrue = datadb["pstrue"][-1]
             persenfalse =  datadb["psfalse"][-1]
             predscore_true =  datadb["pdtrue"][-1]
             predscore_false =  datadb["pdfalse"][-1]
             err =  datadb["err"][-1]
             tltext1 =  datadb["judul"][-1]
             text1 =  datadb["teks"][-1]
             ac =  datadb["ukonten"][-1]
             at =  datadb["ujudul"][-1]\
               
        else:
            print("ada yang salah di bagian tombol predict")
    else:
        print("ada yang salah di bagian metod")
    
    data = printT()
    ranonim = data["anonim"]
    r_id = data["id"]
    rname = data["name"]
    r_rate = data["rate"]
    rmessage = data["message"]
    return render_template("result_pn.html", danonime=ranonim, drate=r_rate, dname=rname, did=r_id, dmessage=rmessage, persen_benar=persentrue, persen_salah=persenfalse, n_benar=predscore_true, n_salah=predscore_false, error=err, text=text1, tltext=tltext1, tit=at, con=ac)
    



app.run(debug=True) 
















# @app.route("/function_route", methods=["GET", "POST"])
# def my_function():
#     if request.method == "POST":
#         data = {}# empty dict to store data
#         data["title"] = request.json["title"]
#         data["release_date"] = request.json["movie_release_date"]
        
#         #do whatever you want with the data here e.g look up in database or something
#         #if you want to print to console
        
#         print(data, file=sys.stderr)
        
#         #then return something back to frontend on success
#         #this returns back received data and you should see it in browser console
#         #because of the console.log() in the script.
#         return jsonify(data)
#     else:
#         print("aya nu salah")