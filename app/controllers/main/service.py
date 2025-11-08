from app.models.supabase_client import supabase

PRODUCTS_TABLE = "produtos"

def get_all_products():

    try:
        response = supabase.table(PRODUCTS_TABLE).select("*").execute()
        if response.error:
            print(f"Erro ao buscar produtos: {response.error.message}")
            return []
        return response.data
    except Exception as e:
        print(f"Exceção ao buscar produtos: {e}")
        return [] 