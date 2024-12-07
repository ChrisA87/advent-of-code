package year_2024;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Day01 {
    public static void main(String[] args) {
        String relativePath = "../../src/aoc/2024/data/01.txt";
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        try {
            // Convert relative path to absolute path
            Path filePath = Paths.get(relativePath).toAbsolutePath().normalize();

            parseDataFromCsv(filePath.toString(), left, right);
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
            return;
        }
        // Sort the data after parsing
        Collections.sort(left);
        Collections.sort(right);

        // Part 1
        System.out.println("Part 1: " + part1(left, right));

        // Part 2
        System.out.println("Part 2: " + part2(left, right));
    }

    private static void parseDataFromCsv(String filePath, List<Integer> left, List<Integer> right) throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split("\\s+");
                if (parts.length >= 2) {
                    left.add(Integer.parseInt(parts[0].trim()));
                    right.add(Integer.parseInt(parts[1].trim()));
                }
            }
        }
    }

    private static int part1(List<Integer> left, List<Integer> right) {
        int sum = 0;
        for (int i = 0; i < left.size(); i++) {
            sum += Math.abs(left.get(i) - right.get(i));
        }
        return sum;
    }

    private static int part2(List<Integer> left, List<Integer> right) {
        Map<Integer, Long> rightCounts = right.stream()
                .collect(Collectors.groupingBy(e -> e, Collectors.counting()));

        int sum = 0;
        for (int x : left) {
            sum += (int) (x * rightCounts.getOrDefault(x, 0L));
        }
        return sum;
    }
}
