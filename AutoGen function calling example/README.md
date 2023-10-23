# Autogen Function Calling with LM Studio

[![Autogen Framework](https://img.shields.io/badge/Framework-Autogen-brightgreen)](https://github.com/microsoft/autogen)
[![LM Studio](https://img.shields.io/badge/Powered%20By-LM%20Studio-blue)](https://lmstudio.ai/)
[![OpenAI Version](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-red)](https://openai.com)

Autogen Function Calling with LM Studio is an example that demonstrates the integration of the Autogen multi-agent system framework by Microsoft with the capabilities of the LM Studio inference server and the power of OpenAI's GPT-3.5-turbo.

## Overview

[Autogen](https://github.com/microsoft/autogen) is a conversational multi-agent system framework developed by Microsoft that allows multiple agents to collaboratively handle user requests. 

[LM Studio](https://lmstudio.ai/) LM Studio offers a comprehensive suite for language model enthusiasts and developers. It empowers users to operate LLMs directly on their personal computers without the need for an internet connection. The platform provides an interactive in-app Chat UI, and if you're familiar with OpenAI, it offers a compatible local server to streamline your tasks. Plus, it integrates seamlessly with HuggingFace, allowing for easy model file downloads from their vast repositories. To stay updated with the latest in language model technology, LM Studio showcases new and noteworthy LLMs right on the app's home page. The perfect partner for open source LLM agents!

One of the unique features of this example is the use of [langchain tools](https://github.com/langchain-ai/langchain) that facilitate OpenAI function calls using the `gpt-3.5-turbo` model.

## Features

- **Multi-Agent Integration**: Seamless integration of multiple agents to handle complex user queries.
- **Open Source Model Testing**: Test different open-source models in an agent setting.
- **Function Call Compatibility**: The use of a specific agent class, `LMStudioAgent(AssistantAgent)`, ensures that messages are cleansed to make function call messages compatible with LM Studio.

## Getting Started

1. Clone this repository.
2. Install the necessary dependencies.
3. Configure your Autogen settings.
4. Setup your LM Studio inference server.
5. Ensure your OpenAI API keys are set up correctly for `gpt-3.5-turbo` access.
6. Ensure to have: GOOGLE_CSE_ID, GOOGLE_API_KEY and a custom search engine [LangChain Google](https://python.langchain.com/docs/integrations/tools/google_search)
7. Run main.py.

## Acknowledgements

- [Microsoft's Autogen Framework](https://github.com/microsoft/autogen)
- [LM Studio](https://lmstudio.ai/)
- [Langchain](https://github.com/langchain-ai/langchain)