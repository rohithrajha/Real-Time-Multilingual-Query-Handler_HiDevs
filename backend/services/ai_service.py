def generate_response(query):

    responses = {
        "refund": "We are processing your refund request.",
        "payment": "Please verify your payment details.",
        "delivery": "Your order will arrive soon.",
        "hello": "Hello! How can we help you today?"
    }

    query = query.lower()

    for key in responses:
        if key in query:
            return responses[key]

    return "Thank you for contacting support. Our team will assist you shortly."