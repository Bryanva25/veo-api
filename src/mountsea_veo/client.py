"""
Veo 3 API Client

Generate AI videos using Google Veo 3, Veo 3 Fast via Mountsea AI.

Documentation: https://docs.mountsea.ai/api-reference/veo/introduction
Platform: https://shanhaiapi.com/zh/
"""

import time
import requests


class VeoClient:
    """Client for Mountsea Veo 3 API.

    Args:
        api_key: Your Mountsea AI API key. Get one at https://shanhaiapi.com/zh/
        base_url: API base URL (default: https://api.mountsea.ai)
        timeout: Request timeout in seconds (default: 30)

    Example:
        >>> client = VeoClient("your-api-key")
        >>> task = client.generate("Aurora borealis over a lake, 4K")
        >>> result = client.wait(task["taskId"])
        >>> print(result["videoUrl"])
    """

    def __init__(self, api_key: str, base_url: str = "https://api.mountsea.ai", timeout: int = 30):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        })

    def generate(self, prompt: str, model: str = "veo-3", duration: int = 5,
                 resolution: str = "1080p", **kwargs) -> dict:
        """Generate a video using Veo 3 or Veo 3 Fast.

        Args:
            prompt: Text description of the video
            model: "veo-3" (default) or "veo-3-fast"
            duration: Video duration in seconds
            resolution: Video resolution
        """
        payload = {"prompt": prompt, "model": model, "duration": duration,
                   "resolution": resolution, **kwargs}
        resp = self._session.post(f"{self.base_url}/veo/generate", json=payload, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def image_to_video(self, prompt: str, image_url: str, model: str = "veo-3", **kwargs) -> dict:
        """Animate an image using Veo 3."""
        return self.generate(prompt=prompt, model=model, imageUrl=image_url, **kwargs)

    def get_task(self, task_id: str) -> dict:
        """Get task status."""
        resp = self._session.get(f"{self.base_url}/veo/task", params={"taskId": task_id},
                                 timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def wait(self, task_id: str, timeout: int = 600, interval: int = 15) -> dict:
        """Wait for task completion."""
        start = time.time()
        while time.time() - start < timeout:
            result = self.get_task(task_id)
            if result.get("status") == "completed":
                return result
            if result.get("status") == "failed":
                raise RuntimeError(f"Veo failed: {result.get('error', 'Unknown')}")
            time.sleep(interval)
        raise TimeoutError(f"Veo task {task_id} timed out after {timeout}s")

