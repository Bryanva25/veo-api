/**
 * Veo 3 API - Video Generation Example (Node.js)
 * Generate videos using Google Veo 3 / Veo 3 Fast via Mountsea AI
 *
 * Documentation: https://docs.mountsea.ai/api-reference/veo/introduction
 * Platform: https://shanhaiapi.com/zh/
 */

const axios = require('axios');

const API_KEY = process.env.MOUNTSEA_API_KEY || 'your-api-key';
const BASE_URL = 'https://api.mountsea.ai';
const headers = { 'Authorization': `Bearer ${API_KEY}`, 'Content-Type': 'application/json' };

async function generateVeoVideo(prompt, model = 'veo-3', duration = 5, resolution = '1080p') {
  const { data } = await axios.post(`${BASE_URL}/veo/generate`,
    { prompt, model, duration, resolution }, { headers });
  return data;
}

async function waitForResult(taskId, timeout = 600000) {
  const start = Date.now();
  while (Date.now() - start < timeout) {
    const { data } = await axios.get(`${BASE_URL}/veo/task`, { headers, params: { taskId } });
    console.log(`Status: ${data.status}`);
    if (data.status === 'completed') return data;
    if (data.status === 'failed') throw new Error(data.error);
    await new Promise(r => setTimeout(r, 15000));
  }
  throw new Error('Timeout');
}

(async () => {
  try {
    // Veo 3
    console.log('🎬 Generating with Veo 3...');
    const task = await generateVeoVideo('Aurora borealis over a frozen lake, 4K cinematic', 'veo-3');
    console.log('Task ID:', task.taskId);
    const result = await waitForResult(task.taskId);
    console.log('✅ Video URL:', result.videoUrl);

    // Veo 3 Fast
    console.log('\n⚡ Quick generation with Veo 3 Fast...');
    const task2 = await generateVeoVideo('A puppy running on the beach', 'veo-3-fast', 3);
    console.log('Task ID:', task2.taskId);
  } catch (err) {
    console.error('Error:', err.message);
  }
  console.log('\n📘 Docs: https://docs.mountsea.ai/api-reference/veo/introduction');
  console.log('🏠 Platform: https://shanhaiapi.com/zh/');
})();

