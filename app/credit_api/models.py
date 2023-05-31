from pydantic import BaseModel, constr, conint
from typing import Union

class CreditInfo(BaseModel):
    APPLICATION_SUBMISSION_TYPE: constr(regex='^(Carga|Web)$')
    QUANT_ADDITIONAL_CARDS: Union[conint(ge=1, le=2), None]
    POSTAL_ADDRESS_TYPE: conint(ge=1, le=2)
    SEX: constr(regex='^(M|N|F)$')
    MARITAL_STATUS: conint(ge=1, le=7)
    QUANT_DEPENDANTS: int
    EDUCATION_LEVEL: conint(ge=1, le=5)
    NACIONALITY: conint(ge=0, le=2)
    FLAG_RESIDENCIAL_PHONE: constr(regex='^(Y|N)$')
    RESIDENCE_TYPE: Union[int, None]
    MONTHS_IN_RESIDENCE: int
    FLAG_EMAIL: conint(ge=0, le=1)
    PERSONAL_MONTHLY_INCOME: int
    OTHER_INCOMES: int
    FLAG_VISA: int
    FLAG_MASTERCARD: conint(ge=0, le=1)
    FLAG_DINERS: conint(ge=0, le=1)
    FLAG_AMERICAN_EXPRESS: conint(ge=0, le=1)
    FLAG_OTHER_CARDS: Union[conint(ge=0, le=1), None]
    QUANT_BANKING_ACCOUNTS: int
    QUANT_SPECIAL_BANKING_ACCOUNTS: int
    PERSONAL_ASSETS_VALUE: int
    QUANT_CARS: int
    COMPANY: constr(regex='^(Y|N)$')
    FLAG_PROFESSIONAL_PHONE: constr(regex='^(Y|N)$')
    PROFESSIONAL_PHONE_AREA_CODE: int
    MONTHS_IN_THE_JOB: int
    PROFESSION_CODE: int
    OCCUPATION_TYPE: int
    FLAG_HOME_ADDRESS_DOCUMENT: conint(ge=0, le=1)
    FLAG_RG: conint(ge=0, le=1)
    FLAG_CPF: conint(ge=0, le=1)
    FLAG_INCOME_PROOF: conint(ge=0, le=1)
    PRODUCT: conint(ge=1, le=7)
    AGE: int
    TARGET_LABEL_BAD: conint(ge=0, le=1)
