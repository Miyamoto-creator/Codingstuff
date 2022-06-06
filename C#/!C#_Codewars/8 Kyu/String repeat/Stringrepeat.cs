using System;

public class Kata
{
  static void Main(string[] args)
  {
      int n = 6;
      string s = "A";
      
      Console.WriteLine(Greet(n, s));
  }
  public static string RepeatStr(int n, string s)
  {
    return new string(s, n);
  }
}