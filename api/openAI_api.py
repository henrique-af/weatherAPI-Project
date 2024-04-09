import openai

def load_api_key_from_env(file_path=".env"):
    with open(file_path, "r") as file:
        for line in file:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                if key.strip() == "API_KEY_OPENIA":
                    return value.strip()
    return None

def get_weather_5_days(data):
    api_key = load_api_key_from_env()

    openai.api_key = api_key
    data_str = str(data)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        response_format={"type": "json"},
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant, send a json output",
            },
            {
                "role": "user",
                "content": f"Based on {data_str}, create a preview on how the weather will be in these location, the output json will be used in a graphviz graph, so populate that json with values that can easily adapt to that output",
            },
        ],
    )
    if response and response.choices:
        return response.choices[0].message.json()
    else:
        return None
