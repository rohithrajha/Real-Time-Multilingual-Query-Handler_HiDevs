from flask import Blueprint, render_template, request, jsonify

from services.translator_service import (
    detect_language,
    translate_to_english
)

from services.ai_service import generate_response

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return render_template('index.html')

@api.route('/translate', methods=['POST'])
def translate():

    data = request.get_json()

    user_query = data.get("query")

    detected_lang = detect_language(user_query)

    english_text = translate_to_english(user_query)

    ai_response = generate_response(english_text)

    return jsonify({
        "original_query": user_query,
        "detected_language": detected_lang,
        "translated_text": english_text,
        "support_response": ai_response
    })