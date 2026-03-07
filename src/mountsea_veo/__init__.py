"""
Mountsea Veo SDK - Generate videos with Google Veo 3 API

Quick Start:
    >>> from mountsea_veo import VeoClient
    >>> client = VeoClient("your-api-key")
    >>> task = client.generate("A sunset over the ocean, cinematic 4K")
    >>> result = client.wait(task["taskId"])
    >>> print(result["videoUrl"])

Documentation: https://docs.mountsea.ai/api-reference/veo/introduction
Platform: https://shanhaiapi.com/zh/
"""

from .client import VeoClient

__version__ = "1.0.0"
__all__ = ["VeoClient"]

