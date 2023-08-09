from . import common


class QueryChat:
    def __init__(
        self,
        service="openai",
        prompt="You are a helpful AI assistant. The following is a conversation with a student.",
        messages=None,
        model="gpt-3.5-turbo",
        temperature=0.3,
        max_tokens=400,
    ):
        if service not in common.ADAPTORS:
            raise RuntimeError(f"Unkown service name")
        if (adaptor := common.ADAPTORS[service]) and not adaptor.initialized:
            raise RuntimeError(
                f"ChatProxy is not initialized properly. call chatproxy.init(services=['service', ...]) first"
            )
        self.service_adaptor = adaptor
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.prompt = prompt
        self.messages = messages

    def vector(self, query):
        return self.service_adaptor.get_vector(query)

    def clear(self):
        self.messages = []

    def send(self, message=None):
        _messages = self.messages or []

        if self.prompt:
            _messages = [{"role": "system", "content": self.prompt}] + _messages

        if message:
            _messages.append({"role": "user", "content": message})

        response = self.service_adaptor.send(
            model=self.model,
            messages=_messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return response
