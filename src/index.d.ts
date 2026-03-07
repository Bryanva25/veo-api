export interface VeoClientOptions { baseUrl?: string; timeout?: number; }
export interface GenerateOptions { model?: string; duration?: number; resolution?: string; imageUrl?: string; [key: string]: any; }
export interface TaskResult { taskId: string; status: string; videoUrl?: string; error?: string; }
export interface WaitOptions { timeout?: number; interval?: number; }

export declare class VeoClient {
  constructor(apiKey: string, options?: VeoClientOptions);
  generate(prompt: string, options?: GenerateOptions): Promise<TaskResult>;
  imageToVideo(prompt: string, imageUrl: string, options?: GenerateOptions): Promise<TaskResult>;
  getTask(taskId: string): Promise<TaskResult>;
  wait(taskId: string, options?: WaitOptions): Promise<TaskResult>;
}

