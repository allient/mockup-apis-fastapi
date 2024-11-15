from fastapi import FastAPI, HTTPException, Query, Body
from fastapi.middleware.cors import CORSMiddleware

from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, Field

# Esquema de Metadata para la información adicional de cada asegurado
class Metadata(BaseModel):
    fee: str = Field(..., description="Costo de la póliza")
    plan: str = Field(..., description="Tipo de plan")
    nro_aseg: str = Field(..., description="Número del asegurado")
    maternity: str = Field(..., description="Cobertura de maternidad")
    id_persona: str = Field(..., description="Identificación única de la persona")
    nro_pariente: str = Field(..., description="Número del pariente relacionado")
    document_type: str = Field(..., description="Tipo de documento del asegurado")

# Esquema de InsuredUser para cada usuario asegurado
class InsuredUser(BaseModel):
    id: str = Field(..., description="Identificador único del asegurado")
    identity_card: str = Field(..., description="Número de cédula de identidad del asegurado")
    related_id_card: str = Field(..., description="Cédula de identidad de la persona relacionada")
    first_name: str = Field(..., description="Nombre del asegurado")
    last_name: str = Field(..., description="Apellido del asegurado")
    full_name: str = Field(..., description="Nombre completo del asegurado")
    certificate: int = Field(..., description="Número de certificado del asegurado")
    birthday: str = Field(..., description="Fecha de nacimiento del asegurado")
    start_date: str = Field(..., description="Fecha de inicio de la póliza")
    is_titular: bool = Field(..., description="Indica si es el titular de la póliza")
    category_plan: Optional[str] = Field(None, description="Categoría del plan")
    metadata: Metadata = Field(..., description="Metadatos adicionales del asegurado")
    relationship: str = Field(..., description="Relación del asegurado (TITULAR, CONYUGE, HIJO/A)")

# Esquema de Policy para representar la póliza completa
class Policy(BaseModel):
    policy_number: int = Field(..., description="Número de la póliza")
    branch_office_id: int = Field(..., description="ID de la sucursal")
    branch_office_name: str = Field(..., description="Nombre de la sucursal")
    contractor_name: str = Field(..., description="Nombre de la entidad contratante")
    contractor_ruc: str = Field(..., description="RUC de la entidad contratante")
    broker_name: str = Field(..., description="Nombre del corredor de seguros")
    broker_ruc: str = Field(..., description="RUC del corredor de seguros")
    lob: str = Field(..., description="Línea de negocio")
    category: str = Field(..., description="Categoría de la póliza")
    emission_date: str = Field(..., description="Fecha de emisión de la póliza")
    end_date: str = Field(..., description="Fecha de finalización de la póliza")
    insured_amount: int = Field(..., description="Monto asegurado")
    do_require_warranty: bool = Field(..., description="Indica si se requiere garantía")
    insured_users: List[InsuredUser] = Field(..., description="Lista de asegurados")

# Esquema de PolicyResponse para representar la respuesta completa de la API
class PolicyResponse(BaseModel):
    policies: List[Policy] = Field(..., description="Lista de pólizas")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


# Datos simulados
sample_data = PolicyResponse(
    policies=[
        Policy(
            policy_number=50005,
            branch_office_id=1,
            branch_office_name="Quito",
            contractor_name="Anonima Compañía de Seguros S.A.",
            contractor_ruc="1790475247001",
            broker_name="Nova Seguros",
            broker_ruc="1790475247001",
            lob="AM",
            category="Titular + Familia",
            emission_date="2007-11-01",
            end_date="2025-08-15",
            insured_amount=50000,
            do_require_warranty=True,
            insured_users=[
                InsuredUser(
                    id="57618c92-1aae-47b8-bed6-c46e7d03f731",
                    identity_card="1711111111",
                    related_id_card="1711111111",
                    first_name="PEDRO",
                    last_name="PEREZ LOPEZ",
                    full_name="PEDRO PEREZ LOPEZ",
                    certificate=284,
                    birthday="1985-03-08",
                    start_date="2011-09-12",
                    is_titular=True,
                    category_plan="Titular + Familia",
                    metadata=Metadata(
                        fee="401.670",
                        plan="EJECUTIVOS",
                        nro_aseg="106",
                        maternity="No aplica cobertura Maternidad",
                        id_persona="546494",
                        nro_pariente="0",
                        document_type="C"
                    ),
                    relationship="TITULAR",
                ),
                InsuredUser(
                    id="a1b2c3d4-5678-90ab-cdef-1234567890ab",
                    identity_card="1722222222",
                    related_id_card="1711111111",
                    first_name="MARIA",
                    last_name="GOMEZ MARTINEZ",
                    full_name="MARIA GOMEZ MARTINEZ",
                    certificate=285,
                    birthday="1986-04-15",
                    start_date="2011-09-12",
                    is_titular=False,
                    category_plan="Titular + Familia",
                    metadata=Metadata(
                        fee="0.000",
                        plan="EJECUTIVOS",
                        nro_aseg="107",
                        maternity="No aplica cobertura Maternidad",
                        id_persona="546495",
                        nro_pariente="1",
                        document_type="C"
                    ),
                    relationship="CONYUGE",
                ),
                InsuredUser(
                    id="b2c3d4e5-6789-01bc-def2-3456789012cd",
                    identity_card="1733333333",
                    related_id_card="1711111111",
                    first_name="JUAN",
                    last_name="PEREZ GOMEZ",
                    full_name="JUAN PEREZ GOMEZ",
                    certificate=286,
                    birthday="2012-05-10",
                    start_date="2012-05-10",
                    is_titular=False,
                    category_plan="Titular + Familia",
                    metadata=Metadata(
                        fee="0.000",
                        plan="EJECUTIVOS",
                        nro_aseg="108",
                        maternity="No aplica cobertura Maternidad",
                        id_persona="546496",
                        nro_pariente="2",
                        document_type="C"
                    ),
                    relationship="HIJO",
                )
            ]
        ),
        Policy(
            policy_number=60010,
            branch_office_id=2,
            branch_office_name="Guayaquil",
            contractor_name="Auto Seguro S.A.",
            contractor_ruc="1791056789001",
            broker_name="Autos Protegidos",
            broker_ruc="1791056789001",
            lob="AU",
            category="Vehículo Particular",
            emission_date="2019-06-15",
            end_date="2024-06-14",
            insured_amount=30000,
            do_require_warranty=False,
            insured_users=[
                InsuredUser(
                    id="c3d4e5f6-7890-12ab-34cd-567890abcdef",
                    identity_card="1744444444",
                    related_id_card="1744444444",
                    first_name="CARLOS",
                    last_name="MORALES DIAZ",
                    full_name="CARLOS MORALES DIAZ",
                    certificate=287,
                    birthday="1990-02-20",
                    start_date="2019-06-15",
                    is_titular=True,
                    category_plan="Vehículo Particular",
                    metadata=Metadata(
                        fee="200.000",
                        plan="COMPLETO",
                        nro_aseg="109",
                        maternity="No aplica",
                        id_persona="546497",
                        nro_pariente="0",
                        document_type="C"
                    ),
                    relationship="TITULAR",
                )
            ]
        )
    ],
)



@app.get(
    "/search_policies",
    response_model=PolicyResponse,
    description="""
    Este endpoint permite consultar información detallada de pólizas de seguro, filtrando por nombre completo del asegurado o número de cédula. Al proporcionar cualquiera de estos filtros, la API devuelve un conjunto de pólizas en las que el asegurado coincide con los criterios especificados.

    Detalles de la respuesta:

    La respuesta de la API es un objeto `PolicyResponse` que contiene una lista de pólizas, con los siguientes detalles:

    - **policy_number**: Número de la póliza.
    - **branch_office_id** y **branch_office_name**: ID y nombre de la oficina de sucursal correspondiente.
    - **contractor_name** y **contractor_ruc**: Nombre y RUC del contratante de la póliza.
    - **broker_name** y **broker_ruc**: Nombre y RUC del corredor de seguros.
    - **lob**: Línea de negocio, indicando el tipo de seguro.
    - **category**: Categoría de cobertura de la póliza (por ejemplo, "Titular + Familia").
    - **emission_date** y **end_date**: Fechas de emisión y finalización de la póliza.
    - **insured_amount**: Monto asegurado por la póliza.
    - **do_require_warranty**: Indicador de si se requiere garantía para la póliza.
    - **insured_users**: Lista de asegurados asociados a la póliza, cada uno con los siguientes atributos:
      - **identity_card** y **related_id_card**: Cédula del asegurado y del titular de la póliza.
      - **first_name**, **last_name**, y **full_name**: Nombres y apellidos del asegurado.
      - **certificate**: Número de certificado del asegurado.
      - **birthday** y **start_date**: Fecha de nacimiento y fecha de inicio de la cobertura para el asegurado.
      - **is_titular**: Indica si el asegurado es el titular de la póliza.
      - **category_plan**: Plan de cobertura.
      - **metadata**: Información adicional que incluye la cuota, el tipo de documento, la cobertura de maternidad, y otros datos relevantes.
      - **relationship**: Relación del asegurado con el titular (por ejemplo, "TITULAR", "CONYUGE", "HIJO").

    Parámetros de consulta:

    - **name** (opcional): Nombre completo del asegurado.
    - **identity_card** (opcional): Número de cédula del asegurado.

    Uso del endpoint:

    Este endpoint es útil para obtener información consolidada de pólizas de seguro y los asegurados vinculados, facilitando consultas específicas de acuerdo a los datos de identificación proporcionados.
    """
)
async def search_policies(
    name: Optional[str] = Query(
        None, 
        description="Nombre completo del asegurado",
        openapi_examples={
            "search_by_name": {
                "summary": "Buscar por nombre",
                "description": "Ejemplo de búsqueda de pólizas por nombre completo del asegurado.",
                "value": "PEDRO PEREZ LOPEZ"
            }
        }
    ),
    identity_card: Optional[str] = Query(
        None,
        description="Número de cédula del asegurado",
        openapi_examples={
            "search_by_identity_card": {
                "summary": "Buscar por cédula",
                "description": "Ejemplo de búsqueda de pólizas por número de cédula del asegurado.",
                "value": "1711111111"
            }
        }
    )
):
    return PolicyResponse(
        policies=sample_data.policies,
    )