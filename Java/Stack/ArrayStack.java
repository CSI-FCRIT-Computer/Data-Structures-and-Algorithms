package com.stack;

import java.util.Scanner;

public class ArrayStack {
    private int top=-1;
    private int size;
    private int stack[] = new int[10];
    //The size of stack can be a user input
    boolean empty()
    {
        if(top >= 0)
        {
            return false;
        }
        else
        {
            return true;
        }
    }

    int peek()
    {
        if(empty())
        {
            System.out.println("\n Stack is empty");
            return 0;
        }
        else
        {
            System.out.println("\n Top of Stack: "+ stack[top]);
            return stack[top];
        }
    }

    void push(int num)
    {
        if(top == size)
        {
            System.out.println("\n Stack overflow");
        }
        else
        {
            stack[++top] = num;
            System.out.println("\n "+num+" is inserted in stack");
        }
    }


    int pop()
    {
        if(top < 0)
        {
            System.out.println("\n Stack Empty");
            return 0;
        }
        else
        {
            int x = stack[top--];
            System.out.println("\n "+ x +" removed from stack");
            return x;
        }
    }
    void display()
    {
        if(empty())
        {
            System.out.println("\n Stack is empty");
        }
        else
        {
            System.out.print("\n Stack : ");
            for(int i=0; i<=top; i++)
            {
                System.out.print(" | "+ stack[i]);
            }
        }
    }


    public static void main(String []agrs)
    {
        boolean flag = true;
        int option, num, size;
        Scanner in = new Scanner(System.in);
        ArrayStack stk = new ArrayStack();
        System.out.print("-------------- Stack using Array --------------");

        while(flag)
        {
            System.out.println("\n\n 1. PUSH\n 2. PEEK\n 3. POP\n 4. DISPLAY\n 5. QUIT\n Select Operation : ");
            option = in.nextInt();
            switch (option) {
                case 1 -> {
                    System.out.println(" Enter elements of stack : ");
                    num = in.nextInt();
                    stk.push(num);
                }
                case 2 -> stk.peek();
                case 3 -> stk.pop();
                case 4 -> stk.display();
                case 5 -> flag = false;
            }
        }
    }
}