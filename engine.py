from experta import *
from diseases import diseases
from ioprepare import (
    get_response,
    disease_matched_render,
    disease_not_matched_render,
    init_render
)


class InferenceEngine(KnowledgeEngine):
    @DefFacts()
    def _init_engine(self):
        init_render()
        yield Fact(action='deduce_disease')

    # Stuffy nose
    @Rule(Fact(action='deduce_disease'), NOT(Fact(stuffy_nose=W())), salience=1)
    def stuffy_nose(self):
        self.declare(Fact(stuffy_nose=get_response('¿Tiene nariz congestionada? (si/no): ')))

    # Asthenia
    @Rule(Fact(action='deduce_disease'), NOT(Fact(asthenia=W())), salience=1)
    def asthenia(self):
        self.declare(Fact(asthenia=get_response('¿Tiene astenia (cansancio)? (si/no): ')))

    # Loss voice
    @Rule(Fact(action='deduce_disease'), NOT(Fact(loss_voice=W())), salience=1)
    def loss_voice(self):
        self.declare(Fact(loss_voice=get_response('¿Tiene perdida de voz? (si/no): ')))

    # Watery eyes
    @Rule(Fact(action='deduce_disease'), NOT(Fact(watery_eyes=W())), salience=1)
    def watery_eyes(self):
        self.declare(Fact(watery_eyes=get_response('¿Tiene ojos llorosos? (si/no): ')))

    # Intercostal retreat
    @Rule(Fact(action='deduce_disease'), NOT(Fact(intercostal_retreat=W())), salience=1)
    def intercostal_retreat(self):
        self.declare(Fact(intercostal_retreat=get_response('¿Tiene tiraje intercostal (movimiento de los musculos '
                                                           'hacia adentro entre las costillas)? (si/no): ')))

    # Diarrhoea
    @Rule(Fact(action='deduce_disease'), NOT(Fact(diarrhoea=W())), salience=1)
    def diarrhoea(self):
        self.declare(Fact(diarrhoea=get_response('¿Tiene diarrea? (si/no): ')))

    # Facial pain
    @Rule(Fact(action='deduce_disease'), NOT(Fact(facial_pain=W())), salience=1)
    def facial_pain(self):
        self.declare(Fact(facial_pain=get_response('¿Tiene dolor facial? (si/no): ')))

    # Familiar diseases inheritance
    @Rule(Fact(action='deduce_disease'), NOT(Fact(diseases_inheritance=W())), salience=1)
    def diseases_inheritance(self):
        self.declare(Fact(diseases_inheritance=get_response('¿Cuenta con antecedentes heredofamiliares? (si/no): ')))

    # Shortness breath
    @Rule(Fact(action='deduce_disease'), NOT(Fact(shortness_breath=W())), salience=1)
    def shortness_breath(self):
        self.declare(Fact(shortness_breath=get_response('¿Tiene problemas para respirar? (si/no): ')))

    # Recurrent headache
    @Rule(Fact(action='deduce_disease'), NOT(Fact(recurrent_headache=W())), salience=1)
    def recurrent_headache(self):
        self.declare(Fact(recurrent_headache=get_response('¿Tiene dolor de cabeza recurrente? (si/no): ')))

    # Bad breath
    @Rule(Fact(action='deduce_disease'), NOT(Fact(bad_breath=W())), salience=1)
    def bad_breath(self):
        self.declare(Fact(bad_breath=get_response('¿Tiene mal aliento? (si/no): ')))

    # Skin irritation
    @Rule(Fact(action='deduce_disease'), NOT(Fact(skin_irritation=W())), salience=1)
    def skin_irritation(self):
        self.declare(Fact(skin_irritation=get_response('¿Tiene irritacion cutanea? (si/no): ')))

    # Tobacco
    @Rule(Fact(action='deduce_disease'), NOT(Fact(tobacco=W())), salience=1)
    def tobacco(self):
        self.declare(Fact(tobacco=get_response('¿Ha consumido tabaco? (si/no): ')))

    # High saliva production
    @Rule(Fact(action='deduce_disease'), NOT(Fact(high_saliva=W())), salience=1)
    def high_saliva(self):
        self.declare(Fact(high_saliva=get_response('¿Tiene alta produccion de saliva? (si/no): ')))

    # Slow and prolonged breathing
    @Rule(Fact(action='deduce_disease'), NOT(Fact(slow_prolonged_breathing=W())), salience=1)
    def slow_prolonged_breathing(self):
        self.declare(Fact(slow_prolonged_breathing=get_response('¿Tiene respiraciones pausadas '
                                                                'y prolongadas? (si/no): ')))

    # Itchy palate
    @Rule(Fact(action='deduce_disease'), NOT(Fact(itchy_palate=W())), salience=1)
    def itchy_palate(self):
        self.declare(Fact(itchy_palate=get_response('¿Tiene comezon en el paladar? (si/no): ')))

    # Abdominal pain
    @Rule(Fact(action='deduce_disease'), NOT(Fact(abdominal_pain=W())), salience=1)
    def abdominal_pain(self):
        self.declare(Fact(abdominal_pain=get_response('¿Tiene dolor abdominal? (si/no): ')))

    # Chest pain
    @Rule(Fact(action='deduce_disease'), NOT(Fact(chest_pain=W())), salience=1)
    def chest_pain(self):
        self.declare(Fact(chest_pain=get_response('¿Tiene dolor de pecho? (si/no): ')))

    # Cough and vomiting
    @Rule(Fact(action='deduce_disease'), NOT(Fact(cough_vomiting=W())), salience=1)
    def cough_vomiting(self):
        self.declare(Fact(cough_vomiting=get_response('¿Tiene tos con vomito? (si/no): ')))

    # Sore throat
    @Rule(Fact(action='deduce_disease'), NOT(Fact(sore_throat=W())), salience=1)
    def sore_throat(self):
        self.declare(Fact(sore_throat=get_response('¿Tiene dolor de garganta al ingerir alimento? (si/no): ')))

    # Loud snoring
    @Rule(Fact(action='deduce_disease'), NOT(Fact(loud_snoring=W())), salience=1)
    def loud_snoring(self):
        self.declare(Fact(loud_snoring=get_response('¿Tiene ronquidos fuertes? (si/no): ')))

    # Bucopharyngeal inflammation
    @Rule(Fact(action='deduce_disease'), NOT(Fact(bucopharyngeal_inflammation=W())), salience=1)
    def bucopharyngeal_inflammation(self):
        self.declare(Fact(bucopharyngeal_inflammation=get_response('¿Tiene inflamacion bucofaringea? (si/no): ')))

    # Cough
    @Rule(Fact(action='deduce_disease'), NOT(Fact(cough=W())), salience=1)
    def cough(self):
        self.declare(Fact(cough=get_response('¿Tiene tos? (si/no): ')))

    # Cyanosis
    @Rule(Fact(action='deduce_disease'), NOT(Fact(cyanosis=W())), salience=1)
    def cyanosis(self):
        self.declare(Fact(cyanosis=get_response('¿Presenta cianosis (coloracion en los dedos)? (si/no): ')))

    # Sneeze
    @Rule(Fact(action='deduce_disease'), NOT(Fact(sneeze=W())), salience=1)
    def sneeze(self):
        self.declare(Fact(sneeze=get_response('¿Tiene estornudos? (si/no): ')))

    # Red feet
    @Rule(Fact(action='deduce_disease'), NOT(Fact(red_feet=W())), salience=1)
    def red_feet(self):
        self.declare(Fact(red_feet=get_response('¿Tiene coloracion rojiza en los pies? (si/no): ')))

    # Recurrent sneeze
    @Rule(Fact(action='deduce_disease'), NOT(Fact(recurrent_sneeze=W())), salience=1)
    def recurrent_sneeze(self):
        self.declare(Fact(recurrent_sneeze=get_response('¿Tiene estornudos continuos? (si/no): ')))

    # Weight loss
    @Rule(Fact(action='deduce_disease'), NOT(Fact(weight_loss=W())), salience=1)
    def weight_loss(self):
        self.declare(Fact(weight_loss=get_response('¿Tiene perdida de peso? (si/no): ')))

    # Rattles
    @Rule(Fact(action='deduce_disease'), NOT(Fact(rattles=W())), salience=1)
    def rattles(self):
        self.declare(Fact(rattles=get_response('¿Tiene estertores (ruidos anormales en la respiracion)? (si/no): ')))

    # Sialorrhea
    @Rule(Fact(action='deduce_disease'), NOT(Fact(sialorrhea=W())), salience=1)
    def sialorrhea(self):
        self.declare(Fact(sialorrhea=get_response('¿Tiene sialorrea (exceso de saliva)? (si/no): ')))

    # Thoracic pain
    @Rule(Fact(action='deduce_disease'), NOT(Fact(thoracic_pain=W())), salience=1)
    def thoracic_pain(self):
        self.declare(Fact(thoracic_pain=get_response('¿Presenta dolor toracico? (si/no): ')))

    # Cough whistle
    @Rule(Fact(action='deduce_disease'), NOT(Fact(cough_whistle=W())), salience=1)
    def cough_whistle(self):
        self.declare(Fact(cough_whistle=get_response('¿Se escucha un silbido cuando tose? (si/no): ')))

    # Runny nose
    @Rule(Fact(action='deduce_disease'), NOT(Fact(runny_nose=W())), salience=1)
    def runny_nose(self):
        self.declare(Fact(runny_nose=get_response('¿Tiene secresion nasal? (si/no): ')))

    # Itchy nose
    @Rule(Fact(action='deduce_disease'), NOT(Fact(itchy_nose=W())), salience=1)
    def itchy_nose(self):
        self.declare(Fact(itchy_nose=get_response('¿Tiene comezon de nariz? (si/no): ')))

    # Fatigue
    @Rule(Fact(action='deduce_disease'), NOT(Fact(fatigue=W())), salience=1)
    def fatigue(self):
        self.declare(Fact(fatigue=get_response('¿Tiene fatiga? (si/no): ')))

    # Colored mucus
    @Rule(Fact(action='deduce_disease'), NOT(Fact(colored_mucus=W())), salience=1)
    def colored_mucus(self):
        self.declare(Fact(colored_mucus=get_response('¿Tiene mucosidad transparente, blanca, gris, amarillenta? ('
                                                     'si/no): ')))

    # Toxic agents
    @Rule(Fact(action='deduce_disease'), NOT(Fact(toxic_agents=W())), salience=1)
    def toxic_agents(self):
        self.declare(Fact(toxic_agents=get_response('¿Ha respirado agentes toxicos? (si/no): ')))

    # Fever
    @Rule(Fact(action='deduce_disease'), NOT(Fact(fever=W())), salience=1)
    def fever(self):
        self.declare(Fact(fever=get_response('¿Tiene fiebre? (si/no): ')))

    # Appetite loss
    @Rule(Fact(action='deduce_disease'), NOT(Fact(appetite_loss=W())), salience=1)
    def appetite_loss(self):
        self.declare(Fact(appetite_loss=get_response('¿Tiene perdida de apetito? (si/no): ')))

    # Obesity
    @Rule(Fact(action='deduce_disease'), NOT(Fact(obesity=W())), salience=1)
    def obesity(self):
        self.declare(Fact(obesity=get_response('¿Tiene obesidad? (si/no): ')))

    # Cough absence
    @Rule(Fact(action='deduce_disease'), NOT(Fact(cough_absence=W())), salience=1)
    def cough_absence(self):
        self.declare(Fact(cough_absence=get_response('¿Tiene ausencia de tos? (si/no): ')))

    # Dry cough
    @Rule(Fact(action='deduce_disease'), NOT(Fact(dry_cough=W())), salience=1)
    def dry_cough(self):
        self.declare(Fact(dry_cough=get_response('¿Tiene tos seca? (si/no): ')))

    # Non-productive cough
    @Rule(Fact(action='deduce_disease'), NOT(Fact(non_productive_cough=W())), salience=1)
    def non_productive_cough(self):
        self.declare(Fact(non_productive_cough=get_response('¿Tiene tos no productiva? (si/no): ')))

    # Fever presence
    @Rule(Fact(action='deduce_disease'), NOT(Fact(fever_presence=W())), salience=1)
    def fever_presence(self):
        self.declare(Fact(fever_presence=get_response('¿Ha presentado fiebre? (si/no): ')))

    # Hyaline nasal mucus
    @Rule(Fact(action='deduce_disease'), NOT(Fact(hyaline_nasal_mucus=W())), salience=1)
    def hyaline_nasal_mucus(self):
        self.declare(Fact(hyaline_nasal_mucus=get_response('¿Tiene moco nasal hialino (transparente y blanco)? ('
                                                           'si/no): ')))

    # Itchy eyes
    @Rule(Fact(action='deduce_disease'), NOT(Fact(itchy_eyes=W())), salience=1)
    def itchy_eyes(self):
        self.declare(Fact(itchy_eyes=get_response('¿Tiene comezon de ojos? (si/no): ')))

    # Itchy throat
    @Rule(Fact(action='deduce_disease'), NOT(Fact(itchy_throat=W())), salience=1)
    def itchy_throat(self):
        self.declare(Fact(itchy_throat=get_response('¿Tiene cosquilleo y aspereza en la garganta? (si/no): ')))

    # Weakness
    @Rule(Fact(action='deduce_disease'), NOT(Fact(weakness=W())), salience=1)
    def weakness(self):
        self.declare(Fact(weakness=get_response('¿Sufre de debilidad? (si/no): ')))

    # Taste disturbance
    @Rule(Fact(action='deduce_disease'), NOT(Fact(taste_disturbance=W())), salience=1)
    def taste_disturbance(self):
        self.declare(Fact(taste_disturbance=get_response('¿Tiene alteraciones al gusto? (si/no): ')))

    # -------------------------------------- Diseases -----------------------------------------

    # Apnoea
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='no'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='no'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='si'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='si'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='no'),
        Fact(obesity='si'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def apnoea(self):
        self.declare(Fact(disease='apnea'))

    # Sinusitis
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='si'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='si'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='no'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='si'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='si')
    )
    def sinusitis(self):
        self.declare(Fact(disease='sinusitis'))

    # Rhinitis
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='si'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='si'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='no'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='si'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='si'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='si'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='si'),
        Fact(itchy_eyes='si'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def rhinitis(self):
        self.declare(Fact(disease='rinitis'))

    # Silicosis
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='no'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='si'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='si'),
        Fact(fever='si'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='si'),
        Fact(taste_disturbance='no')
    )
    def silicosis(self):
        self.declare(Fact(disease='silicosis'))

    # Fibrosis
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='no'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='si'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='si'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='si'),
        Fact(cyanosis='si'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def fibrosis(self):
        self.declare(Fact(disease='fibrosis'))

    # Tonsillitis
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='si'),
        Fact(asthenia='si'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='no'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='si'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='si'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='si'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='si'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def tonsillitis(self):
        self.declare(Fact(disease='amigdalitis'))

    # Pulmonary emphysema
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='no'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='si'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='si'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='si'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='si'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def pulmonary_emphysema(self):
        self.declare(Fact(disease='efisema pulmonar'))

    # Pneumothorax
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='no'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='si'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='si'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='si'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='si'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def pneumothorax(self):
        self.declare(Fact(disease='neumotorax'))

    # Bronchiolitis
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='no'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='si'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='si'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='si'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='si'),
        Fact(rattles='no'),
        Fact(sialorrhea='si'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='si'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def bronchiolitis(self):
        self.declare(Fact(disease='bronquiolitis'))

    # Epoc
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='no'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='si'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='si'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='si'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def epoc(self):
        self.declare(Fact(disease='epoc'))

    # Bronchitis
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='no'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='no'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='si'),
        Fact(colored_mucus='si'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='si'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def bronchitis(self):
        self.declare(Fact(disease='bronquitis'))

    # Pneumonia
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='no'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='no'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='si'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='si'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='si'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def pneumonia(self):
        self.declare(Fact(disease='neumonia'))

    # Asthma
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='no'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='si'),
        Fact(shortness_breath='si'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='si'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def asthma(self):
        self.declare(Fact(disease='asma'))

    # Common cold
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='si'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='no'),
        Fact(recurrent_headache='si'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='si'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='si'),
        Fact(cyanosis='no'),
        Fact(sneeze='si'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='si'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def common_cold(self):
        self.declare(Fact(disease='resfriado comun'))

    # Influenza
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='si'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='si'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='no'),
        Fact(recurrent_headache='si'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='si'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='si'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='si'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def influenza(self):
        self.declare(Fact(disease='influenza'))

    # Pharyngitis
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='si'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='no'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='si'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='si'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='si'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def pharyngitis(self):
        self.declare(Fact(disease='faringitis'))

    # Laryngitis
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='no'),
        Fact(asthenia='no'),
        Fact(loss_voice='si'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='no'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='no'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='si'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='no'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='si'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def laryngitis(self):
        self.declare(Fact(disease='laringitis'))

    # Epiglottitis
    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose='no'),
        Fact(asthenia='no'),
        Fact(loss_voice='no'),
        Fact(watery_eyes='no'),
        Fact(intercostal_retreat='no'),
        Fact(diarrhoea='no'),
        Fact(facial_pain='no'),
        Fact(diseases_inheritance='no'),
        Fact(shortness_breath='si'),
        Fact(recurrent_headache='no'),
        Fact(bad_breath='no'),
        Fact(skin_irritation='no'),
        Fact(tobacco='no'),
        Fact(high_saliva='si'),
        Fact(slow_prolonged_breathing='no'),
        Fact(itchy_palate='no'),
        Fact(abdominal_pain='no'),
        Fact(chest_pain='no'),
        Fact(cough_vomiting='no'),
        Fact(sore_throat='no'),
        Fact(loud_snoring='no'),
        Fact(bucopharyngeal_inflammation='si'),
        Fact(cough='no'),
        Fact(cyanosis='no'),
        Fact(sneeze='no'),
        Fact(red_feet='no'),
        Fact(recurrent_sneeze='no'),
        Fact(weight_loss='no'),
        Fact(rattles='no'),
        Fact(sialorrhea='no'),
        Fact(thoracic_pain='no'),
        Fact(cough_whistle='no'),
        Fact(runny_nose='no'),
        Fact(itchy_nose='no'),
        Fact(fatigue='no'),
        Fact(colored_mucus='no'),
        Fact(toxic_agents='no'),
        Fact(fever='no'),
        Fact(appetite_loss='no'),
        Fact(obesity='no'),
        Fact(cough_absence='no'),
        Fact(dry_cough='no'),
        Fact(non_productive_cough='no'),
        Fact(fever_presence='no'),
        Fact(hyaline_nasal_mucus='no'),
        Fact(itchy_eyes='no'),
        Fact(itchy_throat='no'),
        Fact(weakness='no'),
        Fact(taste_disturbance='no')
    )
    def epiglottitis(self):
        self.declare(Fact(disease='epiglotitis'))

    # -------------------------------------- Deduction -----------------------------------------

    @Rule(Fact(action='deduce_disease'), Fact(disease=MATCH.disease), salience=-998)
    def disease_matched(self, disease):
        disease_matched_render(disease)

    @Rule(
        Fact(action='deduce_disease'),
        Fact(stuffy_nose=MATCH.stuffy_nose),
        Fact(asthenia=MATCH.asthenia),
        Fact(loss_voice=MATCH.loss_voice),
        Fact(watery_eyes=MATCH.watery_eyes),
        Fact(intercostal_retreat=MATCH.intercostal_retreat),
        Fact(diarrhoea=MATCH.diarrhoea),
        Fact(facial_pain=MATCH.facial_pain),
        Fact(diseases_inheritance=MATCH.diseases_inheritance),
        Fact(shortness_breath=MATCH.shortness_breath),
        Fact(recurrent_headache=MATCH.recurrent_headache),
        Fact(bad_breath=MATCH.bad_breath),
        Fact(skin_irritation=MATCH.skin_irritation),
        Fact(tobacco=MATCH.tobacco),
        Fact(high_saliva=MATCH.high_saliva),
        Fact(slow_prolonged_breathing=MATCH.slow_prolonged_breathing),
        Fact(itchy_palate=MATCH.itchy_palate),
        Fact(abdominal_pain=MATCH.abdominal_pain),
        Fact(chest_pain=MATCH.chest_pain),
        Fact(cough_vomiting=MATCH.cough_vomiting),
        Fact(sore_throat=MATCH.sore_throat),
        Fact(loud_snoring=MATCH.loud_snoring),
        Fact(bucopharyngeal_inflammation=MATCH.bucopharyngeal_inflammation),
        Fact(cough=MATCH.cough),
        Fact(cyanosis=MATCH.cyanosis),
        Fact(sneeze=MATCH.sneeze),
        Fact(red_feet=MATCH.red_feet),
        Fact(recurrent_sneeze=MATCH.recurrent_sneeze),
        Fact(weight_loss=MATCH.weight_loss),
        Fact(rattles=MATCH.rattles),
        Fact(sialorrhea=MATCH.sialorrhea),
        Fact(thoracic_pain=MATCH.thoracic_pain),
        Fact(cough_whistle=MATCH.cough_whistle),
        Fact(runny_nose=MATCH.runny_nose),
        Fact(itchy_nose=MATCH.itchy_nose),
        Fact(fatigue=MATCH.fatigue),
        Fact(colored_mucus=MATCH.colored_mucus),
        Fact(toxic_agents=MATCH.toxic_agents),
        Fact(fever=MATCH.fever),
        Fact(appetite_loss=MATCH.appetite_loss),
        Fact(obesity=MATCH.obesity),
        Fact(cough_absence=MATCH.cough_absence),
        Fact(dry_cough=MATCH.dry_cough),
        Fact(non_productive_cough=MATCH.non_productive_cough),
        Fact(fever_presence=MATCH.fever_presence),
        Fact(hyaline_nasal_mucus=MATCH.hyaline_nasal_mucus),
        Fact(itchy_eyes=MATCH.itchy_eyes),
        Fact(itchy_throat=MATCH.itchy_throat),
        Fact(weakness=MATCH.weakness),
        Fact(taste_disturbance=MATCH.taste_disturbance),
        NOT(Fact(disease=MATCH.disease)),
        salience=-998
    )
    def disease_not_matched(self, stuffy_nose, asthenia, loss_voice, watery_eyes, intercostal_retreat, diarrhoea,
                            facial_pain, diseases_inheritance, shortness_breath, recurrent_headache, bad_breath,
                            skin_irritation, tobacco, high_saliva, slow_prolonged_breathing, itchy_palate,
                            abdominal_pain, chest_pain, cough_vomiting, sore_throat, loud_snoring,
                            bucopharyngeal_inflammation, cough, cyanosis, sneeze, red_feet, recurrent_sneeze,
                            weight_loss, rattles, sialorrhea, thoracic_pain, cough_whistle, runny_nose, itchy_nose,
                            fatigue, colored_mucus, toxic_agents, fever, appetite_loss, obesity, cough_absence,
                            dry_cough, non_productive_cough, fever_presence, hyaline_nasal_mucus, itchy_eyes,
                            itchy_throat, weakness, taste_disturbance,
                            ):
        symptoms_map = {
            'stuffy_nose': stuffy_nose,
            'asthenia': asthenia,
            'loss_voice': loss_voice,
            'watery_eyes': watery_eyes,
            'intercostal_retreat': intercostal_retreat,
            'diarrhoea': diarrhoea,
            'facial_pain': facial_pain,
            'diseases_inheritance': diseases_inheritance,
            'shortness_breath': shortness_breath,
            'recurrent_headache': recurrent_headache,
            'bad_breath': bad_breath,
            'skin_irritation': skin_irritation,
            'tobacco': tobacco,
            'high_saliva': high_saliva,
            'slow_prolonged_breathing': slow_prolonged_breathing,
            'itchy_palate': itchy_palate,
            'abdominal_pain': abdominal_pain,
            'chest_pain': chest_pain,
            'cough_vomiting': cough_vomiting,
            'sore_throat': sore_throat,
            'loud_snoring': loud_snoring,
            'bucopharyngeal_inflammation': bucopharyngeal_inflammation,
            'cough': cough,
            'cyanosis': cyanosis,
            'sneeze': sneeze,
            'red_feet': red_feet,
            'recurrent_sneeze': recurrent_sneeze,
            'weight_loss': weight_loss,
            'rattles': rattles,
            'sialorrhea': sialorrhea,
            'thoracic_pain': thoracic_pain,
            'cough_whistle': cough_whistle,
            'runny_nose': runny_nose,
            'itchy_nose': itchy_nose,
            'fatigue': fatigue,
            'colored_mucus': colored_mucus,
            'toxic_agents': toxic_agents,
            'fever': fever,
            'appetite_loss': appetite_loss,
            'obesity': obesity,
            'cough_absence': cough_absence,
            'dry_cough': dry_cough,
            'non_productive_cough': non_productive_cough,
            'fever_presence': fever_presence,
            'hyaline_nasal_mucus': hyaline_nasal_mucus,
            'itchy_eyes': itchy_eyes,
            'itchy_throat': itchy_throat,
            'weakness': weakness,
            'taste_disturbance': taste_disturbance
        }
        percentages = {
            'apnea': 0,
            'sinusitis': 0,
            'rinitis': 0,
            'silicosis': 0,
            'fibrosis': 0,
            'amigdalitis': 0,
            'efisema pulmonar': 0,
            'neumotorax': 0,
            'bronquiolitis': 0,
            'epoc': 0,
            'bronquitis': 0,
            'neumonia': 0,
            'asma': 0,
            'resfriado comun': 0,
            'influenza': 0,
            'faringitis': 0,
            'laringitis': 0,
            'epiglotitis': 0
        }
        affirmative_symptoms = set([symptom for symptom in symptoms_map if symptoms_map[symptom] == 'si'])
        for d in diseases:
            symptoms = diseases[d]['symptoms']
            symptoms_len = len(symptoms)
            intersection_len = len(symptoms.intersection(affirmative_symptoms))
            percentage = (intersection_len / symptoms_len) * 100
            percentages[d] = percentage
        disease_not_matched_render(percentages)
