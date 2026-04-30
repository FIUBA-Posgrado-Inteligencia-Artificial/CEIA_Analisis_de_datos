"""
Módulo mappers.py - SEDRONAR 2017 Dataset
==========================================

Mapeos de columnas y valores del dataset "Estudio nacional en población general 
sobre consumo de sustancias psicoactivas - 2017"

Funciones públicas:
    - map_columns(df): Renombra las columnas del dataframe
    - map_values(df, columns=None): Mapea los valores de columnas seleccionadas

Ejemplo de uso:
    import pandas as pd
    from mappers import map_columns, map_values
    
    df = pd.read_csv('base-estudio-hogares-2017.csv')
    df = map_columns(df)
    df = map_values(df)  # Mapea todas las disponibles
    # o
    df = map_values(df, columns=['genero_del_entrevistado', 'situacion_conyugal'])
"""

import pandas as pd
from typing import Optional, List

# ============================================================================
# MAPEO DE COLUMNAS: de código (p1, p2, etc.) a nombre descriptivo
# ============================================================================
COLUMNS_MAPPING = {
    # Datos generales
    'region': 'region',
    'provincia': 'provincia',
    'pondera_dem': 'ponderacion_demografica',
    'tothogar': 'total_personas_hogar_12_65',
    
    # Variables de identificación de vivienda, hogar y entrevistado
    'p1': 'tipo_de_vivienda',
    'p2': 'genero_del_entrevistado',
    'p3': 'nacionalidad',
    'p3.ot': 'nacionalidad_otros',
    'p4': 'edad',
    'p5': 'situacion_conyugal',
    'p6.1a': 'grupo_familiar_jefe_de_hogar',
    'p6.1b': 'grupo_familiar_conyuge',
    'p6.1c': 'grupo_familiar_hijo_hija',
    'p6.1d': 'grupo_familiar_madre_padre',
    'p6.1e': 'grupo_familiar_madrastra_padrastro',
    'p6.1f': 'grupo_familiar_hermano_hermana',
    'p6.1g': 'grupo_familiar_yerno_nuera',
    'p6.1h': 'grupo_familiar_nieto_nieta',
    'p6.1i': 'grupo_familiar_suegro_suegra',
    'p6.1j': 'grupo_familiar_otros_familiares',
    'p6.1k': 'grupo_familiar_otros_no_familiares',
    'p6.2a': 'posicion_en_hogar_jefe',
    'p6.2b': 'posicion_en_hogar_conyuge',
    'p6.2c': 'posicion_en_hogar_hijo_hija',
    'p6.2d': 'posicion_en_hogar_madre_padre',
    'p6.2e': 'posicion_en_hogar_madrastra_padrastro',
    'p6.2f': 'posicion_en_hogar_hermano_hermana',
    'p6.2g': 'posicion_en_hogar_yerno_nuera',
    'p6.2h': 'posicion_en_hogar_nieto_nieta',
    'p6.2i': 'posicion_en_hogar_suegro_suegra',
    'p6.2j': 'posicion_en_hogar_otros_familiares',
    'p6.2k': 'posicion_en_hogar_otros_no_familiares',
    'p7': 'cantidad_miembros_hogar',
    'p9': 'cantidad_habitaciones',
    'p10': 'hay_ninos_fuera_de_escuela_5_13',
    
    # Vivienda - Servicios
    'p11.a': 'acceso_red_electrica',
    'p11.b': 'acceso_red_agua_potable',
    'p11.c': 'acceso_red_cloacas',
    'p11.d': 'acceso_red_gas',
    'p12': 'tipo_bano',
    'p13': 'desague_inodoro',
    
    # Salud
    'p14': 'tipo_atencion_medica',
    'p15.1': 'asistencia_educativa_entrevistado',
    'p15.2': 'asistencia_educativa_jefe_hogar',
    'p16.1': 'nivel_educativo_entrevistado',
    'p16.2': 'nivel_educativo_jefe_hogar',
    'p29': 'estado_salud_general',
    'p30': 'enfermedad_reposo_ultimos_12_meses',
    'p31': 'visita_profesional_salud_mental',
    'p32': 'realiza_actividades_fisicas',
    'p33': 'lugar_actividades_fisicas',
    'p34': 'uso_medicamentos',
    
    # Consumo de tabaco
    'p35': 'ha_fumado_alguna_vez',
    'p36': 'edad_primer_cigarrillo',
    'p37': 'cuando_ultimo_cigarrillo',
    'p38': 'ha_fumado_ultimos_12_meses',
    'p39': 'ha_fumado_ultimos_30_dias',
    'p40': 'dias_fumado_ultimos_30_dias',
    'p41': 'cigarrillos_por_dia_ultimo_mes',
    'p42': 'ha_fumado_100_cigarrillos_vida',
    'p43': 'anos_fumado_diariamente',
    
    # Cigarrillos electrónicos
    'p44': 'ha_usado_cigarrillos_electronicos_vida',
    'p45': 'cuando_primer_cigarrillo_electronico',
    'p46': 'cuando_ultimo_cigarrillo_electronico',
    'p47': 'dias_usado_cigarrillos_electronicos_30dias',
    'p48': 'sabia_cigarrillo_electronico_contiene_nicotina',
    
    # Consumo de alcohol
    'p51': 'ha_consumido_alcohol_alguna_vez',
    'p52': 'edad_primer_consumo_alcohol',
    'p53': 'cuando_primer_consumo_alcohol',
    'p54': 'ha_consumido_alcohol_ultimos_12_meses',
    'p55': 'ha_consumido_alcohol_ultimos_30_dias',
    'p56': 'dias_consumo_alcohol_ultimos_30_dias',
    'p57': 'tragos_consumo_normal_ultimos_30_dias',
    'p58': 'tragos_maximo_dia_ultimos_30_dias',
    'p59': 'veces_5_o_mas_vasos_ultimos_30_dias',
    'p60': 'veces_emborrachado_ultimos_30_dias',
    'p62': 'frecuencia_consumo_alcohol',
    'p63': 'cantidad_tragos_dia_consumo_normal',
    'p64': 'frecuencia_5_tragos_un_solo_dia',
    'p65': 'frecuencia_incapaz_parar_beber',
    'p66': 'frecuencia_no_pudo_cumplir_obligaciones',
    'p67': 'frecuencia_necesito_beber_manana',
    'p68': 'frecuencia_remordimientos_culpa',
    'p69': 'frecuencia_no_recuerda_noche_anterior',
    'p70': 'consecuencias_fisicas_por_alcohol',
    'p71': 'preocupacion_familiar_consumo_alcohol',
    
    # Consumo de drogas
    'p76': 'amigos_familiares_consumen_drogas',
    'p77': 'alguna_vez_posibilidad_probar_droga',
    'p78': 'alguna_vez_curiosidad_probar_droga',
    'p79': 'probaria_droga_si_tuviera_ocasion',
    'p83': 'alguna_vez_ofrecieron_droga',
    
    # Consumo de marihuana
    'p119': 'cuando_primer_consumo_marihuana',
    'p120': 'ha_consumido_marihuana_ultimos_12_meses',
    'p121': 'frecuencia_consumo_marihuana',
    'p122': 'ha_consumido_marihuana_ultimos_30_dias',
    'p123': 'dejo_deberes_por_marihuana',
    'p124': 'puso_peligro_integridad_marihuana',
    'p125': 'hizo_algo_problematico_marihuana',
    'p126': 'problemas_familia_amigos_marihuana',
    'p127.1': 'deseo_irresistible_marihuana',
    'p127.2': 'consumio_marihuana_a_pesar_intencion',
    'p127.3': 'consumio_mayor_cantidad_planeado',
    'p127.4': 'uso_marihuana_eliminar_problemas',
    'p127.5': 'problemas_al_suspender_marihuana',
    'p127.6': 'necesita_mayor_cantidad_marihuana',
    'p127.7': 'menor_efecto_marihuana',
    'p127.8': 'dejo_actividades_por_marihuana',
    'p127.9': 'mas_tiempo_recuperarse_marihuana',
    'p127.10': 'continuo_marihuana_a_pesar_problemas',
    
    # Consumo de cocaína
    'p128': 'cuando_primer_consumo_cocaina',
    'p129': 'ha_consumido_cocaina_ultimos_12_meses',
    'p130': 'frecuencia_consumo_cocaina',
    'p131': 'ha_consumido_cocaina_ultimos_30_dias',
    'p132.1': 'deseo_irresistible_cocaina',
    'p132.2': 'consumio_cocaina_a_pesar_intencion',
    'p132.3': 'consumio_mayor_cantidad_cocaina_planeado',
    'p132.4': 'uso_cocaina_eliminar_problemas',
    'p132.5': 'problemas_al_suspender_cocaina',
    'p132.6': 'necesita_mayor_cantidad_cocaina',
    'p132.7': 'menor_efecto_cocaina',
    'p132.8': 'dejo_actividades_por_cocaina',
    'p132.9': 'mas_tiempo_recuperarse_cocaina',
    'p132.10': 'continuo_cocaina_a_pesar_problemas',
    
    # Demanda de tratamiento
    'p169': 'busco_ayuda_profesional_ultimos_12_meses',
    'p171': 'esta_o_estuvo_en_tratamiento',
    'p172': 'tipo_establecimiento_tratamiento',
    'p173': 'tipo_tratamiento_recibido',
    
    # Impacto
    'p158': 'accidente_laboral_alcohol_drogas',
    'p159': 'siniestro_vial_alcohol_drogas',
    'p162': 'baja_rendimiento_educativo_alcohol_drogas',
    
    # Ámbito laboral
    'p164': 'reglamento_uso_alcohol_drogas_trabajo',
    'p165': 'informacion_prevencion_trabajo',
    'p166': 'programa_ayuda_consumo_trabajo',
    'p167': 'reglamento_prohibicion_fumar_trabajo',
    'p168': 'cumplimiento_reglamento_fumar',
    
    # Drogas de síntesis y nuevas sustancias
    'p157.1.a': 'ha_consumido_ketamina_vida',
    'p157.2.a': 'ha_consumido_ketamina_12_meses',
    'p157.3.a': 'ha_consumido_ketamina_30_dias',
    'p157.4.a': 'edad_primer_consumo_ketamina',
    'p157.5.a': 'ketamina_conseguida_por_internet',
}

# ============================================================================
# MAPEO DE VALORES: código numérico a label descriptivo
# ============================================================================
VALUES_MAPPING = {
    'region': {
        1: 'Metropolitana',
        2: 'Pampeana',
        3: 'NOA',
        4: 'NEA',
        5: 'Cuyo',
        6: 'Patagonia'
    },
    'p1': {
        1: 'Vivienda adecuada',
        2: 'Vivienda precaria',
        88: 'Sin dato'
    },
    'p2': {
        1: 'Hombre',
        2: 'Mujer',
        3: 'Otro'
    },
    'p3': {
        1: 'Argentina',
        2: 'Boliviana',
        3: 'Peruana',
        4: 'Paraguaya',
        5: 'Chilena',
        6: 'Uruguaya',
        7: 'Otra',
        9: 'Sin dato'
    },
    'p5': {
        1: 'De novio/a',
        2: 'Conviviendo',
        3: 'Casado/a',
        4: 'Separado/a',
        5: 'Divorciado/a',
        6: 'Viudo/a',
        7: 'Soltero/a',
        9: 'Sin dato'
    },
    'p10': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p11.a': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p11.b': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p11.c': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p11.d': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p12': {
        1: 'Inodoro con botón o cadena y arrastre de agua',
        2: 'Inodoro sin botón o cadena y arrastre de agua',
        3: 'Letrina (sin arrastre de agua)',
        4: 'Este hogar no tiene instalación de baño',
        9: 'No sabe / No contesta'
    },
    'p13': {
        1: 'A red pública (cloacal)',
        2: 'A cámara séptica',
        3: 'Solamente a pozo ciego',
        4: 'Otro',
        9: 'No sabe / No contesta'
    },
    'p15.1': {
        1: 'Nunca asistió',
        2: 'No asiste, pero asistió',
        3: 'Asiste actualmente',
        9: 'Ns/Nc'
    },
    'p15.2': {
        1: 'Nunca asistió',
        2: 'No asiste, pero asistió',
        3: 'Asiste actualmente',
        9: 'Ns/Nc'
    },
    'p16.1': {
        1: 'Ninguno o sin instrucción',
        2: 'Primaria / EGB 1/ EGB 2/ incompleta',
        3: 'Primaria / EGB 1/ EGB 2/ completa',
        4: 'Secundaria / EGB 3 / Polimodal/ incompleta',
        5: 'Secundaria / EGB 3 / Polimodal/ completa',
        6: 'Intermedia o terciaria incompleta',
        7: 'Intermedia o terciaria completa',
        8: 'Superior o universitario incompleto',
        9: 'Superior o universitario completo',
        10: 'Posgrado',
        11: 'Educación especial',
        99: 'No sabe / No contesta'
    },
    'p16.2': {
        1: 'Ninguno o sin instrucción',
        2: 'Primaria / EGB 1/ EGB 2/ incompleta',
        3: 'Primaria / EGB 1/ EGB 2/ completa',
        4: 'Secundaria / EGB 3 / Polimodal/ incompleta',
        5: 'Secundaria / EGB 3 / Polimodal/ completa',
        6: 'Intermedia o terciaria incompleta',
        7: 'Intermedia o terciaria completa',
        8: 'Superior o universitario incompleto',
        9: 'Superior o universitario completo',
        10: 'Posgrado',
        11: 'Educación especial',
        99: 'No sabe / No contesta'
    },
    'p29': {
        1: 'Muy malo',
        2: 'Malo',
        3: 'Regular',
        4: 'Bueno',
        5: 'Muy bueno',
        9: 'No contesta'
    },
    'p30': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p31': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p32': {
        1: 'Algunas veces al mes',
        2: 'Una o dos veces por semana',
        3: 'Más de dos veces por semana',
        4: 'Todos los días',
        5: 'No realiza regularmente actividades físicas',
        9: 'No contesta'
    },
    'p35': {1: 'Si', 2: 'No'},
    'p38': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p39': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p42': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p44': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p45': {
        1: 'Durante los últimos 30 días',
        2: 'Hace más de 1 mes pero menos de 1 año',
        3: 'Hace más de 1 año',
        9: 'No contesta'
    },
    'p46': {
        1: 'Durante los últimos 30 días',
        2: 'Hace más de 1 mes pero menos de 1 año',
        3: 'Hace más de 1 año',
        9: 'No contesta'
    },
    'p48': {1: 'Si', 2: 'No', 8: 'No sabe', 9: 'No contesta'},
    'p51': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p53': {
        1: 'Durante los últimos 30 días',
        2: 'Hace más de 1 mes pero menos de 1 año',
        3: 'Hace más de 1 año',
        9: 'No contesta'
    },
    'p54': {1: 'Si', 2: 'No', 9: 'No Contesta'},
    'p55': {1: 'Si', 2: 'No', 9: 'No Contesta'},
    'p62': {
        1: 'Una vez al mes o menos',
        2: 'Dos a cuatro veces al mes',
        3: 'Dos o tres veces a la semana',
        4: 'Cuatro o más veces a la semana',
        9: 'Ns/Nc'
    },
    'p63': {
        1: 'Uno o dos tragos',
        2: 'Tres o cuatro tragos',
        3: 'Cinco o seis tragos',
        4: 'Siete a nueve tragos',
        5: 'Diez o más tragos',
        9: 'Ns/Nc'
    },
    'p64': {
        0: 'Nunca',
        1: 'Menos de una vez al mes',
        2: 'Mensualmente',
        3: 'Semanalmente',
        4: 'Todos los días o casi',
        9: 'Ns/Nc'
    },
    'p65': {
        0: 'Nunca',
        1: 'Menos de una vez al mes',
        2: 'Mensualmente',
        3: 'Semanalmente',
        4: 'Todos los días o casi',
        9: 'Ns/Nc'
    },
    'p66': {
        0: 'Nunca',
        1: 'Menos de una vez al mes',
        2: 'Mensualmente',
        3: 'Semanalmente',
        4: 'Todos los días o casi',
        9: 'Ns/Nc'
    },
    'p67': {
        0: 'Nunca',
        1: 'Menos de una vez al mes',
        2: 'Mensualmente',
        3: 'Semanalmente',
        4: 'Todos los días o casi',
        9: 'Ns/Nc'
    },
    'p68': {
        0: 'Nunca',
        1: 'Menos de una vez al mes',
        2: 'Mensualmente',
        3: 'Semanalmente',
        4: 'Todos los días o casi',
        9: 'Ns/Nc'
    },
    'p69': {
        0: 'Nunca',
        1: 'Menos de una vez al mes',
        2: 'Mensualmente',
        3: 'Semanalmente',
        4: 'Todos los días o casi',
        9: 'Ns/Nc'
    },
    'p70': {
        0: 'No',
        1: 'Sí, pero no en el curso del último año',
        2: 'Sí, en el último año',
        9: 'Ns/Nc'
    },
    'p71': {
        0: 'No',
        1: 'Sí, pero no en el curso del último año',
        2: 'Sí, en el último año',
        9: 'Ns/Nc'
    },
    'p76': {
        1: 'Ninguno',
        2: 'Uno',
        3: 'Dos o más',
        8: 'No sabe',
        9: 'No contesta'
    },
    'p77': {
        1: 'Ninguna vez',
        2: 'Una vez',
        3: 'Dos o más veces',
        9: 'No contesta'
    },
    'p78': {1: 'No', 2: 'Puede ser', 3: 'Si', 9: 'No contesta'},
    'p79': {1: 'No', 2: 'Puede ser', 3: 'Si', 9: 'No contesta'},
    'p83': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p119': {
        1: 'Durante los últimos 30 días',
        2: 'Hace más de un mes pero menos de un año',
        3: 'Hace más de un año',
        9: 'Ns/Nc'
    },
    'p120': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p121': {
        1: 'Una sola vez',
        2: 'Algunas veces durante los últimos 12 meses',
        3: 'Algunas veces mensualmente',
        4: 'Algunas veces semanalmente',
        5: 'Diariamente',
        9: 'No contesta'
    },
    'p122': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p123': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p124': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p125': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p126': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p127.1': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p127.2': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p127.3': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p127.4': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p127.5': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p127.6': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p127.7': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p127.8': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p127.9': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p127.10': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p128': {
        1: 'Durante los últimos 30 días',
        2: 'Hace más de un mes pero menos de un año',
        3: 'Hace más de un año',
        9: 'No contesta'
    },
    'p129': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p130': {
        1: 'Una sola vez',
        2: 'Algunas veces durante los últimos 12 meses',
        3: 'Algunas veces mensualmente',
        4: 'Algunas veces semanalmente',
        5: 'Diariamente',
        9: 'No contesta'
    },
    'p131': {1: 'Si', 2: 'No', 9: 'No contesta'},
    'p132.1': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p132.2': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p132.3': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p132.4': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p132.5': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p132.6': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p132.7': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p132.8': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p132.9': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p132.10': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p158': {
        1: 'Sí, por alcohol',
        2: 'Sí, por drogas',
        3: 'Sí, por alcohol y drogas',
        4: 'No estuvo relacionado al consumo',
        5: 'No tuve ningún accidente',
        9: 'No contesta'
    },
    'p159': {
        1: 'Sí, por alcohol',
        2: 'Sí, por drogas',
        3: 'Sí, por alcohol y drogas',
        4: 'No estuvo relacionado al consumo',
        5: 'No participé de ningún accidente',
        9: 'No contesta'
    },
    'p162': {
        1: 'Sí, por alcohol',
        2: 'Sí, por drogas',
        3: 'Sí, por alcohol y drogas',
        4: 'La baja de rendimiento no estuvo relacionada al consumo',
        5: 'No tuve ninguna baja de rendimiento',
        9: 'Ns/Nc'
    },
    'p164': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p165': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p166': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p167': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p168': {
        1: 'Si, en forma irrestricta',
        2: 'Sí, pero parcialmente',
        3: 'No se cumple',
        9: 'Ns/Nc'
    },
    'p169': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p171': {
        1: 'Sí, está actualmente',
        2: 'Sí, estuvo alguna vez pero no está actualmente',
        3: 'Nunca estuvo',
        9: 'Ns/Nc'
    },
    'p172': {
        1: 'Hospital general',
        2: 'Hospital Psiquiátrico o Clínica Psiquiátrica',
        3: 'Centro especializado',
        4: 'Comunidad terapéutica',
        5: 'Grupo de autoayuda',
        6: 'Otro',
        9: 'Ns/Nc'
    },
    'p173': {
        1: 'Ambulatorio',
        2: 'Semi residencial (hospital de día o de noche)',
        3: 'Residencial',
        4: 'Grupo de autoayuda',
        5: 'Otro',
        9: 'Ns/Nc'
    },
    'p157.1.a': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p157.2.a': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p157.3.a': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
    'p157.5.a': {1: 'Si', 2: 'No', 9: 'Ns/Nc'},
}


# ============================================================================
# FUNCIONES PÚBLICAS
# ============================================================================

def map_columns(df: pd.DataFrame, inplace: bool = False) -> pd.DataFrame:
    """
    Renombra las columnas del dataframe usando los mapeos definidos.
    
    Parámetros:
        df (pd.DataFrame): Dataframe con columnas a renombrar
        inplace (bool): Si True, modifica el dataframe original. Por defecto False.
    
    Retorna:
        pd.DataFrame: Dataframe con columnas renombradas
    
    Ejemplo:
        >>> df = pd.read_csv('data.csv')
        >>> df = map_columns(df)
        >>> df.columns  # Columnas renombradas
    """
    if not inplace:
        df = df.copy()
    
    # Crear mapeo solo con columnas que existen en el dataframe
    rename_map = {col: COLUMNS_MAPPING[col] 
                  for col in df.columns 
                  if col in COLUMNS_MAPPING}
    
    df.rename(columns=rename_map, inplace=True)
    return df


def map_values(df: pd.DataFrame, 
               columns: Optional[List[str]] = None, 
               inplace: bool = False) -> pd.DataFrame:
    """
    Mapea los valores numéricos de las columnas a labels descriptivos.
    
    Parámetros:
        df (pd.DataFrame): Dataframe con valores a mapear
        columns (Optional[List[str]]): Lista de nombres de columnas a mapear.
                                      Si None, mapea todas las disponibles.
        inplace (bool): Si True, modifica el dataframe original. Por defecto False.
    
    Retorna:
        pd.DataFrame: Dataframe con valores mapeados
    
    Ejemplo:
        >>> df = map_columns(df)
        >>> df = map_values(df)  # Mapea todas
        >>> # o
        >>> df = map_values(df, columns=['genero_del_entrevistado', 'estado_salud_general'])
    """
    if not inplace:
        df = df.copy()
    
    # Si no se especifican columnas, mapear todas las que se encuentren
    if columns is None:
        columns_to_map = []
        for col in df.columns:
            # Buscar en el mapeo por código original (p1, p2, etc.)
            for code, name in COLUMNS_MAPPING.items():
                if name == col and code in VALUES_MAPPING:
                    columns_to_map.append((col, code))
                    break
    else:
        columns_to_map = []
        for col in columns:
            # Buscar en el mapeo por código original (p1, p2, etc.)
            for code, name in COLUMNS_MAPPING.items():
                if (name == col or code == col) and code in VALUES_MAPPING:
                    columns_to_map.append((col if name == col else code, code))
                    break
    
    # Mapear valores
    for col_name, code in columns_to_map:
        if col_name in df.columns:
            df[col_name] = df[col_name].map(VALUES_MAPPING[code])
    
    return df


# ============================================================================
# INFORMACIÓN PÚBLICA
# ============================================================================

def get_columns_mapping() -> dict:
    """Retorna el diccionario completo de mapeo de columnas."""
    return COLUMNS_MAPPING.copy()


def get_values_mapping() -> dict:
    """Retorna el diccionario completo de mapeo de valores."""
    return VALUES_MAPPING.copy()


def get_mapped_columns() -> List[str]:
    """Retorna lista de columnas mapeadas."""
    return list(COLUMNS_MAPPING.keys())


def get_columns_with_values_mapping() -> List[str]:
    """Retorna lista de columnas que tienen mapeo de valores."""
    return list(VALUES_MAPPING.keys())


if __name__ == '__main__':
    print("=" * 80)
    print("EJEMPLO DE USO DEL MÓDULO MAPPERS")
    print("=" * 80)
    
    print(f"\n✓ Columnas mapeadas: {len(COLUMNS_MAPPING)}")
    print(f"✓ Variables con mapeo de valores: {len(VALUES_MAPPING)}")
    
    print("\n" + "=" * 80)
    print("EJEMPLO 1: Mapear columnas")
    print("=" * 80)
    print("""
    import pandas as pd
    from mappers import map_columns
    
    df = pd.read_csv('base-estudio-hogares-2017.csv')
    df = map_columns(df)
    print(df.columns)
    """)
    
    print("\n" + "=" * 80)
    print("EJEMPLO 2: Mapear valores (todas las disponibles)")
    print("=" * 80)
    print("""
    from mappers import map_columns, map_values
    
    df = pd.read_csv('base-estudio-hogares-2017.csv')
    df = map_columns(df)
    df = map_values(df)
    """)
    
    print("\n" + "=" * 80)
    print("EJEMPLO 3: Mapear valores específicos")
    print("=" * 80)
    print("""
    df = map_values(df, columns=['genero_del_entrevistado', 
                                   'situacion_conyugal',
                                   'estado_salud_general'])
    """)
    
    print("\n" + "=" * 80)
    print("EJEMPLO 4: Obtener información de mapeos")
    print("=" * 80)
    print("""
    from mappers import get_columns_with_values_mapping
    
    columns_with_mappings = get_columns_with_values_mapping()
    print(f"Columnas con mapeo de valores: {columns_with_mappings}")
    """)
    
    print("\n" + "=" * 80)
