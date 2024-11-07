import java.util.Scanner;

public class CustomHashTable {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int table[] = new int[10];
        String input = "";

        while (!input.equals("exit")) {
            System.out.println("Enter the number of element to be inserted or type 'exit' to stop");
            input = scanner.nextLine();
            if (!input.equals("exit")) {
                table = addElement(table, input);
            }
        }

        System.out.println("Enter value to search");
        String searchKey = scanner.nextLine();
        findElement(table, searchKey);

        for (int i = 0; i < table.length; i++) {
            System.out.print(table[i] + " ");
        }

        scanner.close();
    }

    public static int[] addElement(int table[], String input) {
        int hashValue = 0;
        for (int i = 0; i < input.length(); i++) {
            hashValue += (int) input.charAt(i);
        }
        int index = hashValue % table.length;
        boolean added = false;

        if (table[index] == 0) {
            table[index] = hashValue;
        } else {
            for (int i = index + 1; i < table.length; i++) {
                if (table[i] == 0) {
                    table[i] = hashValue;
                    added = true;
                    break;
                }
            }
            if (!added) {
                System.out.println("Hash table is full");
            }
        }
        return table;
    }

    public static void findElement(int table[], String searchKey) {
        int hashValue = 0;
        for (int i = 0; i < searchKey.length(); i++) {
            hashValue += (int) searchKey.charAt(i);
        }
        int index = hashValue % table.length;
        boolean located = false;

        if (table[index] == hashValue) {
            System.out.println("Element found at position " + index);
        } else {
            for (int i = index + 1; i < table.length; i++) {
                if (table[i] == hashValue) {
                    System.out.println("Element found at position " + i);
                    located = true;
                    break;
                }
            }
            if (!located) {
                System.out.println("Element not found");
            }
        }
    }
}

