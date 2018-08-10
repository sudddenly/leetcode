public class Solution {
    public int distributeCandies(int[] candies) {
        return Math.min(candies.length / 2, IntStream.of(candies).boxed().collect(Collectors.toSet()).size());
    }
}