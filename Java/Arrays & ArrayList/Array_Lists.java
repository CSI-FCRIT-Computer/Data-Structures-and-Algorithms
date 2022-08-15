package Ajinkya.Arrays;

import  java.util.ArrayList;
import java.util.Scanner;

//Note: Your class name can never be ArrayList as it is a keyword
public class Array_Lists
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        /* Syntax
                ==> ArrayList<DataType> listName = new ArrayList<DataType>();
        */

        ArrayList<String> ProgLangs = new ArrayList<String>();

        //To add elements in ArrayList use add()
        ProgLangs.add("Java");
        ProgLangs.add("Kotlin");
        ProgLangs.add("C");
        ProgLangs.add("C++");
        ProgLangs.add("Python");
        System.out.println(ProgLangs);

        //set of elements can be added using loops
        for (int i = 0; i < 5; i++) {
            ProgLangs.add(input.nextLine());
        }
        System.out.println(ProgLangs);

        //To fetch any element use get() method
        String Element3 = ProgLangs.get(3);
        System.out.println(Element3);

        //Similarly there are many other methods to manipulate ArrayLists
        //To remove element
        ProgLangs.remove(5);

        //To modify element
        // Syntax ==> ProgLangs.set(index,String)
        ProgLangs.set(5,"C#");

        //To know size of ArrayList
        ProgLangs.size();

        //To remove all the elements from ArrayList
        ProgLangs.clear();

    }
}