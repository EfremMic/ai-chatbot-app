import aiohttp
import asyncio
import os
import logging

class ChatBotService:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    async def get_response(self, user_input):
        try:
            if user_input:
                self.messages.append({"role": "user", "content": user_input})
                
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                        "https://api.openai.com/v1/chat/completions",
                        headers={"Authorization": f"Bearer {self.api_key}"},
                        json={"model": "gpt-3.5-turbo", "messages": self.messages}
                    ) as resp:
                        response_data = await resp.json()
                        assistant_reply = response_data['choices'][0]['message']['content']
                        self.messages.append({"role": "assistant", "content": assistant_reply})
                        return assistant_reply
        except Exception as e:
            logging.error(f"Error fetching response: {e}")
            return "Sorry, an error occurred."
