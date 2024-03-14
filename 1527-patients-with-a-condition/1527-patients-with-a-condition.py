import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients['conditions'] = patients['conditions'].apply(lambda x: x if 'DIAB1' in [r[:5] for r in x.split()] else 'Fail')    
    patients = patients.drop(patients[patients['conditions'] == 'Fail'].index)
    return patients