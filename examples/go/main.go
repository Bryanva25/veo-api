// Veo 3 API - Video Generation Example (Go)
// Generate videos using Google Veo 3 / Veo 3 Fast via Mountsea AI
//
// Documentation: https://docs.mountsea.ai/api-reference/veo/introduction
// Platform: https://shanhaiapi.com/zh/

package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"time"
)

const baseURL = "https://api.mountsea.ai"

var apiKey = getEnv("MOUNTSEA_API_KEY", "your-api-key")

func getEnv(key, fallback string) string {
	if v := os.Getenv(key); v != "" {
		return v
	}
	return fallback
}

type VeoRequest struct {
	Prompt     string `json:"prompt"`
	Model      string `json:"model"`
	Duration   int    `json:"duration,omitempty"`
	Resolution string `json:"resolution,omitempty"`
}

type TaskResponse struct {
	TaskID   string `json:"taskId"`
	Status   string `json:"status"`
	VideoURL string `json:"videoUrl"`
	Error    string `json:"error"`
}

func generateVideo(req VeoRequest) (*TaskResponse, error) {
	body, _ := json.Marshal(req)
	httpReq, _ := http.NewRequest("POST", baseURL+"/veo/generate", bytes.NewBuffer(body))
	httpReq.Header.Set("Authorization", "Bearer "+apiKey)
	httpReq.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(httpReq)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	data, _ := io.ReadAll(resp.Body)
	var result TaskResponse
	json.Unmarshal(data, &result)
	return &result, nil
}

func waitForCompletion(taskID string) (*TaskResponse, error) {
	for i := 0; i < 60; i++ {
		req, _ := http.NewRequest("GET", fmt.Sprintf("%s/veo/task?taskId=%s", baseURL, taskID), nil)
		req.Header.Set("Authorization", "Bearer "+apiKey)
		resp, err := http.DefaultClient.Do(req)
		if err != nil {
			return nil, err
		}
		data, _ := io.ReadAll(resp.Body)
		resp.Body.Close()
		var result TaskResponse
		json.Unmarshal(data, &result)
		fmt.Printf("Status: %s\n", result.Status)
		if result.Status == "completed" {
			return &result, nil
		}
		if result.Status == "failed" {
			return nil, fmt.Errorf("failed: %s", result.Error)
		}
		time.Sleep(15 * time.Second)
	}
	return nil, fmt.Errorf("timeout")
}

func main() {
	fmt.Println("🎬 Generating video with Veo 3...")
	task, err := generateVideo(VeoRequest{
		Prompt: "A futuristic city with flying cars and neon lights at night, 4K", Model: "veo-3", Duration: 5,
	})
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	fmt.Printf("Task ID: %s\n", task.TaskID)

	result, err := waitForCompletion(task.TaskID)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	fmt.Printf("✅ Video URL: %s\n", result.VideoURL)
	fmt.Println("\n📘 Docs: https://docs.mountsea.ai/api-reference/veo/introduction")
}

