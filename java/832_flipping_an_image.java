// Runtime: 8 mss

class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int i = 0;
        for(int[] row : A){
            int[] f = new int[row.length];
            for(int m = 0;m<row.length;m++){
                f[m] = row[row.length -1 -m];
            }

            for(int j=0; j<f.length; j++){
                f[j] = 1 - f[j];
            }
            A[i] = f;
            i++;
        }
        return A;
    }
}