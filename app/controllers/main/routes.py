from flask import Blueprint, render_template, flash, url_for, redirect
from app.models.supabase_client import supabase
from app.controllers.main.service import get_all_products

main_blueprint = Blueprint('main', __name__, url_prefix='/')

@main_blueprint.route('/')
def index():
    if not supabase:
        flash("Serviço indisponível no momento. Tente novamente mais tarde.", "danger")
        return render_template('main/index.html', products=[])
    
    supabase_response = get_all_products()

    if supabase_response and supabase_response.data:
        products_list = supabase_response.data
    else:
        products_list = []  
        flash("Nenhum produto encontrado.", "warning")   


    return render_template('main/index.html', products=products_list)
