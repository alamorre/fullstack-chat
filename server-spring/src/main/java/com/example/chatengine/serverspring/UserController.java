package com.example.chatengine.serverspring;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {
    // private static String CHAT_ENGINE_PROJECT_ID =
    // "5d498a31-cd23-42b7-b367-4fcc9463bd2f";
    private static String CHAT_ENGINE_PRIVATE_KEY = "49a46286-91c3-4f9c-92bf-284ae51b7628";

    @RequestMapping(path = "/login", method = RequestMethod.GET)
    public String getLogin() {
        return "user allowed";
    }

    @RequestMapping(path = "/signup", method = RequestMethod.GET)
    public String newSignup() {
        HttpURLConnection connection = null;
        try {
            // Create connection
            URL url = new URL("https://api.chatengine.io/users");
            connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            // Headers
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Accept", "application/json");
            connection.setRequestProperty("Private-Key", CHAT_ENGINE_PRIVATE_KEY);
            // Add body
            connection.setDoOutput(true);
            String jsonInputString = "{\"username\": \"adam1\", \"secret\": \"pass1234\", \"first_name\": \"adam\", \"last_name\": \"lamorre\", \"email\": \"alamorre@mail.ca\"}";
            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }
            // Generate and return response
            try (BufferedReader br = new BufferedReader(
                    new InputStreamReader(connection.getInputStream(), "utf-8"))) {
                StringBuilder response = new StringBuilder();
                String responseLine = null;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                return response.toString();
            }

        } catch (Exception e) {
            e.printStackTrace();
            return null;
        } finally {
            if (connection != null) {
                connection.disconnect();
            }
        }
    }
}
