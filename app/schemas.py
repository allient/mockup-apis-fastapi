from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel

# Modelos de datos
from typing import List, Optional
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
