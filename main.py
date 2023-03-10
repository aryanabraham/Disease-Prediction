{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5b88ddc3",
   "metadata": {},
   "source": [
    "# Importing Libraries "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5fa72d75",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "from tkinter import messagebox\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "719cc55a",
   "metadata": {},
   "source": [
    "# Creating list l1 for symptoms\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "4ef56a5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',\n",
    "    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',\n",
    "    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',\n",
    "    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',\n",
    "    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',\n",
    "    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',\n",
    "    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',\n",
    "    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',\n",
    "    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',\n",
    "    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',\n",
    "    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',\n",
    "    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',\n",
    "    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',\n",
    "    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',\n",
    "    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',\n",
    "    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',\n",
    "    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',\n",
    "    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "4a6d3a9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Creating list L2 for diseases \n",
    "disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',\n",
    "        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',\n",
    "        ' Migraine','Cervical spondylosis',\n",
    "        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',\n",
    "'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',\n",
    "'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',\n",
    "'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',\n",
    "'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',\n",
    "'Impetigo']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "2892a4bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating an empty list of size l1 and filling with 0\n",
    "l2=[]\n",
    "for x in range(0,len(l1)):\n",
    "    l2.append(0)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "724ce4c1",
   "metadata": {},
   "source": [
    "# Reading Training csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "bd02fbfb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  0,  0, ..., 38, 39, 40], dtype=int64)"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv(\"Training.csv\")\n",
    "\n",
    "# assigning each disease with an index\n",
    "df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,\n",
    "'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,\n",
    "'Migraine':11,'Cervical spondylosis':12,\n",
    "'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,\n",
    "'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,\n",
    "'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,\n",
    "'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,\n",
    "'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,\n",
    "'Impetigo':40}},inplace=True)\n",
    "\n",
    "X= df[l1]\n",
    "\n",
    "y = df[[\"prognosis\"]]\n",
    "np.ravel(y)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d8871c74",
   "metadata": {},
   "source": [
    "# Reading test file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c8a5071c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,\n",
       "       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,\n",
       "       34, 35, 36, 37, 38, 39, 40], dtype=int64)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tr=pd.read_csv(\"Testing.csv\")\n",
    "tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,\n",
    "'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,\n",
    "'Migraine':11,'Cervical spondylosis':12,\n",
    "'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,\n",
    "'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,\n",
    "'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,\n",
    "'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,\n",
    "'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,\n",
    "'Impetigo':40}},inplace=True)\n",
    "\n",
    "X_test= tr[l1]\n",
    "y_test = tr[[\"prognosis\"]]\n",
    "np.ravel(y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "812a7f77",
   "metadata": {},
   "source": [
    "# Message function to display final message"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5271a57a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def message():\n",
    "    if (Symptom1.get() == \"None\" and  Symptom2.get() == \"None\" and Symptom3.get() == \"None\" and Symptom4.get() == \"None\" and Symptom5.get() == \"None\"):\n",
    "        messagebox.showinfo(\"OOPS!!\", \"ENTER  SYMPTOMS PLEASE\")\n",
    "    else :\n",
    "        NaiveBayes()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7c94114a",
   "metadata": {},
   "source": [
    "# Multinomial Naive Bayes Algorithm "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "ed274b55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.0\n",
      "41\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\Aryan\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but MultinomialNB was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "def NaiveBayes():\n",
    "    from sklearn.naive_bayes import MultinomialNB\n",
    "    gnb = MultinomialNB()\n",
    "    gnb=gnb.fit(X,np.ravel(y))      # makes array 1D                        \n",
    "    from sklearn.metrics import accuracy_score\n",
    "    y_pred = gnb.predict(X_test)                            \n",
    "    print(accuracy_score(y_test, y_pred))                    \n",
    "    print(accuracy_score(y_test, y_pred, normalize=False))\n",
    "\n",
    "    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]\n",
    "\n",
    "    for k in range(0,len(l1)):\n",
    "        for z in psymptoms:\n",
    "            if(z==l1[k]):\n",
    "                l2[k]=1\n",
    "\n",
    "    inputtest = [l2]\n",
    "    predict = gnb.predict(inputtest)                                            \n",
    "    predicted=predict[0]\n",
    "\n",
    "    h='no'\n",
    "    for a in range(0,len(disease)):\n",
    "        if(disease[predicted] == disease[a]):\n",
    "            h='yes'\n",
    "            break\n",
    "\n",
    "    if (h=='yes'):\n",
    "        t3.delete(\"1.0\", END)                                      \n",
    "        t3.insert(END, disease[a])                                \n",
    "    else:\n",
    "        t3.delete(\"1.0\", END)\n",
    "        t3.insert(END, \"No Disease\")\n",
    "\n",
    "\n",
    "root = Tk()\n",
    "root.title(\"Diagnosing of Disease using Machine Learning\")\n",
    "root.configure()\n",
    "\n",
    "Symptom1 = StringVar()\n",
    "Symptom1.set(None)\n",
    "Symptom2 = StringVar()\n",
    "Symptom2.set(None)\n",
    "Symptom3 = StringVar()\n",
    "Symptom3.set(None)\n",
    "Symptom4 = StringVar()\n",
    "Symptom4.set(None)\n",
    "Symptom5 = StringVar()\n",
    "Symptom5.set(None)\n",
    "\n",
    "w2 = Label(root, justify=LEFT, text=\"Please enter your symptoms\")\n",
    "w2.config(font=(\"Elephant\", 30))\n",
    "w2.grid(row=1, column=0, columnspan=2, padx=100)\n",
    "\n",
    "NameLb1 = Label(root, text=\"\")\n",
    "NameLb1.config(font=(\"Elephant\", 20))\n",
    "NameLb1.grid(row=5, column=1, pady=10,  sticky=W)\n",
    "\n",
    "S1Lb = Label(root,  text=\"Symptom 1\")\n",
    "S1Lb.config(font=(\"Elephant\", 15))\n",
    "S1Lb.grid(row=7, column=1, pady=10 , sticky=W)\n",
    "\n",
    "S2Lb = Label(root,  text=\"Symptom 2\")\n",
    "S2Lb.config(font=(\"Elephant\", 15))\n",
    "S2Lb.grid(row=8, column=1, pady=10, sticky=W)\n",
    "\n",
    "S3Lb = Label(root,  text=\"Symptom 3\")\n",
    "S3Lb.config(font=(\"Elephant\", 15))\n",
    "S3Lb.grid(row=9, column=1, pady=10, sticky=W)\n",
    "\n",
    "S4Lb = Label(root,  text=\"Symptom 4\")\n",
    "S4Lb.config(font=(\"Elephant\", 15))\n",
    "S4Lb.grid(row=10, column=1, pady=10, sticky=W)\n",
    "\n",
    "S5Lb = Label(root,  text=\"Symptom 5\")\n",
    "S5Lb.config(font=(\"Elephant\", 15))\n",
    "S5Lb.grid(row=11, column=1, pady=10, sticky=W)\n",
    "\n",
    "lr = Button(root, text=\"Predict\",height=2, width=20, command=message)\n",
    "lr.config(font=(\"Elephant\", 15))\n",
    "lr.grid(row=15, column=1,pady=20)\n",
    "\n",
    "OPTIONS = sorted(l1)\n",
    "\n",
    "S1En = OptionMenu(root, Symptom1,*OPTIONS)\n",
    "S1En.grid(row=7, column=2)\n",
    "\n",
    "S2En = OptionMenu(root, Symptom2,*OPTIONS)\n",
    "S2En.grid(row=8, column=2)\n",
    "\n",
    "S3En = OptionMenu(root, Symptom3,*OPTIONS)\n",
    "S3En.grid(row=9, column=2)\n",
    "\n",
    "S4En = OptionMenu(root, Symptom4,*OPTIONS)\n",
    "S4En.grid(row=10, column=2)\n",
    "\n",
    "S5En = OptionMenu(root, Symptom5,*OPTIONS)\n",
    "S5En.grid(row=11, column=2)\n",
    "\n",
    "NameLb = Label(root, text=\"\")\n",
    "NameLb.config(font=(\"Elephant\", 20))\n",
    "NameLb.grid(row=13, column=1, pady=10,  sticky=W)\n",
    "\n",
    "NameLb = Label(root, text=\"\")\n",
    "NameLb.config(font=(\"Elephant\", 15))\n",
    "NameLb.grid(row=18, column=1, pady=10,  sticky=W)\n",
    "\n",
    "t3 = Text(root, height=2, width=30)\n",
    "t3.config(font=(\"Elephant\", 20))\n",
    "t3.grid(row=20, column=1 , padx=10)\n",
    "\n",
    "root.mainloop()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]"
  },
  "vscode": {
   "interpreter": {
    "hash": "25d9d3c7995d1295c4e90ce0d967b893116c8cb57cac7d0e3327b2e0bf889a8a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
