using System;
public class funcexer3
{
    public static int Sum(int num1, int num2)
    {
        int total;
        total = num1 + num2;
        return total;
    }
     
    public static void Main()
    {
      Console.WriteLine("\nThe sum of two numbers is : {0} \n", Sum(5,2) );
    }
}