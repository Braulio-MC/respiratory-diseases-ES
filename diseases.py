diseases = {
    'apnea': {
        'questions': [
            '¿Tiene obesidad?',
            '¿Tiene respiraciones pausadas y prolongadas?',
            '¿Tiene ronquidos fuertes?'
        ],
        'symptoms': {
            'obesity',
            'slow_prolonged_breathing',
            'loud_snoring'
        },
        'treatment': '''Para aquellos casos leves se recomienda cambiar elementos del estilo de vida como adelgazar o 
dejar de fumar, puede darse el caso de necesitar terapias con ayuda de dispostivos, consistiendo en 
ejercicios de presion de aire por medio de mascarilla mientras se duerme, en caso de que las terapias no 
funcionen se requerira cirugia'''
    },
    'sinusitis': {
        'questions': [
            '¿Tiene dolor facial?',
            '¿Tiene alteraciones al gusto?',
            '¿Tiene mal aliento?',
            '¿Tiene nariz congestionada?'
        ],
        'symptoms': {
            'facial_pain',
            'taste_disturbance',
            'bad_breath',
            'stuffy_nose'
        },
        'treatment': '''Uso de antibioticos en caso de sinusitis bacteriana'''
    },
    'rinitis': {
        'questions': [
            '¿Tiene estornudos continuos?',
            '¿Tiene comezon de nariz?',
            '¿Tiene moco nasal hialino (transparente y blanco)?',
            '¿Tiene ojos llorosos?',
            '¿Tiene nariz congestionada?',
            '¿Tiene comezon de ojos?',
            '¿Tiene comezon en el paladar?'
        ],
        'symptoms': {
            'recurrent_sneeze',
            'itchy_nose',
            'hyaline_nasal_mucus',
            'watery_eyes',
            'stuffy_nose',
            'itchy_eyes',
            'itchy_palate'
        },
        'treatment': '''Evitar en la medida de lo posible el contacto con los alérgenos, el médico puede prescribir 
antihistamínicos y corticoides para paliar los síntomas, la administración de inhaladores con corticoides 
tópicos como la fluticasona puede mejorar estos síntomas'''
    },
    'silicosis': {
        'questions': [
            '¿Ha respirado agentes toxicos?',
            '¿Tiene problemas para respirar?',
            '¿Sufre de debilidad?',
            '¿Tiene fiebre?',
        ],
        'symptoms': {
            'toxic_agents',
            'shortness_breath',
            'weakness',
            'fever'
        },
        'treatment': '''Se prescribe antibioticos para las infecciones respiratorias complementando con oxigeno, 
brincodilatadores y evitar la exposicion al silice para evitar un empeoramiento'''
    },
    'fibrosis': {
        'questions': [
            '¿Tiene irritacion cutanea?',
            '¿Tiene problemas para respirar?',
            '¿Tiene tos?',
            '¿Presenta cianosis (coloracion en los dedos)?'
        ],
        'symptoms': {
            'skin_irritation',
            'shortness_breath',
            'cough',
            'cyanosis'
        },
        'treatment': '''Utilizar farmacos antifibroticos como complementar con uso de oxigeno para facilitar la 
respiracion, se recomienda administrar B2'''
    },
    'amigdalitis': {
        'questions': [
            '¿Ha presentado fiebre?',
            '¿Tiene secresion nasal?',
            '¿Tiene astenia (cansancio)?',
            '¿Tiene ausencia de tos?',
            '¿Tiene dolor de garganta al ingerir alimento?',
            '¿Tiene nariz congestionada?'
        ],
        'symptoms': {
            'fever_presence',
            'runny_nose',
            'asthenia',
            'cough_absence',
            'sore_throat',
            'stuffy_nose'
        },
        'treatment': '''Fomentar descanso, como proprocionar liquidos adecuados para prevenir la deshidratacion, 
bocadillos frios pueden ayudar a aliviar el dolor de garganta en caso de ser necesario se recetara un 
antibiotico, como tambien antiinflamatorios o analgesicos'''
    },
    'efisema pulmonar': {
        'questions': [
            '¿Tiene problemas para respirar?',
            '¿Tiene tos?',
            '¿Tiene coloracion rojiza en los pies?',
            '¿Ha consumido tabaco?'
        ],
        'symptoms': {
            'shortness_breath',
            'cough',
            'red_feet',
            'tobacco'
        },
        'treatment': '''Ese puede no curarse, pero ayudara a aliviar los sintomas con el uso de Broncodilatadores que 
ayudaran a aliviar la tos como la falta de aire, uso de antibioticos y/o cortcoesteroides inhalados para 
reducir la inflamacion'''
    },
    'neumotorax': {
        'questions': [
            '¿Tiene dolor de pecho?',
            '¿Tiene problemas para respirar?',
            '¿Tiene tos seca?',
            '¿Presenta dolor toracico?'
        ],
        'symptoms': {
            'chest_pain',
            'shortness_breath',
            'dry_cough',
            'thoracic_pain'
        },
        'treatment': '''Se busca aliviar la presion al pulmon para permitir que este pueda expandirse,
por lo que estar en observacion con el paciente es fundamental como tambien aspiracion con aguja, 
reparacion no quirurjuca, incluso terapias de oxigeno'''
    },
    'bronquiolitis': {
        'questions': [
            '¿Tiene dolor abdominal?',
            '¿Tiene perdida de apetito?',
            '¿Tiene problemas para respirar?',
            '¿Tiene perdida de peso?',
            '¿Tiene tiraje intercostal (movimiento de los musculos hacia adentro entre las costillas)?',
            '¿Tiene sialorrea (exceso de saliva)?'
        ],
        'symptoms': {
            'abdominal_pain',
            'appetite_loss',
            'shortness_breath',
            'weight_loss',
            'intercostal_retreat',
            'sialorrhea'
        },
        'treatment': '''En la mayoria de los casos solo con cuidados domesticos este puede tratar pero en caso de 
requerir medicamento lo mas comun es brindar antinflamatorios analgesicos o incluso puede llegarse a utilizar 
un broncodilator'''
    },
    'epoc': {
        'questions': [
            '¿Tiene problemas para respirar?',
            '¿Ha consumido tabaco?',
            '¿Tiene tiraje intercostal (movimiento de los musculos hacia adentro entre las costillas)?'
        ],
        'symptoms': {
            'shortness_breath',
            'tobacco',
            'intercostal_retreat'
        },
        'treatment': '''Se necesita que el paciente deje de fumar, y se le brinde al paciente la ayuda necesaria, 
en caso de requerir medicametnos los brocodilatadores, los esterioides inhalables o pudiendo utilizar 
inhaladores combinados y por ultimo y no menos importante el uso antibioticos'''
    },
    'bronquitis': {
        'questions': [
            '¿Tiene tos no productiva?',
            '¿Tiene fatiga?',
            '¿Tiene mucosidad transparente, blanca, gris, amarillenta?'
        ],
        'symptoms': {
            'non_productive_cough',
            'fatigue',
            'colored_mucus'
        },
        'treatment': '''Los remedios mas comunes son aquellos para el alivio de la tos se recomienda el uso de 
antiinflamatorios no esteroideos, por ejemplo ibuprofeno y analgesicos, para asi poder reducir el dolor como 
inflamacion'''
    },
    'neumonia': {
        'questions': [
            '¿Tiene fiebre?',
            '¿Tiene tos no productiva?',
            '¿Tiene estertores (ruidos anormales en la respiracion)?'
        ],
        'symptoms': {
            'fever',
            'non_productive_cough',
            'rattles'
        },
        'treatment': '''Los remedios mas comunes son aquellos para el alivio de la tos incluido los antifebriles y 
analgesicos para la fiebre y el malestar e.j. aspirina antibioticos para el treatment de la neumonia 
bacteriana'''
    },
    'asma': {
        'questions': [
            '¿Tiene problemas para respirar?',
            '¿Cuenta con antecedentes heredofamiliares?',
            '¿Se escucha un silbido cuando tose?'
        ],
        'symptoms': {
            'shortness_breath',
            'diseases_inheritance',
            'cough_whistle'
        },
        'treatment': '''En estas situaciones es recomendable la Administracion de B2 ademas acomparlo con el uso de 
inhibidores de leucotrienos incluir en el treatment corticosteroides inhalados u orales'''
    },
    'resfriado comun': {
        'questions': [
            '¿Tiene nariz congestionada?',
            '¿Tiene tos?',
            '¿Tiene estornudos?',
            '¿Tiene dolor de cabeza recurrente?',
            '¿Tiene fiebre?',
            '¿Tiene dolor de garganta al ingerir alimento?'
        ],
        'symptoms': {
            'stuffy_nose',
            'cough',
            'sneeze',
            'recurrent_headache',
            'fever',
            'sore_throat'
        },
        'treatment': '''La mayoría de los casos de resfriado común mejoran sin tratamiento, normalmente en un plazo 
de una semana a 10 días. Pero una tos puede persistir algunos días más. Lo mejor que puedes hacer es cuidarte 
mientras tu cuerpo se cura. Por ejemplo, bebe mucho líquido, humedece el aire, usa enjuagues nasales salinos 
y descansa adecuadamente.'''
    },
    'influenza': {
        'questions': [
            '¿Tiene dolor de garganta al ingerir alimento?',
            '¿Tiene dolor de cabeza recurrente?',
            '¿Tiene tos?',
            '¿Tiene fiebre?',
            '¿Tiene nariz congestionada?',
            '¿Tiene diarrea?'
        ],
        'symptoms': {
            'sore_throat',
            'recurrent_headache',
            'cough',
            'fever',
            'stuffy_nose',
            'diarrhoea'
        },
        'treatment': '''Hacer uso de Medicamento antiviral para treatment de la gripe junto con la administracion de 
inhibidores de la neuraminidasa para atacar el influenza es indispensable mantenerse hidratado'''
    },
    'faringitis': {
        'questions': [
            '¿Tiene nariz congestionada?',
            '¿Tiene tos?',
            '¿Tiene fiebre?',
            '¿Tiene dolor de garganta al ingerir alimento?'
        ],
        'symptoms': {
            'stuffy_nose',
            'cough',
            'fever',
            'sore_throat'
        },
        'treatment': '''Se recomienda el uso de Medicinas antiinflamatorias e.j. paracetamol 
ademas incluir la administracion de acetaminofen para el dolor y la fiebre'''
    },
    'laringitis': {
        'questions': [
            '¿Tiene tos con vomito?',
            '¿Tiene cosquilleo y aspereza en la garganta?',
            '¿Tiene perdida de voz?'
        ],
        'symptoms': {
            'cough_vomiting',
            'itchy_throat',
            'loss_voice'
        },
        'treatment': '''Uso de Corticosteroides para reducir la inflamacion de las cuerdas vocales debe ir acompanado 
de esteroides orales o inhalados contar con oxigeno suplementario en caso de emergencia'''
    },
    'epiglotitis': {
        'questions': [
            '¿Tiene alta produccion de saliva?',
            '¿Tiene inflamacion bucofaringea?',
            '¿Tiene problemas para respirar?'
        ],
        'symptoms': {
            'high_saliva',
            'bucopharyngeal_inflammation',
            'shortness_breath'
        },
        'treatment': '''Se recomienda el uso de antimicrobianos es indispensable contar con oxigeno suplementario 
de respaldo complementar con administracion de esteroides orales o inhalados'''
    }
}
