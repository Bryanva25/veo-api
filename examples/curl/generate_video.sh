#!/bin/bash
# Veo 3 API - Video Generation Examples (cURL)
# Supports Veo 3, Veo 3.1, Veo 3 Fast
#
# Documentation: https://docs.mountsea.ai/api-reference/veo/introduction
# Platform: https://shanhaiapi.com/zh/

API_KEY="${MOUNTSEA_API_KEY:-your-api-key}"
BASE_URL="https://api.mountsea.ai"

echo "🎬 Veo 3 API Examples"
echo "====================="

# Veo 3 - Text to Video
echo ""
echo "📌 Veo 3 - Text to Video:"
curl -s -X POST "${BASE_URL}/veo/generate" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A beautiful aurora borealis over a frozen lake, 4K cinematic",
    "model": "veo-3",
    "duration": 5,
    "resolution": "1080p"
  }'

# Veo 3 Fast
echo ""
echo "📌 Veo 3 Fast - Quick Generation:"
curl -s -X POST "${BASE_URL}/veo/generate" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A puppy running on the beach",
    "model": "veo-3-fast",
    "duration": 3
  }'

# Check status
echo ""
echo "📌 Check Task Status:"
echo "curl -X GET '${BASE_URL}/veo/task?taskId=YOUR_TASK_ID' -H 'Authorization: Bearer YOUR_API_KEY'"

echo ""
echo "🔗 Docs: https://docs.mountsea.ai/api-reference/veo/introduction"
echo "🏠 Platform: https://shanhaiapi.com/zh/"

