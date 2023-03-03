import openai as openai


class Api():

    api_key: str

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    async def get_response(self, message_text: str) -> str:
        openai.api_key = self.api_key
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message_text,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )

        return response["choices"][0]["text"]


