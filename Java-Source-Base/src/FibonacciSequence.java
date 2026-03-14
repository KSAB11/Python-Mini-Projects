public class FibonacciSequence {

    public static void fiboSequence() {
        int row = 1;
        int firstTerm = 0;
        int secondTerm = 1;
        int count;

        while (row <= 8) {
            count = 1;

            while (count <= row) {
                System.out.println(firstTerm + "\t");

                int lastTerm = firstTerm + secondTerm;
                firstTerm = secondTerm;
                secondTerm = lastTerm;

                count++;
            }
            row++;
        }
    }
    public static void main(String[] args) {
        fiboSequence();
    }
}