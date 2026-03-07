/**
 * Veo 3 API - Video Generation Example (Java)
 * Generate videos using Google Veo 3 / Veo 3 Fast via Mountsea AI
 *
 * Documentation: https://docs.mountsea.ai/api-reference/veo/introduction
 * Platform: https://shanhaiapi.com/zh/
 *
 * Dependencies: Java 11+ (uses java.net.http)
 */

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class VeoApiExample {

    private static final String API_KEY = System.getenv("MOUNTSEA_API_KEY") != null
            ? System.getenv("MOUNTSEA_API_KEY") : "your-api-key";
    private static final String BASE_URL = "https://api.mountsea.ai";

    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        // Veo 3 - Text to Video
        System.out.println("🎬 Generating with Veo 3...");
        String body = """
                {
                    "prompt": "An eagle soaring over snowy mountains at sunrise, cinematic 4K",
                    "model": "veo-3",
                    "duration": 5,
                    "resolution": "1080p"
                }
                """;

        HttpRequest req = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/veo/generate"))
                .header("Authorization", "Bearer " + API_KEY)
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(body))
                .build();

        HttpResponse<String> resp = client.send(req, HttpResponse.BodyHandlers.ofString());
        System.out.println("Response: " + resp.body());

        // Veo 3 Fast
        System.out.println("\n⚡ Generating with Veo 3 Fast...");
        String fastBody = """
                {
                    "prompt": "A cat playing with a ball",
                    "model": "veo-3-fast",
                    "duration": 3
                }
                """;

        HttpRequest fastReq = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/veo/generate"))
                .header("Authorization", "Bearer " + API_KEY)
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(fastBody))
                .build();

        HttpResponse<String> fastResp = client.send(fastReq, HttpResponse.BodyHandlers.ofString());
        System.out.println("Response: " + fastResp.body());

        System.out.println("\n📘 Docs: https://docs.mountsea.ai/api-reference/veo/introduction");
        System.out.println("🏠 Platform: https://shanhaiapi.com/zh/");
    }
}

