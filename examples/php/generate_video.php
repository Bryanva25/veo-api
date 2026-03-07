<?php
/**
 * Veo 3 API - Video Generation Example (PHP)
 * Generate videos using Google Veo 3 / Veo 3 Fast via Mountsea AI
 *
 * Documentation: https://docs.mountsea.ai/api-reference/veo/introduction
 * Platform: https://shanhaiapi.com/zh/
 */

$API_KEY = getenv('MOUNTSEA_API_KEY') ?: 'your-api-key';
$BASE_URL = 'https://api.mountsea.ai';

function veoGenerate(string $prompt, string $model = 'veo-3', int $duration = 5): array
{
    global $API_KEY, $BASE_URL;
    $ch = curl_init("$BASE_URL/veo/generate");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_HTTPHEADER => ["Authorization: Bearer $API_KEY", 'Content-Type: application/json'],
        CURLOPT_POSTFIELDS => json_encode(['prompt' => $prompt, 'model' => $model, 'duration' => $duration]),
    ]);
    $response = curl_exec($ch);
    curl_close($ch);
    return json_decode($response, true);
}

function getStatus(string $taskId): array
{
    global $API_KEY, $BASE_URL;
    $ch = curl_init("$BASE_URL/veo/task?taskId=$taskId");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => ["Authorization: Bearer $API_KEY"],
    ]);
    $response = curl_exec($ch);
    curl_close($ch);
    return json_decode($response, true);
}

// Veo 3
echo "🎬 Generating with Veo 3...\n";
$task = veoGenerate('A beautiful aurora borealis over a frozen lake, 4K cinematic', 'veo-3');
echo "Task ID: {$task['taskId']}\n";

// Veo 3 Fast
echo "\n⚡ Quick generation with Veo 3 Fast...\n";
$task2 = veoGenerate('A puppy running on the beach', 'veo-3-fast', 3);
echo "Task ID: {$task2['taskId']}\n";

echo "\n📘 Docs: https://docs.mountsea.ai/api-reference/veo/introduction\n";
echo "🏠 Platform: https://shanhaiapi.com/zh/\n";

