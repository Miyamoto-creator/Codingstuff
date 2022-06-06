using System;

public class Kata
{
  static void Main(string[] args)
  {
      string name;
      
      // Passing value to string

      name = "Roger";
      
      Console.WriteLine(Greet(name));
  }
  public static string Greet(string name)
  {
      return $"Hello, {name} how are you doing today?";
  }
}