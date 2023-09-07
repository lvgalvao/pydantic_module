from pydantic import BaseModel, EmailStr, Field, field_validator
from enum import Enum

# É aqui que criamos nossa Classe com nossas regras de validações
# O ideal que essa Classe seja pensada para garantir que os registros,
# sejam acidionados corretamente no nosso banco de dados, vamos criar 4 regras:

class SalesRecord(BaseModel):
    # 1) EmailStr garante que o email seja válido (checa se tem @ e etc)
    sales_email: EmailStr
    # 2) O fornecedor deve ser um dos valores da lista
    supply: Enum("SUPPLIER_A", "SUPPLIER_B")
    # 3) Valor da venda deve ser entre 10000 e 40000
    sale_value: float = Field(..., ge=10000, le=40000)
    # 4) Field_validator personalizado
    sales_name: str

    # Decorator para adicionar valições personalizadas
    @field_validator('sales_name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('O nome deve conter ao menos um espaço')
        return v.title()

# Agora é a nossa pipeline de dados
import pandas as pd

records = [['Alice Brown', 'alice@email.com', 'SUPPLIER_A', 15000],  # Valido
           ['Charlie', 'charlie@email.com', 'SUPPLIER_B', 30000],    # Nome invalido
           ['David Lee', 'davidemail', 'SUPPLIER_A', 15000],         # Email invalido
           ['Frank Black', 'frank@email.com', 'UNKNOWN_SUPPLIER', 25000],  # Supplier invalido
           ['Grace White', 'grace@email.com', 'SUPPLIER_A', -50000]]  # Valor invalido

# Criando um mapa de colunas para converter listas em dicionários
column_map = ['sales_name', 'sales_email', 'supply', 'sale_value']

validated_records = []

# Tente validar cada registro
for record in records:
    record_dict = dict(zip(column_map, record))
    try:
        validated_record = SalesRecord(**record_dict)
        validated_records.append(validated_record.model_dump())
    except ValueError as e:
        print(f"Erro ao validar o registro: {record}")

# Converta os registros validados para um DataFrame e salve em um arquivo CSV
df = pd.DataFrame(validated_records)
df.to_csv('sales_records.csv', index=False)
