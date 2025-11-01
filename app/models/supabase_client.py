from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("Cliente Supabase inicializado com sucesso.")

except Exception as e:
    print("Erro de inicialização do Cliente Supabase:", {e})
    supabase = None

