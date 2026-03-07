"""
Veo 3 API - Video Generation Example (Python)
Generate videos using Google Veo 3 / Veo 3 Fast via Mountsea AI

Documentation: https://docs.mountsea.ai/api-reference/veo/introduction
Platform: https://shanhaiapi.com/zh/
"""

import requests
import time
import os

API_KEY = os.environ.get("MOUNTSEA_API_KEY", "your-api-key")
BASE_URL = "https://api.mountsea.ai"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def text_to_video(prompt: str, model: str = "veo-3", duration: int = 5, resolution: str = "1080p") -> dict:
    """Generate video with Veo 3 or Veo 3 Fast."""
    response = requests.post(
        f"{BASE_URL}/veo/generate",
        headers=HEADERS,
        json={"prompt": prompt, "model": model, "duration": duration, "resolution": resolution}
    )
    response.raise_for_status()
    return response.json()


def image_to_video(prompt: str, image_url: str, model: str = "veo-3", duration: int = 5) -> dict:
    """Animate an image using Veo 3."""
    response = requests.post(
        f"{BASE_URL}/veo/generate",
        headers=HEADERS,
        json={"prompt": prompt, "imageUrl": image_url, "model": model, "duration": duration}
    )
    response.raise_for_status()
    return response.json()


def wait_for_completion(task_id: str, timeout: int = 600, interval: int = 15) -> dict:
    """Poll until task completes."""
    start = time.time()
    while time.time() - start < timeout:
        resp = requests.get(f"{BASE_URL}/veo/task", headers=HEADERS, params={"taskId": task_id})
        result = resp.json()
        print(f"Status: {result.get('status')}")
        if result['status'] == 'completed':
            return result
        if result['status'] == 'failed':
            raise Exception(f"Failed: {result.get('error')}")
        time.sleep(interval)
    raise TimeoutError(f"Timeout for task {task_id}")


if __name__ == "__main__":
    # Veo 3 - Text to Video
    print("🎬 Generating video with Veo 3...")
    task = text_to_video("A majestic eagle soaring over mountains at sunrise, cinematic 4K", model="veo-3")
    print(f"Task ID: {task['taskId']}")
    result = wait_for_completion(task['taskId'])
    print(f"✅ Video URL: {result.get('videoUrl')}")

    # Veo 3 Fast - Quick generation
    print("\n⚡ Quick generation with Veo 3 Fast...")
    task2 = text_to_video("A cat playing with yarn", model="veo-3-fast", duration=3)
    print(f"Task ID: {task2['taskId']}")

    print("\n📘 Docs: https://docs.mountsea.ai/api-reference/veo/introduction")
    print("🏠 Platform: https://shanhaiapi.com/zh/")

