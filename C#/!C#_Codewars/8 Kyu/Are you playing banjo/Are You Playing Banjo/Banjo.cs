using System;

public class Kata
{
  static void Main(string[] args)
  {
      string name;
      
      // Passing value to Arg

      name = "Roger";
      
      Console.WriteLine(AreYouPlayingBanjo(name));
  }
  public static string AreYouPlayingBanjo(string name)
  {
      string result = "";
    
      if (name[0] == 'R' || name[0] == 'r')
      {
          result = name + " plays banjo";
      }
      else
      {
          result = name + " does not play banjo";
      }
      
      return result;
  }
}