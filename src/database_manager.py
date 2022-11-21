import pandas as pd

from datetime import datetime

FILEPATH: str = './src/data/banco.xlsx'
SHEET_NAME: str = "Pedidos"

def create_database() -> None:
    df: pd.DataFrame = pd.DataFrame([], columns=["Data", "Status", "Nome", "Pedido"])
    df.to_excel(FILEPATH, sheet_name=SHEET_NAME, index=False)

def load_database() -> pd.DataFrame:
    return pd.read_excel(FILEPATH, sheet_name=SHEET_NAME)

def save_database(df: pd.DataFrame) -> None:
    df.to_excel(FILEPATH, sheet_name=SHEET_NAME, index=False)

def insert_order(nome: str, pedido: str) -> str:    

    df: pd.DataFrame = load_database()
    df.loc[len(df.index)] = [datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "Iniciado", nome,  pedido]    
    save_database(df)
    
    return "Realizado"

def update_order(index: int, status: str) -> str:
    
    df: pd.DataFrame = load_database()
    if index > len(df.index): return "Cancelado: Index fora de alcance"
    
    index -= index    
    df.loc[index, "Status"] = status
    save_database(df)
    
    return "Pedido atualizado"        

def read_order() -> list:
    df: pd.DataFrame = load_database()

    return df.values.tolist()
