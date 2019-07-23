import nexmo

NEXMO_API_KEY = "dd7eef91"
NEXMO_API_SECRET = "x6fFHG1jMABuXlEG"
TO_NUMBER = "639994521937"

client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

responseData = client.send_message(
    {
        "from": "CJ Salgo",
        "to": TO_NUMBER,
        "text": "A text message sent using the Nexmo SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")