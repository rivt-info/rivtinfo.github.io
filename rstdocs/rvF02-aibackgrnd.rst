**F.2** AI Background
=====================


**[1]** Foundational Models
--------------------------------------------------------------------- 

Foundational models include private and open source services.

**Private**

1. GPT-5 (OpenAI-US): OpenAI's flagship generation of reasoning and
coding-optimized models, highly regarded for their mastery of software
engineering benchmarks.

2. Claude (Anthropic-US): Renowned for their nuanced writing, sophisticated
handling of complex logic, and deep integration with tool-use platforms like the
Model Context Protocol.

3. Gemini 3 (Google-US) / Ultra: Google’s natively multimodal foundation models,
designed for massive context windows, seamless deep integration across the
Android/Google Workspace ecosystem, and heavy reasoning

4. Llama 4 (Meta-US): Meta’s flagship open-weight entry, heavily favored for
building custom local AI workflows and broad general knowledge tasks.

5. Stable Diffusion (Stability AI-US): Open foundation models specialized in latent
text-to-image and generative video editing.

6. Devstral (Mistral AI-EU): European-developed models celebrated for their
efficiency, speed, and suitability for local development.


**Open Source**

7. DeepSeek (China): Open-weight with exceptional mathematical reasoning, efficient
mixture-of-experts (MoE) architectures, and coding capabilities.

8. Qwen (Alibaba-China): A family of highly capable generalist and vision-language
(VL) models developed by Alibaba, scoring highly across academic and reasoning
benchmarks.

9. Mistral (EU and China): Created by former DeepMind and Meta scientists, Mistral
offers highly capable, free-to-download models under the Apache 2.0 license.

10. Meta Llama (Deep Seek and Meta): highly customizable, and available in various
sizes.

11. IBM Granite (US): IBM has open-sourced its enterprise-focused Granite family of
language, code, and time-series foundation models under the permissive Apache
2.0 license.

12. Allen Institute for AI (AI2 - US): Based in Seattle, AI2 regularly open-sources its
OLMo family of language models, providing full transparency into the training
data and architecture.

13. Databricks DBRX (US): Released by the San Francisco-based data and AI company
Databricks, DBRX is a powerful open-weights model utilizing a mixture-of-experts
(MoE) architecture.

------------------------------------

**[2]** Agents and UIs
--------------------------------------------------------------------- 

**Private User Interfaces, Agents and Extensions**

1. ChatGPT: The flagship interface for OpenAI GPT series (featuring GPT-4o and
reasoning models), offering prompt chat, document analysis, voice interaction,
and workspace canvases. Access it on OpenAI ChatGPT. ws. Access it on Anthropic
Claude.

2. Gemini: Conversational AI interface, directly integrated with the
Google Workspace ecosystem for exporting documents and generating real-time
data. Access it on Google Gemini

3. Google AI Studio: A streamlined, web-based prototyping environment for
developers to test prompts, adjust model parameters (temperature, token limits),
and directly generate API code. Visit Google AI Studio.

4. Claude: Anthropic platform regarded for its advanced reasoning,
large context windows, and specific interface features like "Projects" and
artifact generation for coding and design.

5. Google Gemini: The premier UI for real-time information and deep integration
with the Google Workspace ecosystem.

6. Perplexity AI: A specialized, citation-heavy UI designed specifically for
research, deep web-diving, and source transparency

7. Cursor: It functions as a rebuilt VS Code fork designed for auto-completion,
deep multi-file project context, and seamless "in-place" code edits.

8. Windsurf: Cognition desktop IDE. It stands out for its strong agentic
workflow, autonomously planning, editing, and executing tests with reviewable
diffs directly in your project.

9. GitHub Copilot: The most widely adopted tool. Best for teams seeking enterprise
integration and real-time inline suggestions directly within their existing
development tools.

10. Claude Code: Anthropic CLI-first agent. It excels at deep
reasoning, reading your entire codebase, planning changes, and iterating on
failures using natural language.Aider: A powerful command-line pair programmer.
It is highly favored by terminal power users who want manual context control and
transparent, incremental git commits.

11. Cline: A highly transparent, open-source VS Code extension and CLI. It allows
developers to offload multi-file edits and terminal commands securely with
in-editor diff approvals.

12. Codex: can perform tasks for you such as writing features, answering questions
about your codebase, fixing bugs, and proposing pull requests for review.


**Open Source User Interfaces, Agents and Extensions**

13. Open WebUI
Open WebUI is a self-hosted, extensible AI interface that supports Ollama,
OpenAI API, and various LLM runners. It features granular permissions,
responsive design, full Markdown/LaTeX support, hands-free voice/video calls,
native Python function calling, persistent artifact storage, local RAG
integration, web search, image generation/editing, and enterprise
authentication. It’s ideal for privacy-focused deployments, local model
experimentation, and enterprise use cases.

GitHub Link: https://github.com/open-webui/open-webui

14. LobeChat
LobeChat is a modern, open-source ChatGPT-like UI with support for speech
synthesis, multi-modal input, a plugin system, agent marketplace, and one-click
deployment. It supports MCP (Model Context Protocol), smart internet search,
chain of thought visualization, branching conversations, artifacts, file
upload/knowledge base, multi-model providers, local LLMs (Ollama), visual
recognition, TTS/STT, text-to-image generation, and custom themes. LobeChat
excels in extensibility, user experience, and rapid deployment for both
individuals and teams.

GitHub Link: https://github.com/lobehub/lobe-chat

15. Text Generation Web UI
Text Generation Web UI is a popular open-source platform for running and
interacting with local LLMs. It supports a wide range of models, offers a clean
interface, and includes advanced features like model presets, plugins, and
community-driven enhancements. It’s favored by developers and researchers for
local experimentation and model benchmarking.

GitHub Link: https://github.com/oobabooga/text-generation-webui

16. Chatbot UI
Chatbot UI is a Next.js-based, open-source chat interface that supports OpenAI
and Azure APIs. It’s designed for easy self-hosting, customization, and rapid
prototyping, making it a go-to choice for developers building custom chatbot
experiences. GitHub Link: https://github.com/mckaywrigley/chatbot-ui

17. LibreChat
LibreChat is an open-source, multi-provider chat UI with support for MCP, rich
UI features, and a focus on privacy. It’s designed for users who want a
versatile, self-hosted chat experience with advanced agent orchestration and
workflow management.

GitHub Link: https://github.com/danny-avila/LibreChat

18. AnythingLLM
AnythingLLM is a multi-model, MCP-compatible UI that supports local and cloud
deployment. It’s known for its flexibility, privacy, and ease of use, making it
suitable for both personal and enterprise AI workflows.

GitHub Link: https://github.com/Mintplex-Labs/anything-llm

19. Flowise
Flowise is a visual builder for LangChain-based LLM applications. It enables
users to create complex agent workflows and pipelines with drag-and-drop ease,
ideal for developers and non-developers alike.


GitHub Link: https://github.com/FlowiseAI/Flowise

20. LangFlow
LangFlow is a visual pipeline builder for LangChain, allowing users to design,
prototype, and deploy LLM-powered workflows. It’s perfect for rapid
experimentation and building complex agent logic.

GitHub Link: https://github.com/logspace-ai/langflow

21. assistant-ui
assistant-ui is a React/TypeScript-based component library for building custom
LLM chat interfaces. It’s highly modular and customizable, making it a favorite
for developers building tailored agent experiences.

GitHub Link: https://github.com/assistant-ui/assistant-ui

22. Streamlit
Streamlit is a Python-based framework for quickly building and deploying
interactive web apps, including LLM chat interfaces. It’s ideal for rapid
prototyping, data science, and AI experimentation.

GitHub Link: https://github.com/streamlit/streamlit

23. Hugging Chat: An open-source, community-driven interface that hosts multiple
foundational models (such as Mistral and Llama) in a single chat environment.
Try it on Hugging Chat.

Github Link: https://github.com/huggingface/chat-ui





