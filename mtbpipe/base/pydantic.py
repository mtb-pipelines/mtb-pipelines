from pydantic import BaseModel
from pydantic.generics import GenericModel


class AliasesBaseModel(BaseModel):
    class Config:
        allow_population_by_field_name = True


class AliasesBaseGenericModel(GenericModel):
    class Config:
        allow_population_by_field_name = True
