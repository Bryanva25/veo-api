# 🎬 Veo 3 API - Google Veo API | Veo 3.1 | Veo 3 Fast | Google DeepMind Video AI | Text-to-Video API

[English](#english) | [中文](#中文)

> Access **Google Veo 3** (Veo3, Veo 3.1, Veo 3 Fast, Veo-3, Google DeepMind Veo) text-to-video and image-to-video generation through a simple API. Up to 50% discount! The cheapest Veo 3 API available.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![API Status](https://img.shields.io/badge/API-Online-green.svg)](https://shanhaiapi.com/zh/)
[![Documentation](https://img.shields.io/badge/Docs-Available-blue.svg)](https://docs.mountsea.ai/api-reference/veo/introduction)
[![PyPI](https://img.shields.io/badge/PyPI-mountsea--veo-blue.svg)](https://pypi.org/project/mountsea-veo/)
[![npm](https://img.shields.io/badge/npm-mountsea--veo-red.svg)](https://www.npmjs.com/package/mountsea-veo)

---

<a name="english"></a>

## 🤔 What is Veo 3 API?

**Veo 3** (also known as Veo3, Veo 3.1, Google Veo, Veo-3, Google DeepMind Veo) is Google's latest AI video generation model. This project provides the **cheapest and easiest access** to Veo 3 API through [Mountsea AI](https://shanhaiapi.com/zh/).

### Supported Models

| Model | Also Known As | Description | Speed | Quality |
|-------|--------------|-------------|-------|---------|
| **Veo 3** | Veo3, Veo-3, Google Veo 3 | Latest flagship model | Standard | Highest |
| **Veo 3 Fast** | Veo3-Fast, Veo-3-Fast | Speed-optimized model | Fast | High |
| **Veo 3.1** | Veo3.1 | Next-gen update | Standard | Highest |

## 🔥 Special Offer

**Enjoy Veo 3 and Veo 3 Fast up to 50% discount on credits!** [Get Started →](https://shanhaiapi.com/zh/)

## ✨ Features

- 🎥 **Text-to-Video** – Generate high-quality videos from text prompts
- 🖼️ **Image-to-Video** – Transform images into stunning animations
- ⚡ **Veo 3 Fast** – Quick generation for rapid prototyping
- 🎬 **Veo 3 Pro** – Premium quality for production use
- 💰 **50% OFF** – Best pricing for Veo API access
- 🐍 **Python SDK** – `pip install mountsea-veo`
- 📦 **Node.js SDK** – `npm install mountsea-veo`

## 🚀 Quick Start

### Install SDK

```bash
# Python
pip install mountsea-veo

# Node.js
npm install mountsea-veo
```

### Get Your API Key

1. Visit [Mountsea AI Platform](https://shanhaiapi.com/zh/)
2. Sign up and get your API key
3. Start generating videos with Veo!

### Python SDK Example

```python
from mountsea_veo import VeoClient

client = VeoClient("your-api-key")
task = client.generate("A sunset over the ocean, cinematic 4K", model="veo-3")
result = client.wait(task["taskId"])
print(result["videoUrl"])
```

### Node.js SDK Example

```javascript
const { VeoClient } = require('mountsea-veo');

const client = new VeoClient('your-api-key');
const task = await client.generate('A sunset over the ocean, 4K', { model: 'veo-3' });
const result = await client.wait(task.taskId);
console.log(result.videoUrl);
```

### Python Example (requests)

```python
import requests
import time

API_KEY = "your-api-key"
BASE_URL = "https://api.mountsea.ai"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Text-to-Video with Veo 3
response = requests.post(
    f"{BASE_URL}/veo/generate",
    headers=headers,
    json={
        "prompt": "A majestic eagle soaring over snow-capped mountains at sunrise, cinematic 4K",
        "model": "veo-3",
        "duration": 5,
        "resolution": "1080p"
    }
)

task = response.json()
task_id = task['taskId']
print(f"Task ID: {task_id}")

# Poll for results
while True:
    status = requests.get(
        f"{BASE_URL}/veo/task",
        headers=headers,
        params={"taskId": task_id}
    ).json()
    
    if status['status'] == 'completed':
        print(f"Video URL: {status['videoUrl']}")
        break
    elif status['status'] == 'failed':
        print(f"Error: {status['error']}")
        break
    
    print(f"Status: {status['status']}...")
    time.sleep(10)
```

### Veo 3 Fast (Quick Generation)

```python
# Use Veo 3 Fast for rapid prototyping
response = requests.post(
    f"{BASE_URL}/veo/generate",
    headers=headers,
    json={
        "prompt": "A cat playing with a ball of yarn, cute and playful",
        "model": "veo-3-fast",
        "duration": 3
    }
)
```

### Image-to-Video with Veo

```python
# Animate an image using Veo
response = requests.post(
    f"{BASE_URL}/veo/generate",
    headers=headers,
    json={
        "prompt": "The flowers gently sway in the breeze with petals falling",
        "imageUrl": "https://example.com/flowers.jpg",
        "model": "veo-3",
        "duration": 5
    }
)
```

### JavaScript / Node.js

```javascript
const axios = require('axios');

const API_KEY = process.env.MOUNTSEA_API_KEY || 'your-api-key';
const BASE_URL = 'https://api.mountsea.ai';

async function generateVeoVideo(prompt, options = {}) {
  const response = await axios.post(`${BASE_URL}/veo/generate`, {
    prompt,
    model: options.model || 'veo-3',
    duration: options.duration || 5,
    resolution: options.resolution || '1080p',
    ...options
  }, {
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json'
    }
  });

  return response.data;
}

// Usage
(async () => {
  const task = await generateVeoVideo(
    'A futuristic city with flying cars and neon lights at night',
    { model: 'veo-3', duration: 5 }
  );
  console.log('Task ID:', task.taskId);
})();
```

### cURL

```bash
# Generate with Veo 3
curl -X POST https://api.mountsea.ai/veo/generate \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A beautiful aurora borealis over a frozen lake, 4K cinematic",
    "model": "veo-3",
    "duration": 5,
    "resolution": "1080p"
  }'

# Generate with Veo 3 Fast
curl -X POST https://api.mountsea.ai/veo/generate \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A puppy running on the beach",
    "model": "veo-3-fast",
    "duration": 3
  }'
```

## 📖 Available Models

| Model | Description | Speed | Quality |
|-------|-------------|-------|---------|
| `veo-3` | Latest flagship model | Standard | Highest |
| `veo-3-fast` | Optimized for speed | Fast | High |

## 📖 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/veo/generate` | POST | Generate video from text or image |
| `/veo/task` | GET | Get task status and results |

## 🆚 Why Choose Mountsea Veo API?

| Feature | Mountsea AI | Official Vertex AI | Other Providers |
|---------|-------------|-------------------|-----------------|
| **Pricing** | ✅ Up to 50% OFF | ❌ Full price | ❌ Varies |
| **Setup** | ✅ API key only | ❌ GCP project + billing | ❌ Complex |
| **Python SDK** | ✅ `pip install mountsea-veo` | ❌ Heavy SDK | ❌ No SDK |
| **Node.js SDK** | ✅ `npm install mountsea-veo` | ❌ No dedicated SDK | ❌ No SDK |
| **Veo 3 Fast** | ✅ Supported | ❌ Limited | ❌ No |
| **Image-to-Video** | ✅ Supported | ✅ Supported | ❌ Varies |
| **Pay-as-you-go** | ✅ Credit system | ❌ Complex billing | ❌ Subscription |

## ❓ FAQ

### Is Veo 3 API free?
Mountsea AI offers a free trial with initial credits when you sign up. [Get started for free →](https://shanhaiapi.com/zh/)

### Veo 3 vs Sora 2 – which is better?
Both are top-tier AI video generators. Veo 3 excels in visual quality and realism, while Sora 2 is strong in creative motion. We support both! See [Sora API](https://github.com/mountsea-ai/sora-api).

### What video resolutions does Veo 3 support?
Veo 3 supports up to 1080p resolution with various aspect ratios (16:9, 9:16, 1:1).

### How long can generated videos be?
Currently Veo 3 supports videos up to 8 seconds. Veo 3 Fast supports up to 5 seconds for quick generation.

### Can I use Veo API for commercial projects?
Yes! All generated videos through Mountsea AI can be used for commercial purposes.

### Do you support image-to-video?
Yes! You can animate static images using Veo 3 by passing an `imageUrl` parameter along with your prompt.

## 💰 Pricing

🔥 **Special: Up to 50% OFF on Veo 3 credits!**

| Package | Credits | Price |
|---------|---------|-------|
| Starter | 10,000 | ¥100 |
| Basic | 50,000 | ¥500 |
| Pro | 200,000 | ¥2,000 |
| Business | 500,000 | ¥4,500 (10% OFF) |
| Enterprise | 1,000,000 | ¥8,000 (20% OFF) |

👉 [View Full Pricing](https://shanhaiapi.com/zh/)

## 📚 Documentation

- 📘 [Veo API Documentation](https://docs.mountsea.ai/api-reference/veo/introduction)
- 🏠 [Mountsea AI Platform](https://shanhaiapi.com/zh/)
- 🐍 [PyPI - mountsea-veo](https://pypi.org/project/mountsea-veo/)
- 📦 [npm - mountsea-veo](https://www.npmjs.com/package/mountsea-veo)

## 🔗 Related Projects

- [Sora API](https://github.com/mountsea-ai/sora-api) - OpenAI Sora 2 Video Generation API
- [Nano Banana API](https://github.com/mountsea-ai/nano-banana-api) - AI Image Generation API (Gemini)
- [Suno API](https://github.com/mountsea-ai/suno-api) - AI Music Generation API
- [Gemini API](https://github.com/mountsea-ai/gemini-api) - Google Gemini Chat API
- [Producer API](https://github.com/mountsea-ai/producer-api) - AI Music Production API
- [OpenAI Compatible API](https://github.com/mountsea-ai/openai-compatible-api) - OpenAI-compatible Chat API

---

<a name="中文"></a>

## 🇨🇳 中文文档

# 🎬 Veo 3 API - 谷歌 Veo API | Veo 3.1 | Veo 3 Fast | AI 视频生成 | 文本转视频

> 通过简单的 API 访问 **Google Veo 3**（Veo3、Veo 3.1、Veo 3 Fast、Veo-3、Google DeepMind Veo）视频生成能力。最便宜的 Veo 3 API，积分最高享 50% 折扣！

## 🔥 特惠活动

**Veo 3 和 Veo 3 Fast 积分最高享 50% 折扣！** [立即开始 →](https://shanhaiapi.com/zh/)

## ✨ 功能特点

- 🎥 **文本生成视频** – 从文字描述生成高质量视频
- 🖼️ **图片生成视频** – 将静态图片转化为精彩动画
- ⚡ **Veo 3 Fast** – 快速生成，适合原型制作
- 🎬 **Veo 3 Pro** – 高级质量，适合正式制作
- 💰 **5折优惠** – Veo API 最优价格
- 🐍 **Python SDK** – `pip install mountsea-veo`
- 📦 **Node.js SDK** – `npm install mountsea-veo`

## 🚀 快速开始

### 安装 SDK

```bash
# Python
pip install mountsea-veo

# Node.js
npm install mountsea-veo
```

### 获取 API 密钥

1. 访问 [Mountsea AI 平台](https://shanhaiapi.com/zh/)
2. 注册账号并获取 API 密钥
3. 开始用 Veo 生成视频！

### Python 示例

```python
import requests

API_KEY = "your-api-key"
BASE_URL = "https://api.mountsea.ai"

# 使用 Veo 3 生成视频
response = requests.post(
    f"{BASE_URL}/veo/generate",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "prompt": "雄鹰在日出时分翱翔于雪山之上，电影级4K画质",
        "model": "veo-3",
        "duration": 5,
        "resolution": "1080p"
    }
)

task = response.json()
print(f"任务 ID: {task['taskId']}")
```

## 🆚 为什么选择 Mountsea Veo API？

| 特性 | Mountsea AI | 官方 Vertex AI | 其他第三方 |
|------|-------------|---------------|-----------|
| **价格** | ✅ 低至5折 | ❌ 原价 | ❌ 不一定 |
| **接入方式** | ✅ 只需 API Key | ❌ 需配置 GCP 项目 | ❌ 复杂 |
| **Python SDK** | ✅ `pip install mountsea-veo` | ❌ 臃肿 SDK | ❌ 无 |
| **Node.js SDK** | ✅ `npm install mountsea-veo` | ❌ 无专用 SDK | ❌ 无 |

## ❓ 常见问题

### Veo 3 API 免费吗？
注册即送试用积分！[立即免费体验 →](https://shanhaiapi.com/zh/)

### Veo 3 和 Sora 2 哪个好？
两者都是顶级 AI 视频生成模型。Veo 3 在画面质量和真实感方面更强，Sora 2 在创意运动方面有优势。我们两个都支持！详见 [Sora API](https://github.com/mountsea-ai/sora-api)。

### 支持哪些视频分辨率？
Veo 3 支持最高 1080p，支持 16:9、9:16、1:1 等多种比例。

### 能用于商业项目吗？
可以！通过 Mountsea AI 生成的所有视频均可用于商业用途。

## 📚 文档

- 📘 [Veo API 完整文档](https://docs.mountsea.ai/api-reference/veo/introduction)
- 🏠 [Mountsea AI 官网](https://shanhaiapi.com/zh/)

## 🔗 相关项目

- [Sora API](https://github.com/mountsea-ai/sora-api) - OpenAI Sora 2 视频生成 API
- [Nano Banana API](https://github.com/mountsea-ai/nano-banana-api) - AI 图片生成 API (Gemini)
- [Suno API](https://github.com/mountsea-ai/suno-api) - AI 音乐生成 API
- [Gemini API](https://github.com/mountsea-ai/gemini-api) - Google Gemini 对话 API
- [Producer API](https://github.com/mountsea-ai/producer-api) - AI 音乐制作 API
- [OpenAI Compatible API](https://github.com/mountsea-ai/openai-compatible-api) - OpenAI 兼容对话 API

## ⭐ Star History

如果这个项目对你有帮助，请给我们一个 Star ⭐

## 📄 License

[MIT License](LICENSE)

---

**Powered by [Mountsea AI](https://shanhaiapi.com/zh/) – Your All-in-One AI API Platform for Video, Music, Image & Chat Generation**
