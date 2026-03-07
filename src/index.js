/**
 * Mountsea Veo SDK - Generate videos with Google Veo 3 API
 *
 * @example
 * const { VeoClient } = require('mountsea-veo');
 * const client = new VeoClient('your-api-key');
 * const task = await client.generate('Aurora borealis, 4K cinematic');
 * const result = await client.wait(task.taskId);
 * console.log(result.videoUrl);
 *
 * Documentation: https://docs.mountsea.ai/api-reference/veo/introduction
 * Platform: https://shanhaiapi.com/zh/
 */

const https = require('https');
const http = require('http');
const { URL } = require('url');

class VeoClient {
  constructor(apiKey, options = {}) {
    this.apiKey = apiKey;
    this.baseUrl = (options.baseUrl || 'https://api.mountsea.ai').replace(/\/$/, '');
    this.timeout = options.timeout || 30000;
  }

  async generate(prompt, options = {}) {
    return this._post('/veo/generate', {
      prompt, model: 'veo-3', duration: 5, resolution: '1080p', ...options
    });
  }

  async imageToVideo(prompt, imageUrl, options = {}) {
    return this.generate(prompt, { imageUrl, ...options });
  }

  async getTask(taskId) {
    return this._get(`/veo/task?taskId=${encodeURIComponent(taskId)}`);
  }

  async wait(taskId, options = {}) {
    const timeout = options.timeout || 600000;
    const interval = options.interval || 15000;
    const start = Date.now();
    while (Date.now() - start < timeout) {
      const result = await this.getTask(taskId);
      if (result.status === 'completed') return result;
      if (result.status === 'failed') throw new Error(`Veo failed: ${result.error || 'Unknown'}`);
      await new Promise(r => setTimeout(r, interval));
    }
    throw new Error(`Veo task ${taskId} timed out`);
  }

  _post(path, body) { return this._request('POST', path, body); }
  _get(path) { return this._request('GET', path); }

  _request(method, path, body) {
    return new Promise((resolve, reject) => {
      const url = new URL(this.baseUrl + path);
      const mod = url.protocol === 'https:' ? https : http;
      const req = mod.request({
        method, hostname: url.hostname, port: url.port, path: url.pathname + url.search,
        headers: { 'Authorization': `Bearer ${this.apiKey}`, 'Content-Type': 'application/json' },
        timeout: this.timeout,
      }, (res) => {
        let data = '';
        res.on('data', c => data += c);
        res.on('end', () => { try { resolve(JSON.parse(data)); } catch { reject(new Error(data)); } });
      });
      req.on('error', reject);
      if (body) req.write(JSON.stringify(body));
      req.end();
    });
  }
}

module.exports = { VeoClient };

