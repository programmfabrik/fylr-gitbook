---
description: >-
  Administrator reference for the ai-metadata plugin: connection settings and
  how to connect it to OpenAI, the Azure OpenAI Service, a LiteLLM proxy, or a
  local model served by Ollama.
---

# AI Metadata

{% hint style="info" %}
This plugin is a licensed module. It is only available after a valid license has been purchased — please contact Programmfabrik GmbH.
{% endhint %}

## About

The **ai-metadata plugin** (`ai-metadata`) sends an object's image to a Large Language Model (LLM) and writes the model's answers back into fields of the object. It communicates with any endpoint that implements the OpenAI [Chat Completions API](https://developers.openai.com/api/reference/chat-completions/overview), which means the same plugin can be pointed at:

* **OpenAI** directly,
* the **Azure OpenAI Service**,
* a **LiteLLM** proxy (one endpoint in front of many providers), or
* a **local / self-hosted** model served by **Ollama**.

This page is the **configuration reference for administrators**, with a focus on the connection settings and the four provider types. For the end-to-end workflow — creating prompts, building the metadata mapping, and running it during upload or as a background task — see the [ai-metadata tutorial](../../tutorials/ai-metadata-plugin.md).

## Requirements

For any endpoint, the model you connect to must satisfy three conditions, or the plugin cannot produce metadata:

1. **Chat Completions API** — the endpoint must implement the OpenAI Chat Completions API (`/chat/completions`).
2. **Vision** — the model must accept **image input**. The plugin converts the source image to a JPEG and sends it with the prompt.
3. **A structured answer** — the plugin asks the model to return its answer as a **forced function (tool) call** whose parameters are your configured fields. Models with native tool calling (OpenAI, Azure, and most cloud models) answer this way directly. For local OpenAI‑compatible models that reply in plain text instead, the plugin **retries with a JSON‑schema constraint** and recovers the answer from the message content. A model that returns **neither** a usable tool call nor parseable JSON is rejected with a clear error rather than writing unreliable data — the main thing to verify when using a local model (see the **Ollama** section below).

{% hint style="warning" %}
**Reachability:** The plugin runs in the fylr **execserver**, not in your browser. The endpoint URL you configure must be reachable **from the server**. For a local LiteLLM or Ollama this usually means the host's LAN address — `127.0.0.1` / `localhost` will only work if the service runs on the same host as the execserver.
{% endhint %}

The datamodel requirements (a file field as the image source and text/list/boolean/date fields as targets) and the installation steps are covered in the [tutorial](../../tutorials/ai-metadata-plugin.md). Root permissions are suggested for setup.

## Connection settings (General tab)

Open the **Plugin Manager**, select **ai-metadata**, and configure the connection in the **General** tab.

{% hint style="warning" %}
Only **one** LLM connection can be saved at a time.
{% endhint %}

| Setting | Description |
| --- | --- |
| **API Type** | `OPEN_AI` or `AZURE`. Use **`OPEN_AI`** for OpenAI itself **and** for any OpenAI‑compatible endpoint (LiteLLM, Ollama, …). Use **`AZURE`** only for the Azure OpenAI Service. Defaults to `OPEN_AI`. |
| **Base URL** | The root URL of the endpoint. **Leave empty for OpenAI** (it defaults to `https://api.openai.com/v1`). For any other OpenAI‑compatible endpoint, enter the URL **including the `/v1` path**. For Azure, enter the resource URL. The plugin appends `/chat/completions` itself. |
| **API Key** | Sent as the `Bearer` token. Required for OpenAI and Azure. Stored encrypted (the base config shows `*****`/`***` only when a key is stored). For local endpoints that do not check authentication, it can be left empty. |
| **API Version** | **Azure only.** The Azure REST API version (a date string), e.g. `2026-01-01-preview` or `2026-02-01`. |
| **Model (List)** | A drop‑down of common OpenAI model names. Used when **API Type = `OPEN_AI`** and no manual model is entered. |
| **Model (Deployment Name)** | A free‑text model name that **takes precedence** over the drop‑down. Use it for an Azure **deployment name**, a **LiteLLM** model name, an **Ollama** model tag, or any model not in the list. |
| **Used image size** | Longest edge of the image sent to the model: `small` (≈ 640 px, the default and sufficient for most cases), `medium` (≈ 1200 px), `big` (≈ 1600 px). Larger images add detail but cost more tokens. |
| **Instructions for the AI** | A system prompt describing the model's general style, role, or fixed rules — applied to every answer. Do **not** put the actual questions here. _Currently not applied with API Type `AZURE`._ |
| **Extended protocol** | Adds debug context to `FILE_METADATA` events. Useful while setting up a new endpoint. |

### Which model field is used

* If **Model (Deployment Name)** is filled, it is always used.
* Otherwise, with **API Type `OPEN_AI`**, the **Model (List)** drop‑down value is used.
* For Azure and for any non‑OpenAI model (LiteLLM target, Ollama tag), leave the drop‑down empty and put the model name in **Model (Deployment Name)**.

## Connecting to a provider

The four sections below give the exact settings per provider. The request always ends up at the endpoint's `…/chat/completions` path — shown for each so it can be allow‑listed in a firewall if needed.

### OpenAI

The default and simplest setup.

| Setting | Value |
| --- | --- |
| API Type | `OPEN_AI` |
| Base URL | _empty_ (defaults to `https://api.openai.com/v1`) |
| API Key | An OpenAI key (`sk-…`) from [platform.openai.com → API keys](https://platform.openai.com/settings/keys) |
| Model (List) | A vision‑capable model, e.g. `gpt-5.5`, `gpt-5.4-mini`, `gpt-4o` |

* **Endpoint:** `https://api.openai.com/v1/chat/completions`
* **Billing:** pay‑per‑token on your OpenAI account.

{% hint style="info" %}
Only models that support the **Chat Completions API** can be used. OpenAI "Pro"/reasoning‑only variants that are exposed solely through the Responses API are not compatible.
{% endhint %}

### Azure OpenAI Service

For a model deployed in your own Azure resource.

| Setting | Value |
| --- | --- |
| API Type | `AZURE` |
| Base URL | `https://<your-resource>.openai.azure.com` |
| API Version | Your deployment's Azure REST API version, e.g. `2026-01-01-preview` |
| Model (Deployment Name) | Your **deployment name** (not the underlying OpenAI model name) |
| API Key | A key from your Azure OpenAI resource (Azure Portal → _Keys and Endpoint_) |

* **Endpoint:** `https://<resource>.openai.azure.com/openai/deployments/<deployment>/chat/completions?api-version=<version>`
* The deployment must be backed by a **vision‑ and function‑calling‑capable** model (e.g. a GPT‑4o / GPT‑5‑class deployment).

{% hint style="info" %}
The **Instructions for the AI** (system prompt) are currently **not applied** when API Type is `AZURE`. Put any required style guidance into the individual prompts instead.
{% endhint %}

### LiteLLM (proxy)

[LiteLLM](https://docs.litellm.ai/) exposes many model providers behind a single OpenAI‑compatible endpoint. Use it to centralize keys, quotas and logging, to route to providers the plugin cannot reach directly, or to keep one stable URL while you change the backing model.

| Setting | Value |
| --- | --- |
| API Type | `OPEN_AI` |
| Base URL | `http://<litellm-host>:4000/v1` (your proxy address, including `/v1`) |
| API Key | The LiteLLM **virtual key** you configured (or empty if the proxy is open) |
| Model (Deployment Name) | The model name **as defined in your LiteLLM configuration** (e.g. `gpt-5.4`, or a provider‑prefixed name) |

* **Endpoint:** `http://<litellm-host>:4000/v1/chat/completions`
* The **target** model behind LiteLLM must still support **vision** and **function calling** — LiteLLM forwards the request, it does not add those capabilities to a model that lacks them.

### Ollama (local / self-hosted)

[Ollama](https://ollama.com/) runs open‑weight models on your own hardware and exposes an OpenAI‑compatible endpoint. No data leaves your infrastructure.

| Setting | Value |
| --- | --- |
| API Type | `OPEN_AI` |
| Base URL | `http://<ollama-host>:11434/v1` |
| API Key | _empty_ (Ollama ignores authentication) |
| Model (Deployment Name) | The local model **tag** you pulled, e.g. `mistral-small3.2:24b` |

* **Endpoint:** `http://<ollama-host>:11434/v1/chat/completions`
* Pull the model on the Ollama host first: `ollama pull <model>`.

{% hint style="warning" %}
**Choosing an Ollama model.** The model must be vision‑capable and return **reliable, complete structured output**. Models with native function (tool) calling are ideal; for vision models that reply in plain text, the plugin automatically retries with a JSON‑schema constraint and reads the answer from the content — but only a sufficiently capable model produces a complete result. **`mistral-small3.2:24b` works well**; many small or vision‑only models do not (they truncate, return malformed JSON, or fail to load on a given Ollama version). Always **test on representative images before production**. Larger models are more reliable but slower, so size your task timeouts accordingly.
{% endhint %}

{% hint style="info" %}
Make sure the Ollama host is reachable from the **execserver** (see [Requirements](#requirements)). In a Docker deployment, use the host's LAN address rather than `localhost`.
{% endhint %}

## Prompts, mappings and usage

Once the connection is configured, the prompts (the **fields** the model fills), customizable **variables**, the **metadata mapping** to an object type, and running the plugin during upload or as a background task are all described in the [ai-metadata tutorial](../../tutorials/ai-metadata-plugin.md). The tutorial also links a ready‑to‑upload example configuration you can adapt.
