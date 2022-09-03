package com.stack;

import java.util.Stack;

public class InbuiltStack {
    public static void main(String[] args)
    {
        Stack<String> colour = new Stack<>();
        /*Syntax
                Stack<Type> stacks = new Stack<>();*/


        // Add elements to Stack
        colour.push("Red");
        colour.push("Yellow");
        colour.push("Blue");
        colour.push("Green");
        colour.push("Saffron");

        // Remove element stacks
            // color.pop()
        System.out.println(colour.pop());

        // Access element from the top
            //colour.peek();
        System.out.println(colour.peek());

        /* Search an element
            search(" ") will return the position of the element in the stack*/
        System.out.println(colour.search("Saffron"));

        /* Check if stack is empty
             it returns boolean i.e. true or false*/
        System.out.println(colour.empty());

    }
}
