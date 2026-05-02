"""
Módulo mappers_dispositivos_2022.py - SEDRONAR 2022 Dataset
============================================================

Mapeos de columnas y valores del dataset "Primer Relevamiento Nacional de
Dispositivos de Cuidado, Acompañamiento y Asistencia en Salud Mental
y Consumos Problemáticos 2022"

Funciones públicas:
    - map_columns(df): Renombra las columnas del dataframe
    - map_values(df, columns=None): Mapea los valores de columnas seleccionadas

Ejemplo de uso:
    import pandas as pd
    from mappers_dispositivos_2022 import map_columns, map_values

    df = pd.read_csv('base-primer-relev-dispositivos.csv')
    df = map_columns(df)
    df = map_values(df)  # Mapea todas las disponibles
    # o
    df = map_values(df, columns=['tipo_atencion_ambulatoria', 'hay_historia_clinica'])
"""

import pandas as pd
from typing import Optional, List

# ============================================================================
# MAPEO DE COLUMNAS
# ============================================================================
COLUMNS_MAPPING = {
    "respondent_id": "id_dispositivo",
    "q0011": "provincia",
    "q0021": "atiende_en",
    "q0022": "dependencia_institucional",
    "q0023_0001": "financiamiento_beca_sedronar",
    "q0023_0002": "financiamiento_otras_becas",
    "q0023_0003": "financiamiento_directo",
    "q0023_0004": "financiamiento_donaciones",
    "q0023_0005": "financiamiento_obras_sociales",
    "q0023_0006": "financiamiento_prepaga",
    "q0023_0007": "financiamiento_pago_particular",
    "q0023_0008": "financiamiento_programa_incluir_salud",
    "q0023_0009": "financiamiento_otros",
    "q0024_0001": "modalidad_ambulatoria",
    "q0024_0002": "modalidad_internacion",
    "q0024_0003": "modalidad_comunitaria",
    "q0025": "tipo_dispositivo",
    "q0026": "confecciona_historia_clinica",
    "q0027": "formato_historia_clinica",
    "q0028": "plan_tratamiento_en_historia_clinica",
    "q0029": "firma_consentimiento_informado",
    "q0030": "consentimiento_en_historia_clinica",
    "q0031_0001": "atiende_mujer",
    "q0031_0002": "atiende_mujer_trans_travesti",
    "q0031_0003": "atiende_varon",
    "q0031_0004": "atiende_varon_trans_masculinidad",
    "q0031_0005": "atiende_no_binario",
    "q0031_0006": "atiende_otra_identidad",
    "q0031_0007": "atiende_genero_ignorado",
    "q0031_0008": "atiende_otros_genero",
    "q0032_0001": "atiende_ninos_hasta_12",
    "q0032_0002": "atiende_adolescentes_13_17",
    "q0032_0003": "atiende_jovenes_18_29",
    "q0032_0004": "atiende_adultos_30_59",
    "q0032_0005": "atiende_adultos_60_mas",
    "q0033_0001": "atiende_mujeres_embarazadas_hijos",
    "q0033_0002": "atiende_sin_documentacion",
    "q0033_0003": "atiende_ninos_situacion_calle",
    "q0033_0004": "atiende_adultos_situacion_calle",
    "q0033_0005": "atiende_pueblos_originarios",
    "q0033_0006": "atiende_discapacidad_fisica",
    "q0033_0007": "atiende_discapacidad_mental",
    "q0033_0008": "atiende_enfermedades_infectocontagiosas",
    "q0033_0009": "atiende_derivados_causas_penales",
    "q0033_0010": "atiende_mujeres_violencia_genero",
    "q0033_0011": "atiende_ninos_violencia",
    "q0033_0012": "atiende_derivados_causas_asistenciales",
    "q0033_0013": "atiende_otra_poblacion",
    "q0034_0001": "cobertura_otra",
    "q0034_0002": "cobertura_obra_social_pami",
    "q0034_0003": "cobertura_programa_incluir_salud",
    "q0034_0004": "cobertura_publica_exclusiva",
    "q0034_0005": "cobertura_otra_especificada",
    "q0035_0001": "primer_contacto_orientacion_contencion",
    "q0035_0002": "primer_contacto_teleasistencia",
    "q0035_0003": "primer_contacto_consejeria",
    "q0035_0004": "primer_contacto_entrevista_interdisciplinaria",
    "q0035_0005": "primer_contacto_admision_sm_cp",
    "q0035_0006": "primer_contacto_evaluacion_sm",
    "q0035_0007": "primer_contacto_evaluacion_cp",
    "q0035_0008": "primer_contacto_evaluacion_patologias_medicas",
    "q0035_0009": "primer_contacto_otras_prestaciones",
    "q0036_0001": "prestacion_acciones_preventivas",
    "q0036_0002": "prestacion_admision",
    "q0036_0003": "prestacion_diagnostico_evaluacion",
    "q0036_0004": "prestacion_consejeria_sm_individual",
    "q0036_0005": "prestacion_consejeria_sm_vincular",
    "q0036_0006": "prestacion_interconsulta",
    "q0036_0007": "prestacion_entrevista_interdisciplinaria",
    "q0036_0008": "prestacion_atencion_clinica",
    "q0036_0009": "prestacion_terapia_ocupacional",
    "q0036_0010": "prestacion_estimulacion_temprana",
    "q0036_0011": "prestacion_cuidados_enfermeria_sm",
    "q0036_0012": "prestacion_acompanamiento_terapeutico",
    "q0036_0013": "prestacion_intervencion_sociocomunitaria",
    "q0036_0014": "prestacion_rehabilitacion_psicosocial",
    "q0036_0015": "prestacion_apoyo_inclusion_psicosocial",
    "q0036_0016": "prestacion_continuidad_cuidados_domiciliaria",
    "q0036_0017": "prestacion_derivacion_coordinacion",
    "q0036_0018": "prestacion_supervision",
    "q0036_0019": "prestacion_capacitacion_comunidad",
    "q0036_0020": "prestacion_atencion_domiciliaria",
    "q0036_0021": "prestacion_seguimiento_domiciliario",
    "q0036_0022": "prestacion_seguimiento_post_alta",
    "q0036_0023": "prestacion_intervenciones_grupales",
    "q0036_0024": "prestacion_capacitacion_supervision_equipos",
    "q0036_0025": "prestacion_actividades_recreativas",
    "q0036_0026": "prestacion_psicoterapia_individual",
    "q0036_0027": "prestacion_psicoterapia_grupal",
    "q0036_0028": "prestacion_telesaludmental",
    "q0036_0029": "prestacion_grupos_autoayuda",
    "q0036_0030": "prestacion_tratamiento_psicofarmacologico",
    "q0036_0031": "prestacion_tratamiento_sustitucion_farmacologica",
    "q0036_0032": "prestacion_guardia_emergencia",
    "q0036_0033": "prestacion_hospital_dia_jornada_simple",
    "q0036_0034": "prestacion_hospital_dia_jornada_completa",
    "q0036_0035": "prestacion_hospital_noche",
    "q0036_0036": "prestacion_desintoxicacion_estabilizacion",
    "q0036_0037": "prestacion_orientacion_padres_familiares",
    "q0036_0038": "prestacion_internacion_domiciliaria",
    "q0036_0039": "prestacion_dispensario_farmacologico",
    "q0036_0040": "prestacion_otras",
    "q0037_0001": "inclusion_asesoria_legal",
    "q0037_0002": "inclusion_acompanamiento_tramites",
    "q0037_0003": "inclusion_educacion_formal",
    "q0037_0004": "inclusion_programas_educativos",
    "q0037_0005": "inclusion_capacitacion_laboral",
    "q0037_0006": "inclusion_asesoria_emprendimiento",
    "q0037_0007": "inclusion_orientacion_vocacional",
    "q0037_0008": "inclusion_comedor_comunitario",
    "q0037_0009": "inclusion_servicios_aseo",
    "q0037_0010": "inclusion_otras_prestaciones_basicas",
    "q0037_0011": "inclusion_otras_prestaciones",
    "q0038_0001_0001": "cantidad_medico_clinico",
    "q0038_0002_0001": "cantidad_medico_psiquiatra",
    "q0038_0003_0001": "cantidad_medico_psiquiatra_infanto_juvenil",
    "q0038_0004_0001": "cantidad_medico_toxicologico",
    "q0038_0005_0001": "cantidad_medico_infectologo",
    "q0038_0006_0001": "cantidad_psicologo",
    "q0038_0007_0001": "cantidad_trabajador_social",
    "q0038_0008_0001": "cantidad_enfermero",
    "q0038_0009_0001": "cantidad_terapista_ocupacional",
    "q0038_0010_0001": "cantidad_nutricionista",
    "q0038_0011_0001": "cantidad_psicopedagogo",
    "q0038_0012_0001": "cantidad_operador_socioterapeutico",
    "q0038_0013_0001": "cantidad_operador_calle",
    "q0039_0001_0001": "cantidad_docente",
    "q0039_0002_0001": "cantidad_tallerista",
    "q0039_0003_0001": "cantidad_personal_administrativo",
    "q0039_0004_0001": "cantidad_personal_seguridad",
    "q0039_0005_0001": "cantidad_personal_mantenimiento",
    "q0039_0006_0001": "cantidad_personal_cocina",
    "q0039_0007_0001": "cantidad_personal_maestranza",
    "q0039_0008_0001": "cantidad_personal_apoyo_religioso",
    "q0039_0009_0001": "cantidad_pasante_grado",
    "q0039_0010_0001": "cantidad_pasante_posgrado",
    "q0039_0011_0001": "cantidad_acompanante_terapeutico",
    "q0040": "cuenta_internacion",
    "q0041": "numero_camas_disponibles",
    "q0043": "registro_tiempo_internacion",
    "q0047": "contempla_tiempo_minimo_internacion",
    "q0048": "servicio_internet_internados",
    "q0049": "telefonos_celulares_contacto",
    "q0060_0001": "acceso_consulta_espontanea",
    "q0060_0002": "acceso_derivacion_centros_salud",
    "q0060_0003": "acceso_derivacion_sistema_judicial",
    "q0060_0004": "acceso_derivacion_desarrollo_social",
    "q0060_0005": "acceso_derivacion_organizaciones_sociales",
    "q0060_0006": "acceso_otra_forma",
    "q0061_0001": "canal_turnos_telefonico",
    "q0061_0002": "canal_turnos_online",
    "q0061_0003": "canal_turnos_presencial",
    "q0061_0004": "canal_turnos_otro",
    "q0062": "participa_red_dispositivos",
    "q0063_0001": "red_hospital_especializado_sm_cp",
    "q0063_0002": "red_clinica_especializada_sm_cp",
    "q0063_0003": "red_hospital_general",
    "q0063_0004": "red_clinica_polivalente",
    "q0063_0005": "red_consultorio_externo",
    "q0063_0006": "red_centro_sm_cp",
    "q0063_0007": "red_vivienda_transitoria_apoyos",
    "q0063_0008": "red_vivienda_dependencia",
    "q0063_0009": "red_comunidad_terapeutica_sin_guardia",
    "q0063_0010": "red_comunidad_terapeutica_con_guardia",
    "q0063_0011": "red_dispositivos_territoriales_comunitarios",
    "q0063_0012": "red_centro_rehabilitacion_penitenciarias",
    "q0063_0013": "red_centro_rehabilitacion_establecimientos_religiosos",
    "q0063_0014": "red_caac",
    "q0063_0015": "red_ccc",
    "q0063_0016": "red_centro_dia",
    "q0063_0017": "red_centro_noche",
    "q0063_0018": "red_caps",
    "q0063_0019": "red_cic",
    "q0063_0020": "red_ccsmcp",
    "q0063_0021": "red_cpa",
    "q0063_0022": "red_ursmcp",
    "q0063_0023": "red_extension_territorial",
    "q0063_0024": "red_eric",
    "q0063_0025": "red_otro_tipo",
    "q0064": "realiza_derivaciones",
    "q0065": "derivaciones_segun_protocolo",
    "q0066_0001": "motivo_derivacion_complejidad_superior",
    "q0066_0002": "motivo_derivacion_complejidad_inferior",
    "q0066_0003": "motivo_derivacion_abordaje_especifico",
    "q0066_0004": "motivo_derivacion_no_adapta_normas",
    "q0066_0005": "motivo_derivacion_falta_espacio",
    "q0066_0006": "motivo_derivacion_falta_rrhh",
    "q0066_0007": "motivo_derivacion_decision_persona",
    "q0066_0008": "motivo_derivacion_otros",
    "q0067_0001": "efectividad_mecanismo_referencia_contraref",
    "q0071_0001": "estrategia_covid_medidas_higiene_bioseguridad",
    "q0071_0002": "estrategia_covid_atencion_telefonica",
    "q0071_0003": "estrategia_covid_atencion_videollamadas",
    "q0071_0004": "estrategia_covid_atencion_chat_online",
    "q0071_0005": "estrategia_covid_seguimiento_remoto",
    "q0071_0006": "estrategia_covid_visitas_domiciliarias",
    "q0071_0007": "estrategia_covid_entregas_viandas",
    "q0071_0008": "estrategia_covid_talleres_preventivos",
    "q0071_0009": "estrategia_covid_materiales_impresos",
    "q0071_0010": "estrategia_covid_readaptacion_roles",
    "q0071_0011": "estrategia_covid_articulacion_instituciones",
    "q0071_0012": "estrategia_covid_contencion_equipos",
    "q0071_0013": "estrategia_covid_otras_estrategias",
    "q0072_0001": "dificultad_covid_no_surgieron",
    "q0072_0002": "dificultad_covid_reduccion_equipo_profesional",
    "q0072_0003": "dificultad_covid_reduccion_equipo_apoyo",
    "q0072_0004": "dificultad_covid_falta_recursos_informaticos",
    "q0072_0005": "dificultad_covid_falta_conectividad",
    "q0072_0006": "dificultad_covid_dificultad_visitas_domiciliarias",
    "q0072_0007": "dificultad_covid_falta_elementos_proteccion",
    "q0072_0008": "dificultad_covid_falta_recursos_higiene_seguridad",
    "q0072_0009": "dificultad_covid_dificultad_readaptar_prestaciones",
    "q0072_0010": "dificultad_covid_dificultad_adaptar_espacio_fisico",
    "q0072_0011": "dificultad_covid_incremento_demanda_guardias",
    "q0072_0012": "dificultad_covid_incremento_demanda_cp",
    "q0072_0013": "dificultad_covid_incremento_violencia_genero",
    "q0072_0014": "dificultad_covid_incremento_violencia_callejera",
    "q0072_0015": "dificultad_covid_reduccion_servicio_alimentario",
    "q0072_0016": "dificultad_covid_costo_internet",
    "q0072_0017": "dificultad_covid_insuficiencia_conectividad",
    "q0072_0018": "dificultad_covid_otras_dificultades",
    "q0073": "encuentra_barreras_ley_sm",
    "q0075_0001": "articula_consejo_consultivo_honorario",
    "q0075_0002": "articula_organo_revision_ley_nacional",
    "q0075_0003": "articula_unidad_letrados",
    "q0075_0004": "articula_organizaciones_usuarios",
    "q0075_0005": "articula_organo_revision_provincial",
    "q0075_0006": "articula_secretaria_ddhh_nacion",
    "q0075_0007": "articula_no_requirieron",
    "q0075_0008": "articula_otro",
}

# ============================================================================
# MAPEO DE VALORES
# ============================================================================
VALUES_MAPPING = {
    "confecciona_historia_clinica": {
        "Sí, en todos los casos": "Si_en_todos_los_casos",
        "En algunos casos": "En_algunos_casos",
        "No": "No",
    },
    "formato_historia_clinica": {
        "En papel": "En_papel",
        "Digital (informatizado en red con otros efectores)": "Digital_informatizado",
        "Digital (informatizado sin conexión en red)": "Digital_sin_conexion",
    },
    "plan_tratamiento_en_historia_clinica": {
        "Sí": "Si",
        "No": "No",
    },
    "firma_consentimiento_informado": {
        "Sí, en todos los casos": "Si_en_todos_los_casos",
        "En algunos casos": "En_algunos_casos",
        "No": "No",
    },
    "consentimiento_en_historia_clinica": {
        "Sí": "Si",
        "No": "No",
    },
    "cuenta_internacion": {
        "No": "No",
        "Sí": "Si",
    },
    "registro_tiempo_internacion": {
        "Sí": "Si",
        "No": "No",
    },
    "contempla_tiempo_minimo_internacion": {
        "Sí": "Si",
        "No": "No",
    },
    "servicio_internet_internados": {
        "Sí": "Si",
        "No": "No",
    },
    "telefonos_celulares_contacto": {
        "Sí": "Si",
        "No": "No",
    },
    "participa_red_dispositivos": {
        "No": "No",
        "Sí": "Si",
    },
    "realiza_derivaciones": {
        "No": "No",
        "Sí": "Si",
    },
    "derivaciones_segun_protocolo": {
        "No": "No",
        "Sí": "Si",
    },
    "encuentra_barreras_ley_sm": {
        "Sí, en la red de articulación con otros actores /dispositivos.": "Si_en_red",
        "Sí, en las prácticas cotidianas de atención.": "Si_en_practicas",
        "No, considero que la ley se garantiza plenamente.": "No_ley_garantizada",
        "No articulamos, porque no hubo situaciones que lo requieran.": "No_situaciones_requeridas",
    },
    "efectividad_mecanismo_referencia_contraref": {
        "Muy efectivo": "Muy_efectivo",
        "Efectivo": "Efectivo",
        "Poco efectivo": "Poco_efectivo",
        "Inefectivo": "Inefectivo",
    },
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
        >>> df = pd.read_csv('base-primer-relev-dispositivos.csv')
        >>> df = map_columns(df)
        >>> df.columns  # Columnas renombradas
    """
    if not inplace:
        df = df.copy()

    # Crear mapeo solo con columnas que existen en el dataframe
    rename_map = {
        col: COLUMNS_MAPPING[col] for col in df.columns if col in COLUMNS_MAPPING
    }

    df.rename(columns=rename_map, inplace=True)
    return df


def map_values(
    df: pd.DataFrame, columns: Optional[List[str]] = None, inplace: bool = False
) -> pd.DataFrame:
    """
    Mapea los valores de las columnas a labels descriptivos.

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
        >>> df = map_values(df, columns=['tipo_dispositivo', 'confecciona_historia_clinica'])
    """
    if not inplace:
        df = df.copy()

    # Si no se especifican columnas, mapear todas las que se encuentren
    if columns is None:
        columns_to_map = [col for col in df.columns if col in VALUES_MAPPING]
    else:
        columns_to_map = [
            col for col in columns if col in df.columns and col in VALUES_MAPPING
        ]

    # Mapear valores
    for col in columns_to_map:
        df[col] = df[col].map(VALUES_MAPPING[col])

    return df


# ============================================================================
# FUNCIONES INFORMATIVAS
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


if __name__ == "__main__":
    print("=" * 80)
    print("MÓDULO MAPPERS - DATASET DISPOSITIVOS 2022")
    print("=" * 80)

    print(f"\n✓ Columnas mapeadas: {len(COLUMNS_MAPPING)}")
    print(f"✓ Variables con mapeo de valores: {len(VALUES_MAPPING)}")

    print("\n" + "=" * 80)
    print("EJEMPLO DE USO:")
    print("=" * 80)
    print("""
    import pandas as pd
    from mappers_dispositivos_2022 import map_columns, map_values
    
    # Cargar datos
    df = pd.read_csv('base-primer-relev-dispositivos.csv')
    
    # Renombrar columnas
    df = map_columns(df)
    
    # Mapear valores (todas las disponibles)
    df = map_values(df)
    
    # O mapear solo algunas columnas específicas
    df = map_values(df, columns=['confecciona_historia_clinica', 'tipo_dispositivo'])
    """)

    print("\n" + "=" * 80)
